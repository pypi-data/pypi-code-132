#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools

import pyleoclim as pyleo
import numpy as np
import pandas as pd
import multiprocessing as mp

from pyrqa.time_series import EmbeddedSeries
from pyrqa.settings import Settings
from pyrqa.analysis_type import Classic
from pyrqa.neighbourhood import FixedRadius
from pyrqa.metric import EuclideanMetric
from pyrqa.computation import RPComputation

from ..core.recurrence_matrix import RecurrenceMatrix
from ..core.recurrence_network import RecurrenceNetwork
from ..utils.parameters import tau_search
from ..utils.range_finder import range_finder


class TimeEmbeddedSeries:
    '''Time embedded time series object. Precursor to recurrence matrix and recurrence network.

    series : pyleo.Series object or pandas.Series object
        Time series to be embedded
    
    m : int
        Embedding dimension
    
    tau : int
        Embedding delay, will be calculated according to first minimum of mutual information if not passed

    embedded_data : array
        Time delay embedded data. If not passed will be calculated from series, m, and tau

    embedded_time : array
        Time axis corresponding to embedded_data. If embedded_data is passed without embedded_time, an error will be raised

    value_name : str
        Value name

    value_unit : str
        Value units

    time_name : str
        Time name

    time_unit : str
        Time units

    label : str
        Label for embedding
    '''

    def __init__(self,series,m,tau=None,embedded_data=None,embedded_time=None,value_name=None,value_unit=None,time_name=None,time_unit=None,label=None):
        self.series = series
        self.m = m
        self.tau = tau
        self.embedded_data = embedded_data
        self.embedded_time = embedded_time
        self.value_name = value_name
        self.value_unit = value_unit
        self.time_name = time_name
        self.time_unit = time_unit
        self.label = label

        if self.embedded_data is not None and self.embedded_time is None:
            raise ValueError('Embedded data was passed without associated time axis. Please pass neither or both')

        if self.tau is None:
            self.tau = tau_search(self.series)

        if self.embedded_data is None:

            if isinstance(self.series, (pyleo.core.Series, pyleo.core.LipdSeries)):
                values = self.series.value
                time_axis = self.series.time[:(-self.m*self.tau)]

            elif isinstance(self.series,pd.Series):
                values = self.series.values
                time_axis = list(self.series.index)[:(-self.m*self.tau)]

            else:
                raise ValueError('Unrecognized data type. Please pass a pyleoclim Series or pandas Series type object')
            
            manifold = np.ndarray(shape = (len(values)-(self.m*self.tau),self.m))

            for idx, i in enumerate(values):
                if idx < (len(values)-(self.m*self.tau)):
                    manifold[idx] = values[idx:idx+(self.m*self.tau):self.tau]

            self.embedded_data = manifold
            self.embedded_time = time_axis

        if self.value_name is None:
            self.value_name = self.series.value_name
        
        if self.value_unit is None:
            self.value_unit = self.series.value_unit

        if self.time_name is None:
            self.time_name = self.series.time_name
        
        if self.time_unit is None:
            self.time_unit = self.series.time_unit
        
        if self.label is None:
            self.label = self.series.label

    def create_recurrence_matrix(self,epsilon):
        '''Function to create Recurrence Matrix object
        
        Parameters
        ----------
        
        epsilon : float
            Fixed radius used to calculate whether two points are recurrent
            
        Returns
        -------
        
        RecurrenceMatrix : ammonyte.RecurrenceMatrix object'''

        ts = EmbeddedSeries(self.embedded_data)

        settings = Settings(ts,
                            analysis_type=Classic,
                            neighbourhood=FixedRadius(epsilon),
                            similarity_measure=EuclideanMetric)

        computation = RPComputation.create(settings,
                                        verbose=False)

        result = computation.run()

        matrix = result.recurrence_matrix

        return RecurrenceMatrix(matrix=matrix,time=self.embedded_time,epsilon=epsilon,series=self.series, m = self.m, tau = self.tau,
                                value_name=self.value_name,value_unit=self.value_unit,time_name=self.time_name,
                                time_unit=self.time_unit,label=self.label)

    def create_recurrence_network(self,epsilon):
        '''Function to create Recurrence Network object
        
        Parameters
        ----------
        
        epsilon : float
            Fixed radius used to calculate whether two points are recurrent.
            
        Returns
        -------
        
        RecurrenceNetwork : ammonyte.RecurrenceNetwork object'''

        ts = EmbeddedSeries(self.embedded_data)

        settings = Settings(ts,
                            analysis_type=Classic,
                            neighbourhood=FixedRadius(epsilon),
                            similarity_measure=EuclideanMetric)

        computation = RPComputation.create(settings,
                                        verbose=False)

        result = computation.run()

        matrix = result.recurrence_matrix

        return RecurrenceNetwork(matrix=matrix,time=self.embedded_time,epsilon=epsilon,series=self.series,
                                value_name=self.value_name,value_unit=self.value_unit,time_name=self.time_name,
                                time_unit=self.time_unit,label=self.label)

    def find_epsilon(self,eps,target_density=.05,tolerance=.01,initial_hitrate=None,parallelize=True,num_processes=None,amp=10,verbose=True):
        '''Function to find epsilon value given target recurrence matrix density
        
        Parameters
        ----------

        eps : float
            Starting epsilon value (best guess)

        target_density : float
            Desired recurrence matrix hitrate

        tolerance : float
            Amount of allowable difference between target hitrate and actual hitrate

        initial_hitrate : float
            If you've already calculated the initial hitrate for your settings you can pass it here to save computation time

        parallelize : bool; {True,False}
            Whether or not to parallelize the search process. Currently only tested on macOS, could be issues running this on Windows.

        num_processes : int
            Number of processes to run, automatically set to your cpu count

        amp : int
            The amplitude of the range of epsilon value search. Higher values cover ground quickly but converge slowly, the opposite is true for lower values

        verbose : bool; {True,False}
            Whether or not to print output after each iteration

        Returns
        -------

        epsilon : float
            Epsilon value that produces desired recurrence density within tolerance value provided.

        See also
        --------

        ammonyte.utils.rm_search
        '''

        if num_processes is None:
            if mp.cpu_count() > 2:
                num_processes = mp.cpu_count() - 2
            else:
                num_processes = 1
        
        if initial_hitrate == None:

            initial_result = self.create_recurrence_matrix(eps)
            initial_hitrate = np.sum(initial_result.matrix)/np.size(initial_result.matrix)
            if verbose:
                print(f'Initial hitrate is {initial_hitrate:.4f}')
        
        if np.abs(initial_hitrate - target_density) <= tolerance:
            if verbose:
                print('Initial hitrate is within the tolerance window!')
            results = {'Epsilon':eps,'Output':initial_result}
            return results
        else:
            if verbose:
                print('Initial hitrate is not within the tolerance window, searching...')
            hitrate = initial_hitrate
            flag = True

        if parallelize:

            while flag:

                with mp.Pool(num_processes) as pool:
                    
                    eps_range, flag = range_finder(eps,hitrate,target_density,tolerance,num_processes,amp,verbose)
                    
                    if flag is False:
                        
                        eps = eps_range
                        results = {'Epsilon':eps,'Output':self.create_recurrence_matrix(eps)}
                        return results

                    r = pool.starmap(self.create_recurrence_matrix, zip(eps_range))
                    
                    pool.close()
                    pool.join()

                for item in r:
                    matrix = item.matrix
                    new_eps = item.epsilon
                    new_hitrate = np.sum(matrix)/np.size(matrix)

                    if np.abs(new_hitrate - .05) < np.abs(hitrate -.05):
                        hitrate = new_hitrate
                        eps = new_eps
        
        else:

            while flag:
            
                eps_range, flag = range_finder(eps,hitrate,target_density,tolerance,num_processes,amp,verbose)

                if flag is False:
                        
                        eps = eps_range
                        results = {'Epsilon':eps,'Output':self.create_recurrence_matrix(eps)}
                        return results
                
                for eps in eps_range:

                    item = self.create_recurrence_matrix(eps)
                    matrix = item.matrix
                    new_eps = item.epsilon
                    new_hitrate = np.sum(matrix)/np.size(matrix)

                    if np.abs(new_hitrate - .05) < np.abs(hitrate -.05):
                        hitrate = new_hitrate
                        eps = new_eps
        
        return results

