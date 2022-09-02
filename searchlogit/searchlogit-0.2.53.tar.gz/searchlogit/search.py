from .multinomial_logit import MultinomialLogit
from .mixed_logit import MixedLogit
from .latent_class_model import LatentClassModel
from .latent_class_mixed_model import LatentClassMixedModel
import numpy as np

import time
import datetime
import matplotlib.pyplot as plt
import os
import sys
import math
import copy
import logging
from ._device import device as dev

logger = logging.getLogger(__name__)

# global vars
# boxc_l is the list of suffixes used to denote manually transformed variables
boxc_l = ['L1', 'L2']  # ['L1','L2','L3']
l1 = np.log
l2 = 0.5


class Solution(dict):

    # Counter used to track solution progression
    sol_counter = 0

    def __init__(self, *arg, **kw):
        self['bic'] = 10000000.0
        self['MAE'] = 1.0
        self['loglik'] = -10000000.0
        self['asvars'] = []
        self['isvars'] = []
        self['randvars'] = {}
        self['bcvars'] = []
        self['cor_vars'] = []
        self['bctrans'] = []
        self['cor'] = False
        self['class_params_spec'] = None
        self['member_params_spec'] = None
        self['asc_ind'] = False
        self['sol_num'] = Solution.sol_counter
        Solution.sol_counter += 1
        super(Solution, self).__init__(*arg, **kw)

    def add_objective(self, bic, MAE=1.0, loglik=-10000000.0):
        self['bic'] = bic
        self['MAE'] = MAE
        self['loglik'] = loglik


class Search():
    """Class for the IGHS search algorithm for choice models.
    Attributes
    ----------
    df : pandas.DataFrame
        Dataframe for training data.

    df_test : pandas.DataFrame
        Dateframe for testing data.

    varnames : list-like, shape (n_variables,)
        Names of explanatory variables.

    dist : list, default=None
        Random distributions to select from.

    code_name : str, default="search"
        Name for the search, used in save files.

    avail : array-like, shape (n_samples*n_alts,), default=None
        Availability of alternatives for the choice situations. One
        when available or zero otherwise.

    test_av  array-like, default=None
        Availability of alternatives for the choice situations of
        the testing dataset.

    weights : array-like, shape(n_samples,), default=None
        Sample weights in long format.

    test_weight_var : array-like, shape(n_samples,), default=None
        Sample weights in long format for test dataset.

    choice_set : list of str, default=None
        Alternatives in the choice set.

    choice_var : array-like, default=None
        Choice variable for each observation.

    test_choice_var : array-like, default=None
        Choice variable for each observation of the test dataframe.

    alt_var : array_like, default=None
        Alternative for each row of the training dataframe.

    test_alt_var : array_like, default=None
        Alternative for each row of the testing dataframe.

    choice_id : array_like, default=None
        Custom ids (i.e. choice id) for the training dataframe.

    test_choice_id : array_like, default=None
        Custom ids (i.e. choice id) for the testing dataframe.

    ind_id : array_like, default=None
        Individual ids for the training dataframe.

    test_ind_id : array_like, default=None
        Individual ids for the testing dataframe.

    isvarnames : list, default=None
        Individual-specific variables in varnames.

    asvarnames : list, default=None
        Alternative-specific variables in varnames.

    trans_asvars : list, default=None  # TODO? necessary?
        List of asvars manually transformed.

    ftol : float, default=1e-5
        Sets the tol parameter in scipy.optimize.minimize - Tolerance
        for termination. Also tol parameter for EM algorithm for
        latent classes.

    gtol : float, default=1e-5
        Sets the gtol parameter in scipy.optimize.minimize -
        Gradient norm must be less than gtol before successful
        termination.

    latent_class : bool, default=False
        Option to use latent class models in the search algorithm.

    num_classes : int, default-2
        Sets the number of classes if using latent class models.

    maxiter : int, default=200
        Maximum number of iterations.

    multi_objective : bool, default=False
        Option to use the multi-objective heuristic (training BIC
        and out of sample MAE) or single-objective (training BIC).

    p_val : float, default=0.05
        P-value used to test for non-significance of model coefficients.

    chosen_alts_test: array-like, default=True
        Array of alts of each choice.

    allow_random : bool, default=True  # TODO? temporary - another prespecified approach?
        Allow random variables to be included in the model.

    allow_bcvars : bool, default=True  # TODO? temporary - another prespecified approach?
        Allow transformation variables to be included in the model.

    base_alt : int, float, or str, default=None
        Base alternative.
    """
    def __init__(self, df, varnames, df_test=None, dist=None, code_name="search",
                 avail=None, test_av=None, avail_latent=None,
                 test_avail_latent=None, weights=None,
                 choice_set=None,
                 choice_var=None, test_choice_var=None,
                 alt_var=None, test_alt_var=None,
                 choice_id=None, test_choice_id=None, ind_id=None,
                 test_ind_id=None, isvarnames=None,
                 asvarnames=None, trans_asvars=None, ftol=1e-5, gtol=1e-5,
                 gtol_membership_func=1e-5,
                 latent_class=False, num_classes=2, maxiter=200, n_draws=1000,
                 multi_objective=False, p_val=0.05, chosen_alts_test=None,
                 test_weight_var=None,
                 allow_random=True, allow_bcvars=True,
                 intercept_opts=None, base_alt=None,
                 val_share=0.25,
                 logger_level=None,
                 seed=None):
        """Initialise the search class.

        """
        if dist is None:
            logger.debug("Dist not specifying. Allowing all random distributions.")
            dist = ['n', 'ln', 'tn', 'u', 't', 'f']

        self.dist = dist  # List of random distributions to select from
        self.code_name = code_name
        self.current_date = datetime.datetime.now().strftime("%d%m%Y-%H%M%S")

        logger_name = "logs/" + code_name + "_" + self.current_date + ".log"
        try:
            os.makedirs("logs/", exist_ok=True)
        except Exception as e:
            print('e: ', e)
            logger_name = code_name + "_" + self.current_date + ".log"
        if logger_level is None:
            logger_level = logging.INFO
        logging.basicConfig(filename=logger_name, level=logger_level)
        self.logger_name = logger_name

        self.df = df
        self.varnames = varnames

        self.val_share = val_share

        random_state = None
        if seed:
            random_state = np.random.RandomState(seed)
        random_state = random_state or np.random
        self.random_state = random_state
        if df_test is None and multi_objective:
            # create test dataset
            if ind_id is not None:
                N = len(np.unique(ind_id))
                training_size = int((1-val_share)*N)
                ids = random_state.choice(np.unique(ind_id), training_size, replace=False)
                train_idx = [ii for ii, id_val in enumerate(ind_id) if id_val in ids]
                test_idx = [ii for ii, id_val in enumerate(ind_id) if id_val not in ids]

            else:
                try:
                    N = len(np.unique(df['id'].values))
                    id_key = 'id'
                except KeyError:
                    N = len(np.unique(df['ID'].values))
                    id_key = 'ID'
                training_size = int(val_share*N)
                ids = random_state.choice(N, training_size, replace=False)
                train_idx = [ii for ii, id_val in enumerate(df[id_key]) if id_val in ids]
                test_idx = [ii for ii, id_val in enumerate(df[id_key]) if id_val not in ids]

                train_idx = [ii for ii, id_val in enumerate(df['id']) if id_val in ids]
                test_idx = [ii for ii, id_val in enumerate(df['id']) if id_val not in ids]

            df_train = df.loc[train_idx, :]
            df_test = df.loc[test_idx, :]

            self.df = df_train

            if avail is not None:
                test_av = avail[test_idx]
                avail = avail[train_idx]

            if avail_latent is not None:
                avail_latent_original = avail_latent
                J = len(np.unique(alt_var))
                avail_latent = [np.zeros((int(len(train_idx)/J), J)) for i in range(num_classes)]
                test_avail_latent = [np.zeros((int(len(test_idx)/J), J)) for i in range(num_classes)]
                for ii, avail_l in enumerate(avail_latent_original):
                    if avail_l is None:
                        avail_latent[ii] = None
                        test_avail_latent[ii] = None
                    else:
                        row = avail_latent_original[ii][0, :]  # TODO: Make more flexible
                        avail_latent[ii] = np.tile(row, ((int(len(train_idx)/J), 1)))
                        test_avail_latent[ii] = np.tile(row, ((int(len(test_idx)/J), 1)))
            # try:
            #     avail = df['av']
            #     test_av = df_test['av']
            # except KeyError:
            #     try:
            #         avail = df['av']
            #         test_av = df_test['AV']
            #     except Exception:
            #         logger.debug("Did not find avail column. Using avail=None.")
            if weights is not None:
                test_weight_var = weights[test_idx]
                weights = weights[train_idx]
            # try:
            #     test_weight_var = df_test['weight']
            #     weights = df['weight']
            # except KeyError:
            #     logger.debug("Did not find weight column. Using weight=None.")

            if choice_id is not None:
                test_choice_id = choice_id[test_idx]
                choice_id = choice_id[train_idx]
            # # assuming choice id is "custom_id"
            # try:
            #     choice_id = df['custom_id']
            #     test_choice_id = df_test['custom_id']
            # except KeyError:
            #     try:
            #         choice_id = df['chid']
            #         test_choice_id = df_test['chid']
            #     except Exception:
            #         logger.debug("Did not find a column for choice id.  .")

            if ind_id is not None:
                test_ind_id = ind_id[test_idx]
                ind_id = ind_id[train_idx]
            # try:
            #     ind_id = df['id']
            #     test_ind_id = df_test['id']
            # except KeyError:
            #     try:
            #         ind_id = df['id']
            #         test_ind_id = df_test['ID']
            #     except Exception:
            #         raise("Did not find a column for id. Include choice column with key 'id'.")
            if alt_var is not None:
                test_alt_var = alt_var[test_idx]
                alt_var = alt_var[train_idx]
            # try:
            #     alt_var = df['alt']
            #     test_alt_var = df_test['alt']
            # except KeyError:
            #     try:
            #         alt_var = df['ALT']
            #         test_alt_var = df_test['ALT']
            #     except Exception:
            #         raise("Did not find a column for choice. Include choice column with key 'alt'.")

            if choice_var is not None:
                test_choice_var = choice_var[test_idx]
                choice_var = choice_var[train_idx]
            # try:
            #     test_choice_var = df_test['choice']
            # except KeyError:
            #     try:
            #         test_choice_var = df_test['CHOICE']
            #     except Exception:
            #         raise("Did not find a column for choice. Include choice column with key 'choice'.")

            # self.test_av = test_av
            # self.test_weight_var = test_weight_var
            # self.test_choice_id = test_choice_id
            # self.test_ind_id = test_ind_id
            # self.test_alt_var = test_alt_var
            # self.test_choice_var = test_choice_var

        # self.df = df
        self.df_test = df_test

        if isvarnames is None:
            isvarnames = []
        self.isvarnames = isvarnames

        if asvarnames is None:
            asvarnames = []
        self.asvarnames = asvarnames

        if trans_asvars is None:
            trans_asvars = []
        self.trans_asvars = trans_asvars
        self.ftol = ftol
        self.gtol = gtol
        self.gtol_membership_func = gtol_membership_func
        self.latent_class = latent_class
        self.num_classes = num_classes
        self.maxiter = maxiter
        self.n_draws = n_draws
        self.multi_objective = multi_objective
        self.p_val = p_val

        self.avail = avail
        self.avail_latent = avail_latent
        self.weights = weights
        self.choice_set = choice_set
        self.choice_var = choice_var
        self.alt_var = alt_var
        self.choice_id = choice_id
        self.ind_id = ind_id

        self.test_av = test_av
        self.test_avail_latent = test_avail_latent
        self.test_weight_var = test_weight_var
        self.test_choice_id = test_choice_id
        self.test_ind_id = test_ind_id
        self.test_alt_var = test_alt_var
        self.test_choice_var = test_choice_var

        self.allow_random = allow_random
        self.allow_bcvars = allow_bcvars

        self.intercept_opts = intercept_opts
        self.base_alt = base_alt

        if chosen_alts_test is None and self.multi_objective:
            try:
                chosen_alts_test = test_alt_var[test_choice_var == 1]
            except Exception as e:
                logger.error("Exception: {}".format(e))
                # make lowercase choice if only uppercase, stop further bugs
                self.df_test['choice'] = self.df_test['CHOICE']
                chosen_alts_test = df_test.query('CHOICE == True')['alt']

        self.obs_freq = None
        if self.multi_objective:
            J = len(np.unique(alt_var))
            obs_freq = np.zeros(J)
            for ii, alt in enumerate(np.unique(alt_var)):
                alt_sum = np.sum(chosen_alts_test == alt)
                obs_freq[ii] = alt_sum
            self.obs_freq = obs_freq/(df_test.shape[0]/len(choice_set))

        # TODO BETTER ORGANISATION OF PRESPEC

        psasvar_ind, psisvar_ind, pspecdist_ind, ps_bcvar_ind, ps_corvar_ind = \
            self._prep_inputs(asvarnames=self.asvarnames, isvarnames=self.isvarnames)

        ps_asvars, ps_isvars, ps_rvars, ps_bcvars, ps_corvars, ps_bctrans, \
            ps_cor, ps_interaction, ps_intercept = \
            self.prespec_features(psasvar_ind, psisvar_ind, pspecdist_ind,
                                  ps_bcvar_ind, ps_corvar_ind, self.isvarnames,
                                  self.asvarnames)
        self.ps_asvars = ps_asvars
        self.ps_isvars = ps_isvars
        self.ps_intercept = ps_intercept
        self.ps_rvars = ps_rvars
        self.ps_corvars = ps_corvars
        self.ps_bctrans = ps_bctrans
        self.ps_cor = ps_cor
        self.ps_bcvars = ps_bcvars
        self.ps_interaction = ps_interaction

        self.all_estimated_solutions = []

    def prespec_features(self, ind_psasvar, ind_psisvar, ind_pspecdist,
                         ind_psbcvar, ind_pscorvar, isvarnames, asvarnames):
        """
        Generates lists of features that are predetermined by the modeller for
        the model development
        Inputs:
        (1) ind_psasvar - indicator list for prespecified asvars
        (2) ind_psisvar - indicator list for prespecified isvars
        (3) ind_pspecdist - indicator list for vars with prespecified coefficient distribution
        (4) ind_psbcvar - indicator list for vars with prespecified transformation
        (5) ind_pscorvar - indicator list for vars with prespecified correlation
        """
        # prespecified alternative-specific variables
        ps_asvar_pos = [i for i, x in enumerate(ind_psasvar) if x == 1]
        ps_asvars = [var for var in asvarnames if asvarnames.index(var) in ps_asvar_pos]

        # prespecified individual-specific variables
        ps_isvar_pos = [i for i, x in enumerate(ind_psisvar) if x == 1]
        ps_isvars = [var for var in isvarnames if isvarnames.index(var) in ps_isvar_pos]

        # prespecified coeff distributions for variables
        ps_rvar_ind = dict(zip(asvarnames, ind_pspecdist))
        ps_rvars = {k: v for k, v in ps_rvar_ind.items() if v != "any"}

        # prespecified non-linear transformed variables
        ps_bcvar_pos = [i for i, x in enumerate(ind_psbcvar) if x == 1]
        ps_bcvars = [var for var in asvarnames if asvarnames.index(var) in ps_bcvar_pos]

        # prespecified correlated variables
        ps_corvar_pos = [i for i, x in enumerate(ind_pscorvar) if x == 1]
        ps_corvars = [var for var in asvarnames if asvarnames.index(var) in ps_corvar_pos]

        ps_bctrans = None
        ps_cor = None
        ps_interaction = None
        ps_intercept = None

        return (ps_asvars, ps_isvars, ps_rvars, ps_bcvars, ps_corvars,
                ps_bctrans, ps_cor, ps_interaction, ps_intercept)

    def avail_features(self):
        """
        Generates lists of features that are available to select from for model development
        Inputs:
        (1) asvars_ps - list of prespecified asvars
        (2) isvars_ps - list of prespecified isvars
        (3) rvars_ps - list of vars and their prespecified coefficient distribution
        (4) bcvars_ps - list of vars that include prespecified transformation
        (5) corvars_ps - list of vars with prespecified correlation
        """
        # available alternative-specific variables for selection
        avail_asvars = [var for var in self.asvarnames if var not in self.ps_asvars]

        # available individual-specific variables for selection
        avail_isvars = [var for var in self.isvarnames if var not in self.ps_isvars]

        # available variables for coeff distribution selection
        avail_rvars = [var for var in self.asvarnames if var not in self.ps_rvars.keys()]

        # available alternative-specific variables for transformation
        avail_bcvars = [var for var in self.asvarnames if var not in self.ps_bcvars]

        # available alternative-specific variables for correlation
        avail_corvars = [var for var in self.asvarnames if var not in self.ps_corvars]

        return (avail_asvars, avail_isvars, avail_rvars, avail_bcvars, avail_corvars)

    def df_coeff_col(self, asvars):
        """
        This function creates dummy dataframe columns for variables,
        which are randomly selected to be estimated with
        alternative-specific coefficients.
        Inputs: asvars - list of variable names to be considered
                choise_set - list of available alternatives
                var_alt - dataframe column consisting of alternative variable
        Output: List of as variables considered for model development
        """
        rand_arr = self.random_state.choice([True, False], len(asvars))
        asvars_new = []
        alt_spec_pos_str = [var for ii, var in enumerate(asvars) if rand_arr[ii]]
        for alt_str in alt_spec_pos_str:
            for choice_str in self.choice_set:
                self.df[alt_str + '_' + choice_str] = self.df[alt_str]*(self.alt_var == choice_str)
                if self.multi_objective:
                    self.df_test[alt_str + '_' + choice_str] = self.df_test[alt_str]*(self.alt_var == choice_str)
                asvars_new.append(alt_str + '_' + choice_str)

        asvars_new.extend([str(integer) for ii, integer in enumerate(asvars)
                           if not rand_arr[ii]])
        return asvars_new

    # Removing redundancy if the same variable is included in the model with and without transformation
    # or with a combination of alt-spec and generic coefficients
    def remove_redundant_asvars(self, asvar_list, transasvars, asvarnames):
        redundant_asvars = [s for s in asvar_list if any(xs in s for xs in transasvars)]
        unique_vars = [var for var in asvar_list if var not in redundant_asvars]

        # When transformations are not applied, the redundancy is created if a variable has both generic & alt-spec co-effs
        if len(transasvars) == 0:
            gen_var_select = [var for var in asvar_list if var in asvarnames]
            alspec_final = [var for var in asvar_list if var not in gen_var_select]
        else:
            gen_var_select = []
            alspec_final = []
            for var in transasvars:
                redun_vars = [item for item in asvar_list if var in item]
                gen_var = [var for var in redun_vars if var in asvarnames]
                if gen_var:
                    gen_var_select.append(self.random_state.choice(gen_var))
                alspec_redun_vars = [item for item in asvar_list
                                     if var in item and item not in asvarnames]
                trans_alspec = [i for i in alspec_redun_vars
                                if any(bc_l for bc_l in boxc_l if bc_l in i)]
                lin_alspec = [var for var in alspec_redun_vars
                              if var not in trans_alspec]
                if self.random_state.randint(2):
                    alspec_final.extend(lin_alspec)
                else:
                    alspec_final.extend(trans_alspec)

        if len(gen_var_select) and len(alspec_final) != 0:
            if self.random_state.randint(2):
                final_asvars = gen_var_select
                final_asvars.extend(unique_vars)
            else:
                final_asvars = alspec_final
                final_asvars.extend(unique_vars)

        elif len(gen_var_select) != 0:
            final_asvars = gen_var_select
            final_asvars.extend(unique_vars)
        else:
            final_asvars = alspec_final
            final_asvars.extend(unique_vars)

        final_asvars = list(dict.fromkeys(final_asvars))

        return final_asvars

    def generate_sol(self):
        """
        Generates list of random model features and then includes modeller prespecifications
        Inputs:
        (2) asvars_avail - list of available asvars for random selection
        (3) isvars_avail - list of available isvars for random selection
        (4) rvars_avail - list of available vars for randomly selected coefficient distribution
        (5) bcvars_avail - list of available vars for random selection of transformation
        (6) corvars_avail - list of available vars for random selection of correlation
        ## Prespecification information
        (1) asvars_ps - list of prespecified asvars
        (2) isvars_ps - list of prespecified isvars
        (3) rvars_ps - list of vars and their prespecified coefficient distribution
        (4) bcvars_ps - list of vars that include prespecified transformation
        (5) corvars_ps - list of vars with prespecified correlation
        (6) bctrans_ps - prespecified transformation boolean
        (7) cor_ps - prespecified correlation boolean
        (8) intercept_ps - prespecified intercept boolean

        """
        ind_availasvar = []
        for i in range(len(self.avail_asvars)):
            ind_availasvar.append(self.random_state.randint(2))
        asvar_select_pos = [i for i, x in enumerate(ind_availasvar) if x == 1]
        asvars_1 = [var for var in self.avail_asvars if self.avail_asvars.index(var)
                    in asvar_select_pos]
        asvars_1.extend(self.ps_asvars)

        asvars_new = self.remove_redundant_asvars(asvars_1, self.trans_asvars,
                                                  self.asvarnames)
        # TODO: Removed
        # asvars = self.df_coeff_col(asvars_new)
        asvars = asvars_new

        ind_availisvar = []
        for i in range(len(self.avail_isvars)):
            ind_availisvar.append(self.random_state.randint(2))
        isvar_select_pos = [i for i, x in enumerate(ind_availisvar) if x == 1]
        isvars = [var for var in self.avail_isvars if self.avail_isvars.index(var) in isvar_select_pos]
        isvars.extend(self.ps_isvars)

        if self.ps_intercept is None:
            asc_ind = self.random_state.rand() < 0.5
        else:
            asc_ind = self.ps_intercept

        asc_var = ['_inter'] if asc_ind else []  # Add intercept to class param
        # all_vars = asvars + isvars + asc_var
        class_vars = asvars + asc_var
        member_vars = ['_inter'] + isvars
        class_params_spec = None
        member_params_spec = None
        if self.latent_class:
            class_params_spec = np.array(np.repeat('tmp', self.num_classes),
                                        dtype='object')

            member_params_spec = np.array(np.repeat('tmp', self.num_classes-1),
                                        dtype='object')

            for i in range(self.num_classes):
                tmp_class_spec = np.array([])
                for var in class_vars:
                    # TODO! ARBITRARY PROB HERE OF ACCEPTANCE... kept high...
                    if self.random_state.uniform() < 0.8:  # prob of accepting asvar
                        tmp_class_spec = np.append(tmp_class_spec, var)
                class_params_spec[i] = tmp_class_spec

            for i in range(self.num_classes-1):
                tmp_member_spec = np.array([])
                for var in member_vars:
                    if self.random_state.uniform() < 0.8:  # 0.5 prob of accepting asvar
                        tmp_member_spec = np.append(tmp_member_spec, var)
                member_params_spec[i] = tmp_member_spec

        r_dist = []
        avail_rvar = [var for var in asvars if var in self.avail_rvars]

        for i in range(len(avail_rvar)):
            r_dist.append(self.random_state.choice(self.dist))

        rvars = dict(zip(avail_rvar, r_dist))
        rvars.update(self.ps_rvars)

        rand_vars = {k: v for k, v in rvars.items() if v != "f" and k in asvars}
        r_dis = [dis for dis in self.dist if dis != "f"]
        for var in self.ps_corvars:
            if var in asvars and var not in rand_vars.keys():
                rand_vars.update({var: self.random_state.choice(r_dis)})

        if self.ps_bctrans is None:
            bctrans = self.random_state.rand() < 0.5
        else:
            bctrans = self.ps_bctrans

        if bctrans:
            ind_availbcvar = []
            for i in range(len(self.avail_bcvars)):
                ind_availbcvar.append(self.random_state.randint(2))
            bcvar_select_pos = [i for i, x in enumerate(ind_availbcvar) if x == 1]
            bcvars = [var for var in self.avail_bcvars if self.avail_bcvars.index(var) in bcvar_select_pos]
            bcvars.extend(self.ps_bcvars)
            bc_vars = [var for var in bcvars if var in asvars and var not in self.ps_corvars]
            # variables with random parameters cannot be estimated with lambda
            # TODO? removed below line... trans random vars?
            # bc_vars = [var for var in bc_vars if var not in rand_vars.keys()]
        else:
            bc_vars = []

        if self.ps_cor is None:
            cor = self.random_state.rand() < 0.5
        else:
            cor = self.ps_cor

        if cor:
            ind_availcorvar = []
            for i in range(len(self.avail_corvars)):
                ind_availcorvar.append(self.random_state.randint(2))
            corvar_select_pos = [i for i, x in enumerate(ind_availcorvar)
                                 if x == 1]
            corvars = [var for var in self.avail_corvars if self.avail_corvars.index(var)
                       in corvar_select_pos]
            corvars.extend(self.ps_corvars)
            cor_vars = [var for var in corvars if var in rand_vars.keys()
                        and var not in bc_vars]
            if len(cor_vars) < 2:
                cor = False
                cor_vars = []
        else:
            cor_vars = []

        sol = Solution(asvars=asvars, isvars=isvars, bcvars=bc_vars,
                       cor_vars=cor_vars, bctrans=bctrans, cor=cor,
                       class_params_spec=class_params_spec,
                       member_params_spec=member_params_spec,
                       asc_ind=asc_ind)
        return sol

    def fit_model(self, sol):
        """Fit model specified in the solution."""
        rand_vars = sol['randvars']

        sig_member = None

        sol_already_generated = self.check_sol_already_generated(sol)
        if sol_already_generated:
            bic, val = 10000000.0, None
            asvars, isvars, randvars, bcvars, corvars = [], [], {}, [], []
            conv, sig, coefs = False, [], []
            return (bic, val, asvars, isvars, randvars, bcvars, corvars,
                    conv, sig, sig_member, coefs)

        if bool(rand_vars):
            if self.latent_class:
                # TODO: better way of including num_classes
                bic, val, asvars, isvars, randvars, bcvars, corvars, \
                    conv, sig, sig_member, coefs = self.fit_lccmm(sol)
            else:
                logger.debug("estimating an MXL model")
                bic, val, asvars, isvars, randvars, bcvars, corvars, \
                    conv, sig, coefs = self.fit_mxl(sol)
        else:
            if self.latent_class:
                try:
                    bic, val, asvars, isvars, randvars, bcvars, corvars, \
                        conv, sig, sig_member, coefs = self.fit_lccm(sol)
                except Exception as e:
                    # TODO? UPDATE
                    logger.debug("Exception during fit_lccm: {}".format(e))
                    return (Solution(), False)
            else:
                logger.debug("estimating an MNL model")
                bic, val, asvars, isvars, randvars, bcvars, corvars, \
                    conv, sig, coefs = self.fit_mnl(sol)  # TODO? ugly

        self.all_estimated_solutions.append(sol)

        return (bic, val, asvars, isvars, randvars, bcvars, corvars, \
                conv, sig, sig_member, coefs)

    def fit_mnl(self, sol):
        """
        Estimates multinomial model for the generated solution
        Inputs:
        (1) dat in csv
        (2) as_vars: list of alternative-specific variables
        (3) is_vars: list of individual-specific variables
        (4) bcvars: list of box-cox variables
        (5) choice: df column with choice variable
        (6) alt: df column with alternative variables
        (7) choice_id: df column with choice situation id
        (8) asc_ind: boolean for fit_intercept
        """
        as_vars = sol['asvars']
        is_vars = sol['isvars']
        asc_ind = sol['asc_ind']
        bcvars = sol['bcvars']
        neg_bcvar = [x for x in bcvars if any(self.df[x].values < 0)]
        bcvars = [x for x in bcvars if x not in neg_bcvar]
        try:
            all_vars = as_vars + is_vars

            X = self.df[all_vars].values
            y = self.choice_var
            seed = self.random_state.randint(2**31 - 1)

            model = MultinomialLogit()
            model.fit(X, y, varnames=all_vars, isvars=is_vars,
                      alts=self.alt_var,
                      ids=self.choice_id, fit_intercept=asc_ind,
                      transformation="boxcox", transvars=bcvars,
                      maxiter=self.maxiter, ftol=self.ftol, gtol=self.gtol,
                      avail=self.avail,
                      weights=self.weights, base_alt=self.base_alt,
                      random_state=seed)

            bic = round(model.bic)
            ll = round(model.loglikelihood)
            def_vals = model.coeff_

            rand_vars = {}
            cor_vars = []
            bc_vars = [var for var in bcvars if var not in self.isvarnames]

            old_stdout = sys.stdout
            log_file = open(self.logger_name, "a")
            sys.stdout = log_file
            model.summary()
            sys.stdout = old_stdout
            log_file.close()

            conv = model.convergence
            pvals = model.pvalues
            coef_names = model.coeff_names

            # TODO? MOOF specific?
            # Validation
            if self.multi_objective:
                X_test = self.df_test[all_vars].values
                y_test = self.test_choice_var
                seed = self.random_state.randint(2**31 - 1)

                # Choice frequecy obtained from estimated model applied on testing sample
                # predicted_probabilities_val = model.pred_prob

                ## Calculating MAE
                model = MultinomialLogit()
                model.fit(X_test, y_test, varnames=all_vars, isvars=is_vars,
                          alts=self.alt_var, ids=self.test_choice_id,
                          fit_intercept=asc_ind,
                          transformation="boxcox", transvars=bcvars,
                          maxiter=0, init_coeff=def_vals, gtol=self.gtol,
                          avail=self.test_av, weights=self.test_weight_var,
                          base_alt=self.base_alt, random_state=seed)

                ### Choice frequecy obtained from estimated model applied on testing sample
                predicted_probabilities_val = model.pred_prob * 100
                obs_freq = model.obs_prob * 100

                MAE = round((1/len(self.choice_set))  * (np.sum(np.abs(predicted_probabilities_val - obs_freq))), 2)
        except Exception as e:
            logger.error("Exception in fit_mnl: {}".format(str(e)))
            bic = 1000000
            MAE = 100.00
            ll = 1000000
            val = 1000000
            as_vars = []
            is_vars = []
            rand_vars = {}
            bc_vars = []
            cor_vars = []
            conv = False
            pvals = []
            coef_names = []

        logger.debug("model BIC: {}".format(bic))
        logger.debug("model LL: {}".format(ll))
        if self.multi_objective:
            logger.debug("MAE: {}".format(MAE))
        logger.debug("model convergence: {}".format(conv))
        logger.debug("dof: {}".format(len(coef_names)))


        if any(coef_name for coef_name in coef_names if coef_name.startswith("lambda.")):
            logger.debug("model type is nonlinear MNL")
        else:
            logger.debug("model type is MNL")

        val = ll
        if self.multi_objective:
            val = MAE

        return (bic, val, as_vars, is_vars, rand_vars, bc_vars, cor_vars,
                conv, pvals, coef_names)

    def fit_mxl(self, sol):
        """
        Estimates the model for the generated solution
        Inputs:
        (1) dat: dataframe in csv
        (2) as_vars: list of alternative-specific variables
        (3) is_vars: list of individual-specific variables
        (4) bcvars: list of box-cox variables
        (5) choice: df column with choice variable
        (6) corvars: list of variables allowed to correlate
        (7) alt: df column with alternative variables
        (8) choice_id: df column with choice situation id
        (9) id_val: df column with individual id
        (10) asc_ind: boolean for fit_intercept
        """
        as_vars = sol['asvars']
        is_vars = sol['isvars']
        asc_ind = sol['asc_ind']
        bcvars = sol['bcvars']
        rand_vars = sol['randvars']
        corvars = sol['cor_vars']
        all_vars = as_vars + is_vars
        X = self.df[all_vars]
        y = self.choice_var
        seed = self.random_state.randint(2**31 - 1)

        bcvars = [var for var in bcvars if var not in self.isvarnames]
        neg_bcvar = [x for x in bcvars if any(self.df[x].values < 0)]
        bcvars = [x for x in bcvars if x not in neg_bcvar]

        try:
            model = MixedLogit()
            model.fit(X, y, varnames=all_vars, alts=self.alt_var, isvars=is_vars,
                    ids=self.choice_id, panels=self.ind_id, randvars=rand_vars,
                    n_draws=self.n_draws, fit_intercept=asc_ind,
                    correlation=corvars,
                    transformation="boxcox", transvars=bcvars,
                    maxiter=self.maxiter, avail=self.avail, ftol=self.ftol,
                    gtol=self.gtol,
                    weights=self.weights, base_alt=self.base_alt,
                    random_state=seed)
            bic = round(model.bic)
            ll = round(model.loglikelihood)
            def_vals = model.coeff_
            old_stdout = sys.stdout
            log_file = open(self.logger_name, "a")
            sys.stdout = log_file
            model.summary()
            conv = model.convergence
            pvals = model.pvalues
            coef_names = model.coeff_names

            logger.debug("model convergence", model.convergence)
            sys.stdout = old_stdout
            log_file.close()

            if self.multi_objective:
                # Validation
                X_test = self.df_test[all_vars].values
                y_test = self.test_choice_var

                # MAE
                model = MixedLogit()
                model.fit(X_test, y_test, varnames=all_vars, alts=self.test_alt_var,
                        isvars=is_vars,
                        ids=self.test_choice_id, panels=self.test_ind_id,
                        randvars=rand_vars, n_draws=self.n_draws,
                        fit_intercept=asc_ind, correlation=corvars,
                        transformation="boxcox",
                        transvars=bcvars, avail=self.test_av, maxiter=0,
                        init_coeff=def_vals, gtol=self.gtol,
                        weights=self.test_weight_var,
                        base_alt=self.base_alt, random_state=seed)

                # Calculating MAE

                # Choice frequecy obtained from estimated model applied on testing sample
                predicted_probabilities_val = model.pred_prob * 100
                obs_freq = model.obs_prob * 100

                # TODO: GPU issues
                MAE = round((1/len(self.choice_set))*(np.sum(abs(predicted_probabilities_val -
                                                        obs_freq))), 2)
        except Exception as e:
            logger.error("Exception in fit_mxl: {}".format(str(e)))
            bic = 1000000
            MAE = 100.00
            ll = 1000000
            val = 1000000
            as_vars = []
            is_vars = []
            rand_vars = {}
            bcvars = []
            corvars = []
            conv = False
            pvals = []
            coef_names = []

        if any(l for l in coef_names if l.startswith("chol.")):
            if any(l for l in coef_names if l.startswith("lambda.")):
                logger.debug("model type is nonlinear correlated MXL")
            else:
                logger.debug("model type is linear correlated MXL")
        elif any(l for l in coef_names if l.startswith("lambda.")):
            logger.debug("model type is nonlinear MXL")
        else:
            logger.debug("model type is MXL")

        logger.debug("model BIC: {}".format(bic))
        logger.debug("model LL: {}".format(ll))
        if self.multi_objective:
            logger.debug("MAE: {}".format(MAE))
        logger.debug("model convergence: {}".format(conv))
        logger.debug("dof: {}".format(len(coef_names)))

        val = ll
        if self.multi_objective:
            val = MAE

        return (bic, val, as_vars, is_vars, rand_vars, bcvars, corvars, conv,
                pvals, coef_names)

    def fit_lccm(self, sol):
        """Estimates multinomial model for the generated solution.
        Inputs:
        (1) dat in csv
        (2) as_vars: list of alternative-specific variables
        (3) is_vars: list of individual-specific variables
        (4) num_classes: number of latent classes
        (5) bcvars: list of box-cox variables
        (6) choice: df column with choice variable
        (7) alt: df column with alternative variables
        (8) choice_id: df column with choice situation id
        (9) asc_ind: boolean for fit_intercept
        """
        asc_ind = sol['asc_ind']
        bcvars = sol['bcvars']

        neg_bcvar = [x for x in bcvars if any(self.df[x].values < 0)]
        bcvars = [x for x in bcvars if x not in neg_bcvar]

        corvars = sol['cor_vars']
        class_params_spec = sol['class_params_spec']
        member_params_spec = sol['member_params_spec']

        logger.debug('bcvars: {}'.format(bcvars))
        logger.debug('class_params_spec: {}'.format(class_params_spec))
        logger.debug('member_params_spec: {}'.format(member_params_spec))
        logger.debug('asc_ind: {}'.format(asc_ind))

        class_vars = list(np.concatenate(class_params_spec))
        member_vars = list(np.concatenate(member_params_spec))
        all_vars = class_vars + member_vars

        transvars = [var for var in bcvars if var in class_vars]
        if transvars != bcvars:
            logger.warning("Model transvar not in class_params_spec")

        # remove _inter
        all_vars = [var_name for var_name in all_vars if var_name != '_inter']
        all_vars = np.unique(all_vars)

        X = self.df[all_vars]
        y = self.choice_var
        seed = self.random_state.randint(2**31 - 1)
        model = LatentClassModel()
        if self.num_classes is None:
            optimal_num, model = \
                model.optimal_class_fit(X,
                                        y,
                                        varnames=all_vars,
                                        alts=self.alt_var,
                                        ids=self.choice_id,
                                        fit_intercept=asc_ind,
                                        transformation="boxcox",
                                        transvars=transvars,
                                        maxiter=self.maxiter,
                                        gtol=self.gtol,
                                        avail=self.avail,
                                        weights=self.weights,
                                        num_classes=self.num_classes,
                                        avail_latent=self.avail_latent,
                                        intercept_opts=self.intercept_opts,
                                        random_state=seed)
        else:
            logger.debug('num_classes: {}'.format(self.num_classes))
            model.fit(X, y, varnames=all_vars,
                      class_params_spec=class_params_spec,
                      member_params_spec=member_params_spec,
                      num_classes=self.num_classes, alts=self.alt_var,
                      ids=self.choice_id, fit_intercept=asc_ind,
                      transformation="boxcox", transvars=transvars,
                      maxiter=self.maxiter, gtol=self.gtol,
                      gtol_membership_func=self.gtol_membership_func,
                      avail=self.avail,
                      avail_latent=self.avail_latent,
                      intercept_opts=self.intercept_opts,
                      weights=self.weights, random_state=seed)
        bic = model.bic

        rand_vars = {}
        cor_vars = []

        old_stdout = sys.stdout
        log_file = open(self.logger_name, "a")
        sys.stdout = log_file
        model.summary()
        conv = model.convergence
        pvals = model.pvalues
        pvals_member = model.pvalues_member
        coef_names = model.coeff_names
        member_names = model.coeff_names_member
        logger.debug("model convergence: {}".format(conv))
        sys.stdout = old_stdout
        log_file.close()

        # Validation
        if self.multi_objective:
            X_test = self.df_test[all_vars].values
            y_test = self.test_choice_var.values
            val = model.loglikelihood - (model.validation_loglik(X_test,
                                                                y_test,
                                                                panels=self.test_ind_id,
                                                                avail=self.avail,
                                                                avail_latent=self.test_avail_latent
                                                                )
                                        / self.val_share)

            logger.debug("val: {}".format(val))

            # Choice frequecy obtained from estimated model applied on testing sample
            predicted_probabilities_val = model.pred_prob

        # TODO? GPU issues
        val = model.loglikelihood
        if self.multi_objective:
            MAE = (1/len(self.choice_set))*(np.sum(abs(predicted_probabilities_val
                                                    - self.obs_freq)))
            val = MAE
            logger.debug("MAE: {}".format(val))
        else:
            logger.debug("Log-likelihood: {}".format(val))

        # default opts for asvars and isvars
        as_vars = []
        is_vars = []
        coef_names = np.concatenate((coef_names, member_names))
        return (bic, val, as_vars, is_vars, rand_vars, transvars, cor_vars,
                conv, pvals, pvals_member, coef_names)

    def fit_lccmm(self, sol):
        as_vars = sol['asvars']
        is_vars = sol['isvars']
        asc_ind = sol['asc_ind']
        bcvars = sol['bcvars']
        rand_vars = sol['randvars']
        corvars = sol['cor_vars']
        class_params_spec = sol['class_params_spec']
        member_params_spec = sol['member_params_spec']

        logger.debug("estimating lccmm")
        logger.debug('as_vars: {}'.format(as_vars))
        logger.debug('is_vars: {}'.format(is_vars))
        logger.debug('rand_vars: {}'.format(rand_vars))
        logger.debug('bcvars: {}'.format(bcvars))
        logger.debug('corvars: {}'.format(corvars))
        logger.debug('asc_ind: {}'.format(asc_ind))

        all_vars = as_vars + is_vars
        X = self.df[all_vars]
        y = self.choice_var
        seed = self.random_state.randint(2**31 - 1)

        bcvars = [var for var in bcvars if var not in self.isvarnames]
        neg_bcvar = [x for x in bcvars if any(self.df[x].values < 0)]
        bcvars = [x for x in bcvars if x not in neg_bcvar]

        model = LatentClassMixedModel()
        if self.num_classes is None:
            optimal_num, model = model.fit(X, y, varnames=all_vars,
                                           alts=self.alt_var, isvars=is_vars,
                                           ids=self.choice_id, panels=self.ind_id,
                                           randvars=rand_vars, n_draws=self.n_draws,
                                           fit_intercept=asc_ind,
                                           correlation=corvars,
                                           transformation="boxcox",
                                           transvars=bcvars,
                                           maxiter=self.maxiter,
                                           avail=self.avail,
                                           gtol=self.gtol,
                                           weights=self.weights,
                                           grad=True,
                                           num_classes=self.num_classes,
                                           random_state=seed)
        else:
            model.fit(X, y, varnames=all_vars, alts=self.alt_var,
                      isvars=is_vars, num_classes=self.num_classes,
                      ids=self.choice_id, panels=self.ind_id,
                      randvars=rand_vars, n_draws=self.n_draws,
                      fit_intercept=asc_ind, correlation=corvars,
                      transformation="boxcox", transvars=bcvars,
                      maxiter=self.maxiter, avail=self.avail,
                      gtol=self.gtol, weights=self.weights,
                      grad=True, random_state=seed)
        bic = model.bic
        def_vals = model.coeff_
        old_stdout = sys.stdout
        log_file = open(self.logger_name, "a")
        sys.stdout = log_file
        model.summary()
        conv = model.convergence
        pvals = model.pvalues
        pvals_member = model.pvalues_member
        coef_names = model.coeff_names

        logger.debug("model convergence: {}".format(model.convergence))
        sys.stdout = old_stdout
        log_file.close()

        if self.multi_objective:
            # Validation
            X_test = self.df_test[all_vars].values
            y_test = self.test_choice_var.values

            val = model.loglikelihood - \
                (model.validation_loglik(X_test,
                                        y_test,
                                        panels=self.test_ind_id)
                / self.val_share)
            logger.debug("val: {}".format(val))

            # TODO: What's going on here?
            model = LatentClassMixedModel()

            model.fit(X_test, y_test, varnames=all_vars, alts=self.df_test['alt'],
                    isvars=is_vars, num_classes=self.num_classes,
                    ids=self.df_test['id'], panels=self.df_test['id'],
                    randvars=rand_vars, n_draws=self.n_draws,
                    fit_intercept=asc_ind, correlation=corvars,
                    transformation="boxcox",
                    transvars=bcvars, avail=self.test_av, maxiter=0,
                    init_coeff=def_vals,  # TODO? weird saving?
                    gtol=self.gtol, weights=self.test_weight_var,
                    grad=True)

            # Calculating MAE

            # Choice frequecy obtained from estimated model applied on testing sample
            predicted_probabilities_val = model.pred_prob

            # TODO: GPU issues
            MAE = (1/len(self.choice_set))*(np.sum(abs(predicted_probabilities_val
                                                    - self.obs_freq)))
            logger.debug("MAE: {}".format(MAE))

        val = model.loglikelihood
        if self.multi_objective:
            val = MAE

        return (bic, MAE, as_vars, is_vars, rand_vars, bcvars, corvars, conv,
                pvals, pvals_member, coef_names)

    def evaluate_objective_function(self, sol):
        """
        (1) Evaluates the objective function (estimates the model and BIC) for
        a given list of variables (estimates the model coefficeints, LL and BIC)
        (2) If the solution generated in (1) contains statistically insignificant variables,
        a new model is generated by removing such variables and the model is re-estimated
        (3) the functions returns estimated solution only if it converges
        Inputs: lists of variable names, individual specific variables,
        variables with random coefficients,
        name of the choice variable in df, list of alternatives, choice_id,
        individual_id(for panel data) and fit intercept bool
        """

        as_vars = sol['asvars']
        is_vars = sol['isvars']
        rand_vars = sol['randvars']
        bc_vars = sol['bcvars']
        cor_vars = sol['cor_vars']
        asc_ind = sol['asc_ind']
        class_params_spec = sol['class_params_spec']
        member_params_spec = sol['member_params_spec']

        all_vars = as_vars + is_vars

        convergence = False

        # default model variables
        sig = None
        sig_member = None
        coefs = []

        if not cor_vars:
            cor_vars = []

        logger.debug('class_params_spec: {}'.format(class_params_spec))
        logger.debug('member_params_spec: {}'.format(member_params_spec))

        # Estimate model if input variables are present in specification
        if all_vars:
            iterations = 200  # iterations for MNL fit...
            features_str =  ' '.join(as_vars) + ' '.join(is_vars)
            logger.debug(("features for round 1: asvars: {}, isvars: {}, "
                         "rand_vars: {}, bc_vars: {}, cor_vars: {}, "
                         "asc_ind: {}, class_params_spec: {}, "
                         "member_params_spec: {}").format(as_vars, is_vars,
                                                          rand_vars, bc_vars,
                                                          cor_vars, asc_ind,
                                                          class_params_spec,
                                                          member_params_spec))

            try:
                bic, val, asvars, isvars, randvars, \
                    bcvars, corvars, convergence, sig, sig_member, coefs = self.fit_model(sol)
                # fix bug when bcvar changed in fit_model
                if bcvars != sol['bcvars']:
                    sol['bcvars'] = bcvars
            except Exception as e:  # TODO: better exception
                logger.warning("Exception fitting model: {}".format(e))
                return (Solution(), False)

            if convergence:
                if not corvars:
                    corvars = []
                logger.debug("solution converged in first round")
                if self.multi_objective:
                    sol.add_objective(bic, MAE=val)
                else:
                    sol.add_objective(bic, loglik=val)

                sig_all = sig
                if self.latent_class:
                    sig_all = np.concatenate((sig, sig_member))
                if all(v for v in sig_all <= self.p_val):
                    logger.debug("solution has all sig-values in first  round")
                    return (sol, convergence)
                else:
                    while any([v for v in sig_all if v > self.p_val]):
                        logger.debug("solution consists insignificant coeffs")
                        # create dictionary of {coefficient_names: p_values}
                        p_vals = dict(zip(coefs, sig_all))

                        r_dist = [dis for dis in self.dist if dis != 'f']  # list of random distributions
                        # create list of variables with insignificant coefficients
                        non_sig = [k for k, v in p_vals.items()
                                   if v > self.p_val]  # list of non-significant coefficient names
                        logger.debug("non-sig coeffs are: {}".format(non_sig))
                        # keep only significant as-variables
                        asvars_round2 = [var for var in asvars if var not in non_sig]  # as-variables with significant p-vals
                        asvars_round2.extend(self.ps_asvars)
                        logger.debug("asvars_round2 for round 2: {}".format(asvars_round2))
                        # replace non-sig alt-spec coefficient with generic coefficient
                        nsig_altspec = []
                        for var in self.asvarnames:
                            ns_alspec = [x for x in non_sig if x.startswith(var)]
                            nsig_altspec.extend(ns_alspec)
                            nsig_altspec_vars = [var for var in nsig_altspec
                                                 if var not in self.asvarnames]
                        logger.debug("nsig_altspec_vars: {}".format(nsig_altspec_vars))

                        rem_asvars = []
                        # Replacing non-significant alternative-specific coeffs with generic coeffs estimation
                        if not self.latent_class:
                            if nsig_altspec_vars:
                                gen_var = []
                                for i in range(len(nsig_altspec_vars)):
                                    gen_var.extend(nsig_altspec_vars[i].split("_"))
                                gen_coeff = [var for var in self.asvarnames if var
                                            in gen_var]
                                if asvars_round2:
                                    redund_vars = [s for s in gen_coeff if any(s
                                                in xs for xs in asvars_round2)]
                                    logger.debug("redund_vars for round 2: {}".format(redund_vars))
                                    asvars_round2.extend([var for var in gen_coeff
                                                        if var not in redund_vars])
                                    # rem_asvars = remove_redundant_asvars(asvars_round2,trans_asvars)
                                    logger.debug("asvars_round2 before removing redundancy: {}".format(asvars_round2))
                                    # rem_asvars = remove_redundant_asvars(asvars_round2,trans_asvars)
                                    # checking if remove_redundant_asvars is needed or not
                                    rem_asvars = sorted(list(set(asvars_round2)))
                                else:
                                    rem_asvars = gen_coeff
                            else:
                                rem_asvars = sorted(list(set(asvars_round2)))
                            logger.debug("rem_asvars = {}".format(rem_asvars))

                        rem_class_params_spec = copy.deepcopy(class_params_spec)
                        rem_member_params_spec = copy.deepcopy(member_params_spec)

                        if self.latent_class:
                            i = 0
                            for ii, class_params in enumerate(class_params_spec):
                                tmp_class_params = class_params.copy()
                                delete_idx = []
                                for jj, _ in enumerate(class_params):
                                    if sig[i] > 0.05:
                                        delete_idx.append(jj)
                                    i += 1
                                tmp_class_params = np.delete(tmp_class_params, delete_idx)
                                rem_class_params_spec[ii] = tmp_class_params

                        if self.latent_class:
                            i = 0
                            # rem_member_params_spec = member_params_spec.copy()
                            for ii, member_params in enumerate(member_params_spec):
                                tmp_member_params = member_params.copy()
                                delete_idx = []
                                for jj, _ in enumerate(member_params):
                                    if sig_member[i] > 0.05:
                                        delete_idx.append(jj)
                                    i += 1
                                tmp_member_params = np.delete(tmp_member_params, delete_idx)
                                rem_member_params_spec[ii] = tmp_member_params

                        # remove insignificant is-variables
                        ns_isvars = []
                        for isvar in self.isvarnames:
                            ns_isvar = [x for x in non_sig if
                                        x.startswith(isvar)]
                            ns_isvars.extend(ns_isvar)
                        remove_isvars = []
                        for i in range(len(ns_isvars)):
                            remove_isvars.extend(ns_isvars[i].split("."))

                        remove_isvar = [var for var in remove_isvars if var
                                        in isvars]
                        most_nsisvar = {x: remove_isvar.count(x) for x
                                        in remove_isvar}
                        rem_isvar = [k for k, v in most_nsisvar.items()
                                     if v == (len(self.choice_set)-1)]
                        isvars_round2 = [var for var in is_vars if var
                                         not in rem_isvar]  # individual specific variables with significant p-vals
                        isvars_round2.extend(self.ps_isvars)

                        rem_isvars = sorted(list(set(isvars_round2)))

                        # remove intercept if not significant and not prespecified
                        ns_intercept = [x for x in non_sig if
                                        '_intercept.' in x]  # non-significant intercepts

                        new_asc_ind = asc_ind

                        if self.ps_intercept is None:
                            if len(ns_intercept) == len(self.choice_set)-1:
                                new_asc_ind = False
                        else:
                            new_asc_ind = self.ps_intercept

                        # bug fix when old class params in while loop
                        class_params_spec = copy.deepcopy(rem_class_params_spec)
                        member_params_spec = copy.deepcopy(rem_member_params_spec)

                        # remove insignificant random coefficients
                        ns_sd = [x for x in non_sig if x.startswith('sd.')]  # non-significant standard deviations
                        ns_sdval = [str(i).replace('sd.', '') for i in ns_sd]  # non-significant random variables

                        # non-significant random variables that are not pre-included
                        remove_rdist = [x for x in ns_sdval if x not in
                                        self.ps_rvars.keys() or x not in rem_asvars]
                        # random coefficients for significant variables
                        rem_rand_vars = {k: v for k, v in randvars.items()
                                         if k in rem_asvars and k not in
                                         remove_rdist}
                        rem_rand_vars.update({k: v for k, v in self.ps_rvars.items()
                                              if k in rem_asvars and v != 'f'})
                        logger.debug("rem_rand_vars = {}".format(rem_rand_vars))
                        # including ps_corvars in the model if they are included in rem_asvars
                        for var in self.ps_corvars:
                            if var in rem_asvars and var not in rem_rand_vars.keys():
                                rem_rand_vars.update({var: self.random_state.choice(r_dist)})

                        # remove transformation if not significant and non prespecified
                        ns_lambda = [x for x in non_sig if x.startswith('lambda.')]  # insignificant transformation coefficient
                        ns_bctransvar = [str(i).replace('lambda.', '')
                                         for i in ns_lambda]  # non-significant transformed var
                        rem_bcvars = [var for var in bcvars if var in
                                      rem_asvars and var not in ns_bctransvar
                                      and var not in self.ps_corvars]

                        # remove insignificant correlation
                        ns_chol = [x for x in non_sig if x.startswith('chol.')]  # insignificant cholesky factor
                        ns_cors = [str(i).replace('chol.', '') for i in ns_chol]  # insignicant correlated variables
                        # create a list of variables whose correlation coefficient is insignificant
                        if ns_cors:
                            ns_corvar = []
                            for i in range(len(ns_cors)):
                                ns_corvar.extend(ns_cors[i].split("."))
                            most_nscorvars = {x: ns_corvar.count(x)
                                              for x in ns_corvar}
                            logger.debug('most_nscorvars: {}'.format(most_nscorvars))
                            # check frequnecy of variable names in non-significant coefficients
                            nscorvars = [k for k, v in most_nscorvars.items()
                                         if v >= int(len(corvars)*0.75)]
                            logger.debug('nscorvars: {}'.format(nscorvars))
                            nonps_nscorvars = [var for var in nscorvars
                                               if var not in self.ps_corvars]
                            # if any variable has insignificant correlation
                            # with all other variables, their correlation is
                            # removed from the solution
                            if nonps_nscorvars:
                                # list of variables allowed to correlate
                                rem_corvars = [var for var in
                                               rem_rand_vars.keys() if var
                                               not in nonps_nscorvars and
                                               var not in rem_bcvars]
                            else:
                                rem_corvars = [var for var in
                                               rem_rand_vars.keys() if var
                                               not in rem_bcvars]

                            # need atleast two variables in the list to
                            # estimate correlation coefficients
                            if len(rem_corvars) < 2:
                                rem_corvars = []
                        else:
                            rem_corvars = [var for var in corvars if var in
                                           rem_rand_vars.keys() and var not in
                                           rem_bcvars]
                            if len(rem_corvars) < 2:
                                rem_corvars = []

                        # Evaluate objective function with significant feautures from round 1

                        rem_alvars = rem_asvars + rem_isvars
                        if rem_alvars:
                            if (set(rem_alvars) != set(all_vars) or
                                set(rem_rand_vars) != set(rand_vars) or
                                set(rem_bcvars) != set(bcvars) or
                                set(rem_corvars) != set(corvars) or
                                    new_asc_ind != asc_ind):
                                logger.debug("not same as round 1 model")
                            else:
                                logger.debug("model 2 same as round 1 model")
                                return (sol, convergence)

                            sol = Solution(asvars=rem_asvars,
                                           isvars=rem_isvars,
                                           randvars=rem_rand_vars,
                                           bcvars=rem_bcvars,
                                           cor_vars=rem_corvars,
                                           asc_ind=new_asc_ind,
                                           class_params_spec=rem_class_params_spec,
                                           member_params_spec=rem_member_params_spec
                                           )
                            try:
                                bic, val, asvars, isvars, randvars, \
                                    bcvars, corvars, convergence, sig, sig_member, coefs = self.fit_model(sol)
                            except Exception as e:  # TODO: better exception
                                logger.warning("Exception fitting model: {}".format(e))
                                return (Solution(), False)

                            if convergence:
                                if self.multi_objective:
                                    sol.add_objective(bic, MAE=val)
                                else:
                                    sol.add_objective(bic, loglik=val)

                                if all([v for v in sig if v <= self.p_val]):
                                    break

                                # if only some correlation coefficients or
                                # intercept values are insignificant, we accept
                                # the solution
                                p_vals = dict(zip(coefs, sig))
                                non_sig = [k for k, v in p_vals.items()
                                           if v > self.p_val]
                                logger.debug("non_sig in round 2: {}".format(non_sig))

                                sol['asvars'] = [var for var in sol['asvars'] if var not in
                                          non_sig or var in self.ps_asvars]  # keep only significant vars

                                # Update other features of solution based on sol[1]
                                sol['randvars'] = {k: v for k, v in sol['randvars'].items() if k in sol['asvars']}
                                sol['bcvars'] = [var for var in sol['bcvars'] if var in sol['asvars'] and var not in self.ps_corvars]
                                if sol['cor_vars']:
                                    sol['cor_vars'] = [var for var in sol['cor_vars'] if var in sol['randvars'].keys and var not in sol['bcvars']]

                                # fit_intercept = False if all intercepts are insignificant
                                if len([var for var in non_sig if var in
                                       ['_intercept.' + var for var
                                        in self.choice_set]]) == len(non_sig):
                                    if len(non_sig) == len(self.choice_set)-1:
                                        sol['asc_ind'] = False  # TODO? confirm
                                        return (sol, convergence)

                                all_ns_int = [x for x in non_sig if x.startswith('_intercept.')]
                                all_ns_cors = [x for x in non_sig if x.startswith('chol.')]

                                all_ns_isvars = []
                                for isvar in self.isvarnames:
                                    ns_isvar = [x for x in non_sig if x.startswith(isvar)]
                                    all_ns_isvars.extend(ns_isvar)

                                irrem_nsvars = all_ns_isvars + all_ns_int + all_ns_cors
                                if all(nsv in irrem_nsvars for nsv in non_sig):
                                    logger.debug("non-significant terms cannot be further eliminated")
                                    return (sol, convergence)

                                if (non_sig == all_ns_cors or
                                    non_sig == all_ns_int or
                                    non_sig == list(set().union(all_ns_cors,
                                                                all_ns_int))):
                                    logger.debug("only correlation coefficients or intercepts are insignificant")
                                    return (sol, convergence)

                                if all([var in self.ps_asvars or var in self.ps_isvars or
                                        var in self.ps_rvars.keys() for var in non_sig]):
                                    logger.debug("non-significant terms are pre-specified")
                                    return (sol, convergence)

                                if (len([var for var in non_sig if var in
                                        ['sd.' + var for var
                                         in self.ps_rvars.keys()]]) == len(non_sig)):
                                    logger.debug("non-significant terms are pre-specified random coefficients")
                                    return (sol, convergence)

                            else:
                                logger.debug("convergence not reached in round 2 so final sol is from round 1")
                                return (sol, convergence)
                        else:
                            logger.debug("no vars for round 2")
                            return (sol, convergence)
            else:
                convergence = False
                logger.debug("convergence not reached in round 1")
                return (sol, convergence)
        else:
            logger.debug("no vars when function called first time")
        return (sol, convergence)

    def check_sol_already_generated(self, sol):
        new_har_mem = []

        for sol_i in self.all_estimated_solutions:
            tmp_sol_i = sol_i.copy()
            tmp_sol_i.pop('sol_num', None)
            tmp_sol_i.pop('bic', None)
            tmp_sol_i.pop('MAE', None)
            tmp_sol_i.pop('loglik', None)
            if self.latent_class:
                tmp_sol_i.pop('asvars', None)
                tmp_sol_i.pop('isvars', None)

            new_har_mem.append(tmp_sol_i)

        sol_i = sol.copy()
        sol_i.pop('sol_num', None)
        sol_i.pop('bic', None)
        sol_i.pop('MAE', None)
        sol_i.pop('loglik', None)
        if self.latent_class:
            sol_i.pop('asvars', None)
            sol_i.pop('isvars', None)

        for har_mem_sol in new_har_mem:
            bool_arr = []
            for sol_k, sol_v in sol_i.items():
                if np.all(har_mem_sol[sol_k] == sol_v):
                    bool_arr.append(True)
                else:
                    bool_arr.append(False)
            if np.all(bool_arr):
                logger.debug("Sol already generated. Skipping estimation.")
                return True

        return False

    # Initialize harmony memory and opposite harmony memory of size HMS with random slutions
    def initialize_memory(self, HMS):
        """
        Creates two lists (called the harmony memory and opposite harmony memory)
        harmony memory - containing the initial randomly generated solutions
        opposite harmony memory - containing random solutions that include variables not included in harmony memory
        Inputs: harmony memory size (int), all variable names, individual-specific variable, prespecifications provided by user
        """
        HM = []
        opp_HM = []
        base_model = Solution() # TODO?

        HM.append(base_model)

        # Add an MXL with full covriance structure

        # Create initial harmony memory
        unique_HM = []
        dummy_iter = 0  # prevent stuck in while loop
        while dummy_iter < 30000:
            dummy_iter += 1
            logger.info("Initializing harmony at iteration {}".format(dummy_iter))
            sol = self.generate_sol()
            all_HM = HM + opp_HM
            sol, conv = self.evaluate_objective_function(sol)

            if conv:
                HM.append(sol)
                # keep only unique solutions in memory
                used = set()
                unique_HM = [used.add(x['bic']) or x for x in HM
                             if x['bic'] not in used]
                unique_HM = sorted(unique_HM, key=lambda x: x['bic'])
                logger.debug("harmony memory for iteration: {}, is: {}".format(dummy_iter, str(unique_HM)))

            logger.debug("estimating opposite harmony memory")

            # TODO! NOT DONE PROPERLY? 
            # create opposite harmony memory with variables that were not included in the harmony memory's solution

            opp_sol = self.generate_sol()

            all_HM = HM + opp_HM
            opp_sol, opp_conv = self.evaluate_objective_function(opp_sol)

            unique_opp_HM = []
            if opp_conv:
                opp_HM.append(opp_sol)
                opp_used = set()
                unique_opp_HM = [opp_used.add(x['bic']) or x for x in opp_HM
                                 if x['bic'] not in opp_used]
                unique_opp_HM = sorted(unique_opp_HM, key=lambda x: x['bic'])
                logger.debug("unique_opp_HM is for iteration: {} is: {}".format(dummy_iter, str(unique_opp_HM)))

                if len(unique_opp_HM) == HMS:
                        break

            # Final Initial Harmony
            Init_HM = unique_HM + unique_opp_HM

            unique = set()
            unique_Init_HM = [unique.add(x['bic']) or x for x in Init_HM
                              if x['bic'] not in unique]

            if len(unique_Init_HM) >= HMS:
                unique_Init_HM = unique_Init_HM[:HMS]
                return unique_Init_HM

        return unique_Init_HM

    def harmony_consideration(self, har_mem, HMCR_itr, itr, HM):
        """
        If a generated random number is less than or equal to the harmony memory consideration rate (HMCR)
        then 90% of a solution already in memory will be randomly selected to build the new solution.
        Else a completely new random solution is generated
        Inputs: harmony memory, HMCR for the current interation, iteration number
        """
        new_sol = Solution()

        Fronts = None
        Pareto = None
        if self.multi_objective:
            har_mem = self.non_dominant_sorting(har_mem)
            Fronts = self.get_fronts(har_mem)
            Pareto = self.pareto(Fronts, har_mem)

        if self.random_state.choice([0, 1], p=[1-HMCR_itr, HMCR_itr]) <= HMCR_itr:
            logger.debug("harmony consideration")
            m_pos = self.random_state.choice(len(har_mem))  # randomly choose the position of any one solution in harmony memory
            select_new_asvars_index = self.random_state.choice([0, 1],
                                                       size=len(har_mem[m_pos]['asvars']),
                                                       p=[1-HMCR_itr, HMCR_itr])
            select_new_asvars = [i for (i, v) in zip(har_mem[m_pos]['asvars'],
                                                     select_new_asvars_index)
                                                     if v]
            select_new_asvars = list(self.random_state.choice(har_mem[m_pos]['asvars'],
                                                      int((len(har_mem[m_pos]['asvars']))*HMCR_itr),
                                                      replace=False))  # randomly select 90% of the variables from solution at position m_pos in harmony memory
            n_asvars = sorted(list(set().union(select_new_asvars, self.ps_asvars)))
            new_asvars = self.remove_redundant_asvars(n_asvars, self.trans_asvars,
                                                      self.asvarnames)
            new_sol['asvars'] = new_asvars
            logger.debug("new_asvars: {}".format(new_asvars))

            select_new_isvars_index = self.random_state.choice([0, 1],
                                                       size=len(har_mem[m_pos]['isvars']),
                                                       p=[1-HMCR_itr, HMCR_itr])
            select_new_isvars = [i for (i, v) in zip(har_mem[m_pos]['isvars'], select_new_isvars_index) if v]

            new_isvars = sorted(list(set().union(select_new_isvars, self.ps_isvars)))
            logger.debug("new_isvars: {}".format(new_isvars))
            new_sol['isvars'] = new_isvars

            # include distributions for the variables in new solution based on the solution at m_pos in memory
            # TODO: RYAN ADD - SAFEGUARD
            r_pos = {}
            if self.multi_objective:  # TODO: CHECK BEHAVIOUR FOR SOOF
                if m_pos < len(Pareto):
                    r_pos = {k: v for k, v in har_mem[m_pos]['randvars'].items() if k
                            in new_asvars}
                    logger.debug("r_pos: {}".format(r_pos))
                    new_sol['randvars'] = r_pos

            new_bcvars = [var for var in har_mem[m_pos]['bcvars'] if var in new_asvars
                          and var not in self.ps_corvars]
            new_sol['bcvars'] = new_bcvars

            new_corvars = har_mem[m_pos]['cor_vars']
            if new_corvars:
                new_corvars = [var for var in har_mem[m_pos]['cor_vars'] if var
                            in r_pos.keys() and var not in new_bcvars]
            new_sol['cor_vars'] = new_corvars

            # Take fit_intercept from m_pos solution in memory
            intercept = har_mem[m_pos]['asc_ind']
            new_sol['asc_ind'] = intercept

            class_params_spec = har_mem[m_pos]['class_params_spec']
            new_sol['class_params_spec'] = class_params_spec
            member_params_spec = har_mem[m_pos]['member_params_spec']
            new_sol['member_params_spec'] = member_params_spec

            logger.debug("new sol after HMC-1: {}".format(str(new_sol)))
        else:
            logger.debug("harmony not considered")
            # if harmony memory consideration is not conducted, then a new solution is generated

            new_sol = self.generate_sol()
            logger.debug("new sol after HMC-2: {}".format(new_sol))
        return new_sol

    def add_new_asfeature(self, solution):
        """
        Randomly selects an as variable, which is not already in solution
        Inputs: solution list containing all features generated from harmony consideration
        # TODO: Include alternative-specific coefficients
        """
        new_asvar = [var for var in self.asvarnames if var not in solution['asvars']]
        logger.debug('new_asvar: {}'.format(new_asvar))
        if new_asvar:
            n_asvar = list(self.random_state.choice(new_asvar, 1))
            solution['asvars'].extend(n_asvar)
            solution['asvars'] = self.remove_redundant_asvars(solution['asvars'],
                                                       self.trans_asvars,
                                                       self.asvarnames)
            solution['asvars'] = sorted(list(set(solution['asvars'])))
            logger.debug("new sol: {}".format(str(solution['asvars'])))

            r_vars = {}
            if self.allow_random:
                for i in solution['asvars']:
                    if i in solution['randvars'].keys():
                        r_vars.update({k: v for k, v in solution['randvars'].items()
                                    if k == i})
                        logger.debug("r_vars: {}".format(r_vars))
                    else:
                        if i in self.ps_rvars.keys():
                            r_vars.update({i: self.ps_rvars[i]})
                            logger.debug("r_vars: {}".format(r_vars))
                        else:
                            # TODO! RYAN - REMOVED
                            if len(self.dist) > 0:  # TODO: RYAN ADD
                                r_vars.update({i: self.random_state.choice(self.dist)})
                            logger.debug("r_vars: {}".format(r_vars))
                solution['randvars'] = {k: v for k, v in r_vars.items() if k
                            in solution['asvars'] and v != 'f'}

        if solution['cor_vars']:
            solution['cor_vars'] = [var for var in solution['cor_vars'] if var in solution['randvars'].keys()
                        and var not in solution['bcvars']]
            # TODO: is this the right solution indices? does it switch up throughout?
        if self.ps_intercept is None:
            solution['asc_ind'] = bool(self.random_state.randint(2))
        logger.debug('solution: {}'.format(solution))

        return solution

    def add_new_isfeature(self, solution):
        """
        Randomly selects an is variable, which is not already in solution
        Inputs: solution list containing all features generated from harmony consideration
        """
        if solution['isvars']:
            new_isvar = [var for var in self.isvarnames if var
                         not in solution['isvars']]
            if new_isvar:
                n_isvar = list(self.random_state.choice(new_isvar, 1))
                solution['isvars'] = sorted(list(set(solution['isvars']).union(n_isvar)))
        return solution

    def add_new_bcfeature(self, solution, PAR_itr):
        """
        Randomly selects a variable to be transformed, which is not already in solution
        Inputs: solution list containing all features generated from harmony consideration
        """
        if self.ps_bctrans is None:
            bctrans = bool(self.random_state.randint(2, size=1))
        else:
            bctrans = self.ps_bctrans

        if bctrans and self.allow_bcvars:
            select_new_bcvars_index = self.random_state.choice([0, 1],
                                                       size=len(solution['asvars']),
                                                       p=[1-PAR_itr, PAR_itr])
            new_bcvar = [i for (i, v) in zip(solution['asvars'],
                                             select_new_bcvars_index) if v]
            solution['bcvars'] = sorted(list(set(solution['bcvars']).union(new_bcvar)))
            solution['bcvars'] = [var for var in solution['bcvars'] if var
                                  not in self.ps_corvars]
            class_params = []
            if solution['class_params_spec'] is not None:
                class_params = list(np.concatenate(solution['class_params_spec']))

                solution['bcvars'] = [var for var in solution['bcvars']
                                      if var in class_params]

        else:
            solution['bcvars'] = []

        # TODO? Stop bug
        if not solution['cor_vars']:
            solution['cor_vars'] = []
        if self.allow_bcvars:
            # Remove corvars that are now included in bcvars
            solution['cor_vars'] = [var for var in solution['cor_vars'] if var not in solution['bcvars']]
        return solution

    def add_new_corfeature(self, solution):
        """
        Randomly selects variables to be correlated, which is not already in solution
        Inputs: solution list containing all features generated from harmony consideration
        """
        if self.ps_cor is None:
            cor = bool(self.random_state.randint(2, size=1))
        else:
            cor = self.ps_cor
        if cor:
            new_corvar = [var for var in solution['randvars'].keys() if var
                          not in solution['bcvars']]
            solution['cor_vars'] = sorted(list(set(solution['cor_vars']).union(new_corvar)))
        else:
            solution['cor_vars'] = []
        if len(solution['cor_vars']) < 2:
            solution['cor_vars'] = []
        solution['bcvars'] = [var for var in solution['bcvars'] if var not in solution['cor_vars']]
        return solution

    def add_new_class_paramfeature(self, solution):
        """
        Randomly selects variables to be added to class_params_spec, which is not already in solution
        Inputs: solution list containing all features generated from harmony consideration
        """
        class_params_spec = solution['class_params_spec']
        class_params_spec_new = copy.deepcopy(class_params_spec)
        all_vars = self.asvarnames  # + self.isvarnames # TODO? check up on -> inc. intercept?
        ii = self.random_state.randint(0, len(class_params_spec))
        class_i = class_params_spec[ii]

        new_params = [var for var in all_vars if var not in class_i]
        if len(new_params) > 0:
            new_param = np.array([])
            class_params_spec = class_i

            if len(new_params) > 0:
                new_param = self.random_state.choice(new_params, 1)

                new_class_spec = np.sort(np.append(class_i, new_param))
            # TODO! Consider randvars
            class_params_spec_new[ii] = new_class_spec
        else:
            class_params_spec_new[ii] = class_i

        solution['class_params_spec'] = class_params_spec_new
        return solution

    def add_new_member_paramfeature(self, solution):
        """
        Randomly selects variables to be added to member_params_spec, which is not already in solution
        Inputs: solution list containing all features generated from harmony consideration
        """
        member_params_spec = solution['member_params_spec']
        member_params_spec_new = copy.deepcopy(member_params_spec)
        all_vars = self.isvarnames + ['_inter']
        # for ii, class_i in enumerate(member_params_spec):
        ii = self.random_state.randint(0, len(member_params_spec))
        member_i = member_params_spec_new[ii]

        if len(member_i) > 0:
            new_params = np.array([var for var in all_vars if var not in member_i])
            new_param = np.array([])
            new_member_spec = member_i
            # TODO? remove redundant asvars ?
            if len(new_params) > 0:
                new_param = self.random_state.choice(new_params, 1)
                # TODO? remove redundant asvars ?
                new_member_spec = np.sort(np.append(member_i, new_param))
            # TODO! consider randvars
            member_params_spec_new[ii] = new_member_spec
        else:
            member_params_spec_new[ii] = member_i

        solution['member_params_spec'] = member_params_spec_new

        return solution

    def remove_asfeature(self, solution):
        """
        Randomly excludes an as variable from solution generated from harmony consideration
        Inputs: solution list containing all features
        """
        if solution['asvars']:
            rem_asvar = list(self.random_state.choice(solution['asvars'], 1))
            solution['asvars'] = [var for var in solution['asvars'] if var not in rem_asvar]
            solution['asvars'] = sorted(list(set(solution['asvars']).union(self.ps_asvars)))
            solution['randvars'] = {k: v for k, v in solution['randvars'].items() if k
                                    in solution['asvars']}
            solution['bcvars'] = [var for var in solution['bcvars'] if var in solution['asvars']
                           and var not in self.ps_corvars]
            solution['cor_vars'] = [var for var in solution['cor_vars'] if var in solution['asvars']
                           and var not in self.ps_bcvars]
        return solution

    def remove_isfeature(self, solution):
        """
        Randomly excludes an is variable from solution generated from harmony consideration
        Inputs: solution list containing all features
        """
        if solution['isvars']:
            rem_isvar = list(self.random_state.choice(solution['isvars'], 1))
            solution['isvars'] = [var for var in solution['isvars'] if var not in rem_isvar]
            solution['isvars'] = sorted(list(set(solution['isvars']).union(self.ps_isvars)))
        return solution

    def remove_bcfeature(self, solution):
        """
        Randomly excludes a variable transformation from solution generated from harmony consideration
        Inputs: solution list containing all features
        """
        if solution['bcvars']:
            rem_bcvar = list(self.random_state.choice(solution['bcvars'], 1))
            rem_nps_bcvar = [var for var in rem_bcvar if var
                             not in self.ps_bcvars]
            solution['bcvars'] = [var for var in solution['bcvars'] if var in solution['asvars']
                                 and var not in rem_nps_bcvar]
            solution['cor_vars'] = [var for var in solution['cor_vars'] if var not in solution['bcvars']]
            solution['bcvars'] = [var for var in solution['bcvars'] if var not in solution['cor_vars']]
        return solution

    def remove_corfeature(self, solution):
        """
        Randomly excludes correlaion feature from solution generated from harmony consideration
        Inputs: solution list containing all features
        """
        if solution['cor_vars']:
            rem_corvar = list(self.random_state.choice(solution['cor_vars'], 1))
            rem_nps_corvar = [var for var in rem_corvar if var
                              not in self.ps_corvars]
            solution['cor_vars'] = [var for var in solution['cor_vars'] if var
                                   in solution['randvars'].keys()
                                   and var not in rem_nps_corvar]
            if len(solution['cor_vars']) < 2:
                solution['cor_vars'] = []
        return solution

    def remove_class_paramfeature(self, solution):
        """
        Randomly excludes class_param_spec feature from solution generated from harmony consideration.
        Inputs: solution list containing all features
        """
        class_params_spec = copy.deepcopy(solution['class_params_spec'])
        if solution['class_params_spec'] is not None:
            # Select class to remove var from
            logger.debug("DEBUG class_params_spec - {}".format(str(class_params_spec)))
            ii = self.random_state.randint(0, len(class_params_spec))
            logger.debug("DEBUG ii - {}".format(str(ii)))
            class_i = class_params_spec[ii]
            logger.debug("DEBUG class_i- {}".format(str(class_i)))
            if len(class_i) > 0:
                rem_asvar = list(self.random_state.choice(class_i, 1))
                logger.debug("DEBUG rem_asvar- {}".format(str(rem_asvar)))
                tmp_class_i = [var for var in class_i if not rem_asvar]
                logger.debug("DEBUG tmp_class_i-  {}".format(str(tmp_class_i)))
                class_params_spec[ii] = np.array(tmp_class_i)

        solution['class_params_spec'] = class_params_spec
        return solution

    def remove_member_paramfeature(self, solution):
        """
        Randomly excludes class_param_spec feature from solution generated from harmony consideration.
        Inputs: solution list containing all features
        """
        member_params_spec = copy.deepcopy(solution['member_params_spec'])
        if solution['member_params_spec'] is not None:
            ii = self.random_state.randint(0, len(member_params_spec))
            member_i = member_params_spec[ii]
            if len(member_i) > 0:
                rem_member_param = list(self.random_state.choice(member_i, 1))
                tmp_member_i = [var for var in member_i if not rem_member_param]
                member_params_spec[ii] = np.array(tmp_member_i)
        solution['member_params_spec'] = member_params_spec

        return solution

    def assess_sol(self, solution, har_mem):
        """
        (1) Evaluates the objective function of a given solution
        (2) Evaluates if the solution provides an improvement in BIC by atleast a threshold value compared to any other solution in memory
        (3) Checks if the solution is unique to other solutions in memory
        (4) Replaces the worst solution in memory, if (2) and (3) are true
        Inputs: solution list containing all features, harmony memory
        """
        data = self.df.copy()

        # Stop bug where _inter in class params but intercept is false
        asc_ind = solution['asc_ind']

        improved_sol, conv = self.evaluate_objective_function(solution)

        if conv:
            har_mem.append(improved_sol)

        seen = set()
        seen_add = seen.add
        val_key = 'MAE' if self.multi_objective else 'loglik'

        new_hm = [x for x in har_mem if tuple([x['bic'], x[val_key]]) not in seen and
                  not seen_add(tuple([x['bic'], x[val_key]]))]

        new_har_mem = new_hm
        if self.multi_objective:
            fronts = self.get_fronts(new_hm)
            new_har_mem = self.non_dominant_sorting(new_hm)

        logger.debug("new_har_mem: {}".format(str(new_har_mem)))
        return (new_har_mem, improved_sol)

    def pitch_adjustment(self, sol, har_mem, PAR_itr, itr, HMS):
        """
        (1) A random binary indicator is generated. If the number is 1,
            then a new feature is added to the solution
            generated in the Harmony Memory consideration step.
            Else a feature is randomly excluded from the solution
        (2) The objective function of a given solution is evaluated.
        (3) The worst solution in harmony memory is repalced with the solution,
            if it is unique and provides an improved BIC

        Inputs:
        solution list generated from harmony consideration step
        harmony memory
        Pitch adjustment rate for the given iteration
        """
        improved_harmony = har_mem
        if self.random_state.choice([0, 1], p=[1-PAR_itr, PAR_itr]) <= PAR_itr:
            if self.random_state.randint(2):
                logger.debug("pitch adjustment adding as variables")
                pa_sol = self.add_new_asfeature(sol)
                improved_harmony, current_sol = self.assess_sol(pa_sol,
                                                                har_mem)

                if self.isvarnames:
                    logger.debug("pitch adjustment adding is variables")
                    pa_sol = self.add_new_isfeature(pa_sol)
                    improved_harmony, current_sol = self.assess_sol(pa_sol,
                                                                    har_mem)

                if self.ps_bctrans is None or self.ps_bctrans:
                    logger.debug("pitch adjustment adding bc variables")
                    pa_sol = self.add_new_bcfeature(pa_sol, PAR_itr)
                    improved_harmony, current_sol = self.assess_sol(pa_sol,
                                                                    har_mem)

                if self.ps_cor is None or self.ps_cor:
                    logger.debug("pitch adjustment adding cor variables")
                    pa_sol = self.add_new_corfeature(pa_sol)
                    improved_harmony, current_sol = self.assess_sol(pa_sol,
                                                                    har_mem)

                if pa_sol['class_params_spec'] is not None:
                    logger.debug("pitch adjustment adding class param variables")
                    pa_sol = self.add_new_class_paramfeature(pa_sol)
                    improved_harmony, current_sol = self.assess_sol(pa_sol,
                                                                    har_mem)

                if pa_sol['member_params_spec'] is not None:
                    logger.debug("pitch adjustment adding member param variables")
                    pa_sol = self.add_new_member_paramfeature(pa_sol)
                    improved_harmony, current_sol = self.assess_sol(pa_sol,
                                                                    har_mem)

            elif len(sol['asvars']) > 1:
                logger.debug("pitch adjustment by removing as variables")
                pa_sol = self.remove_asfeature(sol)
                improved_harmony, current_sol = self.assess_sol(pa_sol,
                                                                har_mem)

                if self.isvarnames or sol['isvars']:
                    logger.debug("pitch adjustment by removing is variables")
                    pa_sol = self.remove_isfeature(pa_sol)
                    improved_harmony, current_sol = self.assess_sol(pa_sol,
                                                                    har_mem)

                if self.ps_bctrans is None or self.ps_bctrans:
                    logger.debug("pitch adjustment by removing bc variables")
                    pa_sol = self.remove_bcfeature(pa_sol)
                    improved_harmony, current_sol = self.assess_sol(pa_sol,
                                                                    har_mem)

                if self.ps_cor is None or self.ps_cor:
                    logger.debug("pitch adjustment by removing cor variables")
                    pa_sol = self.remove_corfeature(pa_sol)
                    improved_harmony, current_sol = self.assess_sol(pa_sol,
                                                                    har_mem)

                if pa_sol['class_params_spec'] is not None:  # check if has class_params_spec
                    logger.debug("pitch adjustment by removing class param variables")
                    pa_sol = self.remove_class_paramfeature(pa_sol)
                    improved_harmony, current_sol = self.assess_sol(pa_sol,
                                                                    har_mem)

                if pa_sol['member_params_spec'] is not None:  # check if has member_params_spec
                    logger.debug("pitch adjustment by removing member param variables")
                    pa_sol = self.remove_member_paramfeature(pa_sol)
                    improved_harmony, current_sol = self.assess_sol(pa_sol,
                                                                    har_mem)

            else:
                logger.debug("pitch adjustment by adding asfeature")
                pa_sol = self.add_new_asfeature(sol)
                improved_harmony, current_sol = self.assess_sol(pa_sol,
                                                                har_mem)
        else:
            logger.debug("no pitch adjustment")
            improved_harmony, current_sol = self.assess_sol(sol, har_mem)
        return (improved_harmony, current_sol)

    def best_features(self, har_mem):
        """
        Generates lists of best features in harmony memory
        Inputs:
        Harmony memory
        """
        HM = self.find_bestsol(har_mem)
        best_asvars = HM['asvars'].copy()
        best_isvars = HM['isvars'].copy()
        best_randvars = HM['randvars'].copy()
        best_bcvars = HM['bcvars'].copy()
        best_corvars = HM['cor_vars'].copy()
        asc_ind = HM['asc_ind']
        best_class_params_spec = None
        best_member_params_spec = None
        if HM['class_params_spec'] is not None:
            best_class_params_spec = HM['class_params_spec'].copy()
        if HM['member_params_spec'] is not None:
            best_member_params_spec = HM['member_params_spec'].copy()

        return (best_asvars, best_isvars, best_randvars, best_bcvars,
                best_corvars, asc_ind, best_class_params_spec,
                best_member_params_spec)

    def local_search(self, improved_harmony, itr, PAR_itr):
        """
        Initiate Artificial Bee-colony optimization
        Check if finetuning the best solution in harmony improves solution's BIC
        Inputs: improved memory after harmony consideration and pitch adjustment
        """
        # For plots (BIC vs. iterations)

        # Select best solution features
        best_asvars, best_isvars, best_randvars, best_bcvars, best_corvars, \
            asc_ind, best_class_params_spec, best_member_params_spec \
                = self.best_features(improved_harmony)

        logger.debug(("first set of best features input for local search - "
                     "as_vars: {}, is_vars: {}, rand_vars: {}, bc_vars: {}, "
                     "cor_vars: {}, best_class_params_spec: {}, "
                     "best_member_params_spec: {}").format(best_asvars,
                                                          best_isvars,
                                                          best_randvars,
                                                          best_bcvars,
                                                          best_corvars,
                                                          best_class_params_spec,
                                                          best_member_params_spec))
        # for each additional feature to the best solution, the objective function is tested

        # Check if changing coefficient distributions of best solution improves the solution BIC
        for var in best_randvars.keys():
            if var not in self.ps_rvars:
                rm_dist = [dis for dis in self.dist if dis != best_randvars[var]]
                best_randvars[var] = self.random_state.choice(rm_dist)
        best_randvars = {key: val for key, val in best_randvars.items()
                         if key in best_asvars and val != 'f'}
        best_bcvars = [var for var in best_bcvars if var in best_asvars
                       and var not in self.ps_corvars]
        best_corvars = [var for var in best_randvars.keys() if var
                        not in best_bcvars]
        solution_1 = Solution(asvars=best_asvars, isvars=best_isvars,
                              randvars=best_randvars, bcvars=best_bcvars,
                              cor_vars=best_corvars, asc_ind=asc_ind,
                              class_params_spec=best_class_params_spec,
                              member_params_spec=best_member_params_spec)
        logger.debug('solution_1: {}'.format(solution_1))
        improved_harmony, current_sol = self.assess_sol(solution_1,
                                                        improved_harmony)
        logger.debug('sol after local search step 1: {}'.format(str(improved_harmony[0])))

        # check if having a full covariance matrix has an improvement in BIC
        best_asvars, best_isvars, best_randvars, best_bcvars, best_corvars, \
            asc_ind, best_class_params_spec, best_member_params_spec = self.best_features(improved_harmony)
        best_bcvars = [var for var in best_asvars if var in self.ps_bcvars]
        if self.ps_cor is None or self.ps_cor:
            best_corvars = [var for var in best_randvars.keys() if var
                            not in best_bcvars]
        elif len(best_corvars) < 2:
            best_corvars = []
        else:
            best_corvars = []
        solution_2 = Solution(asvars=best_asvars, isvars=best_isvars,
                              randvars=best_randvars, bcvars=best_bcvars,
                              cor_vars=best_corvars, asc_ind=asc_ind,
                              class_params_spec=best_class_params_spec,
                              member_params_spec=best_member_params_spec)
        improved_harmony, current_sol = self.assess_sol(solution_2,
                                                        improved_harmony)
        logger.debug("sol after local search step 2: {}".format(str(improved_harmony[0])))

        # check if having a all the variables transformed has an improvement in BIC
        best_asvars, best_isvars, best_randvars, best_bcvars, best_corvars, \
            asc_ind, best_class_params_spec, best_member_params_spec = self.best_features(improved_harmony)
        if self.ps_bctrans is None or self.ps_bctrans:
            best_bcvars = [var for var in best_asvars if var
                           not in self.ps_corvars]
        else:
            best_bcvars = []
        best_corvars = [var for var in best_randvars.keys() if var
                        not in best_bcvars]
        solution_3 = Solution(asvars=best_asvars, isvars=best_isvars,
                              randvars=best_randvars, bcvars=best_bcvars,
                              cor_vars=best_corvars, asc_ind=asc_ind,
                              class_params_spec=best_class_params_spec,
                              member_params_spec=best_member_params_spec)
        improved_harmony, current_sol = self.assess_sol(solution_3,
                                                        improved_harmony)
        logger.debug("sol after local search step 3: {}".format(str(improved_harmony[0])))

        if len(best_asvars) < len(self.asvarnames):
            logger.debug("local search by adding variables")
            solution = Solution(asvars=best_asvars, isvars=best_isvars,
                                randvars=best_randvars, bcvars=best_bcvars,
                                cor_vars=best_corvars, asc_ind=asc_ind,
                                class_params_spec=best_class_params_spec,
                                member_params_spec=best_member_params_spec)
            solution_4 = self.add_new_asfeature(solution)
            improved_harmony, current_sol = self.assess_sol(solution_4,
                                                            improved_harmony)
            logger.debug("sol after local search step 4: {}".format(str(improved_harmony[0])))

        best_asvars, best_isvars, best_randvars, best_bcvars, best_corvars, \
            asc_ind, best_class_params_spec, best_member_params_spec = self.best_features(improved_harmony)
        solution = Solution(asvars=best_asvars, isvars=best_isvars,
                            randvars=best_randvars, bcvars=best_bcvars,
                            cor_vars=best_corvars, asc_ind=asc_ind,
                            class_params_spec=best_class_params_spec,
                            member_params_spec=best_member_params_spec)
        solution_5 = self.add_new_isfeature(solution)
        improved_harmony, current_sol = self.assess_sol(solution_5,
                                                        improved_harmony)
        logger.debug("sol after local search step 5: {}".format(str(improved_harmony[0])))

        best_asvars, best_isvars, best_randvars, best_bcvars, best_corvars, \
             asc_ind, best_class_params_spec, best_member_params_spec = self.best_features(improved_harmony)
        solution = Solution(asvars=best_asvars, isvars=best_isvars,
                            randvars=best_randvars, bcvars=best_bcvars,
                            cor_vars=best_corvars, asc_ind=asc_ind,
                            class_params_spec=best_class_params_spec,
                            member_params_spec=best_member_params_spec)
        solution_6 = self.add_new_bcfeature(solution, PAR_itr)
        improved_harmony, current_sol = self.assess_sol(solution_6,
                                                        improved_harmony)
        logger.debug("sol after local search step 6: {}".format(str(improved_harmony[0])))

        best_asvars, best_isvars, best_randvars, best_bcvars, best_corvars, \
            asc_ind, best_class_params_spec, best_member_params_spec = self.best_features(improved_harmony)
        solution = Solution(asvars=best_asvars, isvars=best_isvars,
                            randvars=best_randvars, bcvars=best_bcvars,
                            cor_vars=best_corvars, asc_ind=asc_ind,
                            class_params_spec=best_class_params_spec,
                            member_params_spec=best_member_params_spec)
        solution_7 = self.add_new_corfeature(solution)
        improved_harmony, current_sol = self.assess_sol(solution_7,
                                                        improved_harmony)
        logger.debug("sol after local search step 7: {}".format(str(improved_harmony[0])))

        # Sort unique harmony memory from min.BIC to max. BIC
        # improved_harmony = sorted(improved_harmony, key = lambda x: x[0])

        # Check if changing coefficient distributions of best solution improves the solution BIC
        best_asvars, best_isvars, best_randvars, best_bcvars, best_corvars, \
            asc_ind, best_class_params_spec, best_member_params_spec = self.best_features(improved_harmony)

        for var in best_randvars.keys():
            if var not in self.ps_rvars:
                rm_dist = [dis for dis in self.dist if dis != best_randvars[var]]
                best_randvars[var] = self.random_state.choice(rm_dist)
        best_randvars = {key: val for key, val in best_randvars.items()
                         if key in best_asvars and val != 'f'}
        best_bcvars = [var for var in best_bcvars if var in best_asvars and
                       var not in self.ps_corvars]
        if self.ps_cor is None or self.ps_cor:
            best_corvars = [var for var in best_randvars.keys() if var
                            not in best_bcvars]
        if self.ps_cor is False:
            best_corvars = []
        if len(best_corvars) < 2:
            best_corvars = []
        solution = Solution(asvars=best_asvars, isvars=best_isvars,
                            randvars=best_randvars, bcvars=best_bcvars,
                            cor_vars=best_corvars, asc_ind=asc_ind,
                            class_params_spec=best_class_params_spec,
                            member_params_spec=best_member_params_spec)
        improved_harmony, current_sol = self.assess_sol(solution,
                                                        improved_harmony)
        logger.debug("sol after local search step 8: {}".format(str(improved_harmony[0])))

        # check if having a full covariance matrix has an improvement in BIC
        best_asvars, best_isvars, best_randvars, best_bcvars, best_corvars, \
            asc_ind, best_class_params_spec, best_member_params_spec = self.best_features(improved_harmony)
        best_bcvars = [var for var in best_asvars if var in self.ps_bcvars]
        if self.ps_cor is None or self.ps_cor:
            best_corvars = [var for var in best_randvars.keys() if var not in best_bcvars]
        else:
            best_corvars = []
        if len(best_corvars) < 2:
            best_corvars = []
        solution = Solution(asvars=best_asvars, isvars=best_isvars,
                            randvars=best_randvars, bcvars=best_bcvars,
                            cor_vars=best_corvars, asc_ind=asc_ind,
                            class_params_spec=best_class_params_spec,
                            member_params_spec=best_member_params_spec)
        improved_harmony, current_sol = self.assess_sol(solution, improved_harmony)
        logger.debug("sol after local search step 9: {}".format(str(improved_harmony[0])))

        # check if having all the variables transformed has an improvement in BIC
        best_asvars, best_isvars, best_randvars, best_bcvars, best_corvars, \
            asc_ind, best_class_params_spec, best_member_params_spec = self.best_features(improved_harmony)
        if self.ps_bctrans is None or self.ps_bctrans:
            best_bcvars = [var for var in best_asvars if var not in self.ps_corvars]
        else:
            best_bcvars = []
        if self.ps_cor is None or self.ps_cor:
            best_corvars = [var for var in best_randvars.keys()
                            if var not in best_bcvars]
        else:
            best_corvars = []

        if len(best_corvars) < 2:
            best_corvars = []
        solution = Solution(asvars=best_asvars, isvars=best_isvars,
                            randvars=best_randvars, bcvars=best_bcvars,
                            cor_vars=best_corvars, asc_ind=asc_ind,
                            class_params_spec=best_class_params_spec,
                            member_params_spec=best_member_params_spec)
        improved_harmony, current_sol = self.assess_sol(solution,
                                                        improved_harmony)
        logger.debug("sol after local search step 10: {}".format(str(improved_harmony[0])))

        # Sort unique harmony memory from min.BIC to max. BIC
        # final_harmony_sorted = sorted(improved_harmony, key = lambda x: x[0])
        final_harmony_sorted = improved_harmony
        return (final_harmony_sorted, current_sol)

    # Function to conduct harmony memory consideraion, pitch adjustment and local search
    def improvise_harmony(self, HCR_max, HCR_min, PR_max, PR_min, har_mem,
                          max_itr, threshold, itr_prop, HM):
        itr = 0

        # for BIC vs. iteration plots
        best_bic_points = []
        current_bic_points = []
        best_val_points = []

        while itr < max_itr:
            # TODO: Progress bar
            itr += 1
            logger.info("Improvising harmony at iteration {}".format(itr))
            # Estimate dynamic HMCR and PCR values for each iteration
            HMCR_itr = (HCR_min + ((HCR_max-HCR_min)/max_itr)*itr) * max(0, math.sin(itr))
            PAR_itr = (PR_min + ((PR_max-PR_min)/max_itr)*itr) * max(0, math.sin(itr))

            # Conduct Harmony Memory Consideration
            hmc_sol = self.harmony_consideration(har_mem, HMCR_itr, itr, HM)
            logger.debug("solution after HMC at iteration {}, is: {}".format(itr, str(hmc_sol)))
            # Conduct Pitch Adjustment
            pa_hm, current_sol = self.pitch_adjustment(hmc_sol, har_mem,
                                                       PAR_itr, itr,
                                                       self.HMS)
            logger.debug("best solution after HMC & PA at iteration: {}, is - {}" .format(itr, str(pa_hm[0])))
            current_bic_points.append(current_sol['bic'])
            # Sort unique harmony memory from min.BIC to max. BIC
            # har_mem_sorted = sorted(pa_hm, key = lambda x: x[0])
            har_mem = pa_hm

            # check iteration to initiate local search
            if itr > int(itr_prop * max_itr):
                logger.debug("HM before starting local search: {}".format(str(har_mem)))

                har_mem, current_sol = self.local_search(har_mem, itr, PAR_itr)
                # Sort unique harmony memory from min.BIC to max. BIC

                logger.debug("final harmony in current iteration {}, is - {} ".format(itr, str(har_mem)))

                best_bic_points.append(har_mem[0]['bic'])
                current_bic_points.append(current_sol['bic'])
                logger.debug(har_mem[0]['bic'])

                logger.debug(har_mem[0]['bic'])

            if itr == max_itr:  # Plot on final iteration
                val_key = 'MAE' if self.multi_objective else 'loglik'
                valid_idx = [ii for ii, har_mem_ii in enumerate(har_mem)
                             if np.abs(har_mem_ii['bic']) < 1e+7
                             and np.abs(har_mem_ii[val_key]) < 1e+7]

                har_mem_iteration_order = sorted(list(np.array(har_mem)[valid_idx]), key=lambda sol: sol['sol_num'])

                all_bic_points = [har_mem_sol['bic'] for _, har_mem_sol in enumerate(har_mem_iteration_order)]
                all_val_points = [har_mem_sol[val_key] for _, har_mem_sol in enumerate(har_mem_iteration_order)]

                best_bic_points = []
                best_val_points = []
                min_bic = 1e+30
                min_val = 1e+30
                max_val = -1e+30

                for ii, bic in enumerate(all_bic_points):
                    if bic < min_bic:
                        min_bic = bic
                    best_bic_points.append(min_bic)

                for ii, val in enumerate(all_val_points):
                    if val == 1:  # Some values default to 1 for MAE causing issues
                        val = -1e+30
                    if self.multi_objective:
                        if val < min_val:
                            min_val = val
                        best_val_points.append(min_val)
                    else:
                        if val > max_val:
                            max_val = val
                        best_val_points.append(max_val)
                # TODO? REFACTOR
                all_bic = all_bic_points
                all_val = all_val_points

                logger.debug('best_bic_points: {}'.format(best_bic_points))
                logger.debug('best_val_points: {}'.format(best_val_points))

                if self.multi_objective:  # Plot for MOOF
                    Fronts = self.get_fronts(har_mem)
                    Pareto = self.pareto(Fronts, har_mem)
                    fig, ax = plt.subplots()

                    lns1 = ax.scatter(all_bic, np.log(all_val), label="All solutions", marker='o')
                    init_sols = [init_sol for _, init_sol in enumerate(HM) if np.abs(init_sol['bic']) < 1000000]
                    init_bic = [init_sol['bic'] for _, init_sol in enumerate(init_sols)]
                    init_val = [init_sol['MAE'] for _, init_sol in enumerate(init_sols)]
                    lns2 = ax.scatter(init_bic, np.log(init_val), label="Initial solutions",  marker='x')

                    Pareto = [pareto for _, pareto in enumerate(Pareto) if np.abs(pareto['bic']) < 1000000]
                    logger.info('Final Pareto: {}'.format(str(Pareto)))

                    # TODO? SORT PARETO FOR BETTER VISUALISATION
                    pareto_bic = np.array([pareto['bic'] for _, pareto in enumerate(Pareto)])
                    pareto_val = np.log([pareto['MAE'] for _, pareto in enumerate(Pareto)])
                    pareto_idx = np.argsort(pareto_bic)
                    # lns3 = ax.scatter(pareto_bic, pareto_val, label="Pareto Front", marker='o')
                    lns4 = ax.plot(pareto_bic[pareto_idx], pareto_val[pareto_idx], color="r", label="Pareto Front")
                    lns = (lns1, lns2, lns4[0])
                    labs = [l_pot.get_label() for l_pot in lns]
                    ax.set_xlabel("BIC - training dataset")
                    ax.set_ylabel("Log MAE - testing dataset")
                    lgd = ax.legend(lns, labs, loc='upper center', bbox_to_anchor=(0.5, -0.1))  # TODO! FIX
                    current_time = datetime.datetime.now().strftime("%d%m%Y-%H%M%S")
                    latent_info = "_" + str(self.num_classes) + "_classes_" if (self.num_classes > 1) else "_"
                    plot_filename = self.code_name + latent_info + current_time + "_MOOF.png"
                    plt.savefig(plot_filename,
                                bbox_extra_artists=(lgd,), bbox_inches='tight')
                else:  # Plot for SOOF
                    fig, ax1 = plt.subplots()
                    ax2 = ax1.twinx()
                    ax1.xaxis.get_major_locator().set_params(integer=True)
                    # TODO: REMOVE 100000?
                    lns1 = ax1.plot(np.arange(len(all_bic)), all_bic, label="BIC of solution estimated at current iteration")
                    lns2 = ax1.plot(np.arange(len(best_bic_points)), best_bic_points, label="BIC of best solution in memory at current iteration", linestyle="dotted")
                    lns3 = ax2.plot(np.arange(len(best_val_points)), best_val_points, label="In-sample LL of best solution in memory at current iteration", linestyle="dashed")
                    lns = lns1 + lns2 + lns3
                    labs = [l_pot.get_label() for l_pot in lns]
                    handles, _ = ax1.get_legend_handles_labels()
                    lgd = ax1.legend(lns, labs, loc='upper center', bbox_to_anchor=(0.5, -0.1))
                    ax1.set_xlabel("Iterations")
                    ax1.set_ylabel("BIC")
                    ax2.set_ylabel("LL")
                    current_time = datetime.datetime.now().strftime("%d%m%Y-%H%M%S")

                    latent_info = "_" + str(self.num_classes) + "_classes_" if (self.num_classes > 1) else "_"
                    plot_filename = self.code_name + latent_info + current_time + "_SOOF.png"
                    plt.savefig(plot_filename,
                                bbox_extra_artists=(lgd,), bbox_inches='tight')

                pass

            if itr == max_itr+1:
                break

        return (har_mem, best_bic_points, current_bic_points)

    def _prep_inputs(self, asvarnames=[], isvarnames=[]):
        """Include modellers' model prerequisites if any."""
        # pre-included alternative-sepcific variables
        # binary indicators representing alternative-specific variables
        # that are prespecified by the user
        psasvar_ind = [0] * len(asvarnames)

        # binary indicators representing individual-specific variables prespecified by the user
        psisvar_ind = [0] * len(isvarnames)

        # pre-included distributions
        # pspecdist_ind = ["f"]* 9 + ["any"] * (len(asvarnames)-9)
        # variables whose coefficient distribution have been prespecified by the modeller
        pspecdist_ind = ["any"] * len(asvarnames)

        # prespecification on estimation of intercept
        # ps_intercept = None  # (True or False or None)  # TODO? REMOVED?

        # prespecification on transformations
        # ps_bctrans = None  # (True or False or None)  # TODO? REMOVED
        # indicators representing variables with prespecified transformation by the modeller
        ps_bcvar_ind = [0] * len(asvarnames)

        # prespecification on estimation of correlation
        # ps_cor = None  # (True or False or None)  # TODO? REMOVED
        # [1,1,1,1,1] indicators representing variables with prespecified correlation by the modeller
        ps_corvar_ind = [0] * len(asvarnames)

        # prespecified interactions
        # ps_interaction = None  # (True or False or None)  # TODO? REMOVE?
        return (psasvar_ind, psisvar_ind, pspecdist_ind, ps_bcvar_ind,
                ps_corvar_ind)

    def run_search(self, HMS=10, HMCR_min=0.6, HMCR_max=0.9, PAR_max=0.85,
                   PAR_min=0.3, itr_max=30, v=0.8, threshold=15):
        """_summary_

        Args:
            HMS (int, optional): _description_. Defaults to 10.
            HMCR_min (float, optional): minimum harmony memory consideration rate. Defaults to 0.6.
            HMCR_max (float, optional): maximum harmony memory consideration rate. Defaults to 0.9.
            PAR_max (float, optional): max pitch adjustment. Defaults to 0.85.
            PAR_min (float, optional): min pitch adjustment. Defaults to 0.3.
            itr_max (int, optional): _description_. Defaults to 30.
            v (float, optional): proportion of iterations to improvise harmony. The rest will be for local search. Defaults to 0.8.
            threshold (int, optional): threshold to compare new solution with worst solution in memory. Defaults to 15.
            val_share (float, optional): _description_. Defaults to 0.25.

        Returns:
            _type_: _description_
        """
        n_gpus = dev.get_device_count()
        gpu_txt = "" if n_gpus > 0 else "not "
        logger.debug("{} GPU device(s) available. searchlogit will {} use GPU processing".format(n_gpus, gpu_txt))

        avail_asvars, avail_isvars, avail_rvars, avail_bcvars, avail_corvars = \
            self.avail_features()

        self.avail_asvars = avail_asvars
        self.avail_isvars = avail_isvars

        # TODO? better setting?
        if not self.allow_random:
            avail_rvars = []
        self.avail_rvars = avail_rvars
        if not self.allow_bcvars:
            avail_bcvars = []
        self.avail_bcvars = avail_bcvars
        self.avail_corvars = avail_corvars

        asvars_new = self.df_coeff_col(self.asvarnames)

        asvars_new = self.remove_redundant_asvars(asvars_new,
                                                  self.trans_asvars,
                                                  self.asvarnames)
        self.generate_sol()

        Init_HM = self.initialize_memory(HMS)

        # Remove duplicate solutions if present
        unique = set()
        unique_HM = [unique.add(x['bic']) or x for x in Init_HM if x['bic'] not in unique]

        # Sort unique harmony memory from min.BIC to max. BIC
        HM_sorted = sorted(unique_HM, key=lambda x: x['bic'])

        # Trim the Harmony memory's size as per the harmony memory size
        HM = HM_sorted[:HMS]
        logger.info("Initial harmony memory: {}".format(str(HM)))
        hm = HM.copy()

        self.HMS = HMS

        initial_harmony = hm.copy()
        new_HM, best_BICs, current_BICs = \
            self.improvise_harmony(HMCR_max, HMCR_min, PAR_max, PAR_min,
            initial_harmony, itr_max,
            threshold, v, HM)
        improved_harmony = new_HM.copy()

        logger.info("Improved harmony: {}".format(improved_harmony))

        if self.multi_objective:
            hm = self.non_dominant_sorting(improved_harmony)
            improved_harmony = hm.copy()
            best_sol = hm[0]  # TODO! SHOULD INSTEAD PRINT ALL ON PARETO FRONT?!
        else:  # single objective - bic, the 0-th index
            improved_harmony.sort(key=lambda x: x['bic'])
            best_sol = improved_harmony[0]
        logger.info("Search ended at: {}".format(str(time.ctime())))
        best_asvarnames = best_sol['asvars']
        best_isvarnames = best_sol['isvars']
        best_randvars = best_sol['randvars']
        best_bcvars = best_sol['bcvars']
        best_corvars = best_sol['cor_vars']
        best_intercept = best_sol['asc_ind']
        best_class_params_spec = best_sol['class_params_spec']
        best_member_params_spec = best_sol['member_params_spec']

        if self.latent_class:
            class_vars = list(np.concatenate(best_class_params_spec))
            member_vars = list(np.concatenate(best_member_params_spec))
            all_vars = class_vars + member_vars + best_isvarnames
            best_varnames = np.unique(all_vars)
        else:
            best_varnames = best_asvarnames + best_isvarnames

        # delete '_inter' bug fix
        if '_inter' in best_varnames:
            best_varnames = np.delete(best_varnames, np.argwhere(best_varnames == '_inter'))
        logger.info("Estimating best solution with entire dataset.")
        # TODO? confirm works for SOOF
        df_all = self.df.append(self.df_test)

        X = df_all[best_varnames]
        y = self.choice_var.append(self.test_choice_var)
        seed = self.random_state.randint(2**31 - 1)

        avail_all = self.avail
        avail_latent_all = self.avail_latent
        weights_all = self.weights
        alt_var_all = self.alt_var
        choice_id_all = self.choice_id
        ind_id_all = self.ind_id

        if self.multi_objective:
            if self.avail is not None:
                avail_all = np.row_stack((self.avail, self.test_av))
            if self.avail_latent is not None:
                avail_latent_all = [None] * self.num_classes
                for ii, avail_latent_ii in enumerate(self.avail_latent):
                    if avail_latent_ii is not None:
                        avail_latent_all[ii] = np.row_stack((avail_latent_ii, self.test_avail_latent[ii]))
            if self.weights is not None:
                weights_all = np.concatenate((self.weights, self.test_weight_var))
            if self.alt_var is not None:
                alt_var_all = np.concatenate((self.alt_var, self.test_alt_var))
            if self.choice_id is not None:
                choice_id_all = np.concatenate((self.choice_id, self.test_choice_id))
            if self.ind_id is not None:
                ind_id_all = np.concatenate((self.ind_id, self.test_ind_id))

        if bool(best_randvars):
            if self.latent_class:
                model = LatentClassMixedModel()
                model.fit(X, y, varnames=best_varnames, isvars=best_isvarnames,
                          class_params_spec=best_class_params_spec,
                          member_params_spec=best_member_params_spec,
                          num_classes=self.num_classes, alts=alt_var_all,
                          ids=choice_id_all, panels=ind_id_all,
                          fit_intercept=best_intercept,
                          transformation="boxcox", transvars=best_bcvars,
                          randvars=best_randvars,
                          correlation=best_corvars,
                          maxiter=self.maxiter, gtol=self.gtol,
                          avail=avail_all,
                          weights=weights_all)
            else:
                model = MixedLogit()
                model.fit(X=X, y=y, varnames=best_varnames,
                          isvars=best_isvarnames, alts=self.alt_var, ids=choice_id_all,
                          panels=ind_id_all, randvars=best_randvars,
                          transformation="boxcox", transvars=best_bcvars,
                          fit_intercept=best_intercept, correlation=best_corvars,
                          n_draws=self.n_draws)
        else:
            if self.latent_class:
                model = LatentClassModel()
                model.fit(X, y, varnames=best_varnames,
                          # isvars=best_isvarnames,
                          class_params_spec=best_class_params_spec,
                          member_params_spec=best_member_params_spec,
                          num_classes=self.num_classes, alts=alt_var_all,
                          ids=choice_id_all, fit_intercept=best_intercept,
                          transformation="boxcox", transvars=best_bcvars,
                        #   randvars=best_randvars,
                        #   correlation=best_corvars,
                          maxiter=self.maxiter, gtol=self.gtol,
                          gtol_membership_func=self.gtol_membership_func,
                          avail=avail_all,
                          avail_latent=avail_latent_all,
                          intercept_opts=self.intercept_opts,
                          weights=weights_all, random_state=seed)
            else:
                model = MultinomialLogit()
                model.fit(X, y,
                          varnames=best_varnames, isvars=best_isvarnames,
                          alts=alt_var_all, ids=choice_id_all,
                          transformation="boxcox", transvars=best_bcvars,
                          fit_intercept=best_intercept)

        old_stdout = sys.stdout
        log_file = open(self.logger_name, "a")
        sys.stdout = log_file
        logger.info("Best model")
        model.summary()
        sys.stdout = old_stdout
        log_file.close()
        if not self.multi_objective:
            logger.info("best_BICs: {}".format(best_BICs))
            logger.info("current_BICs: {}".format(current_BICs))

        return improved_harmony

    def run_search_latent(self, HMS=10, min_classes=1, max_classes=10,
                          HMCR_min=0.6, HMCR_max=0.9, PAR_max=0.85,
                          PAR_min=0.3, itr_max=30, v=0.8, threshold=15):
        models = []
        prev_bic = 1e+30
        best_model_idx = 0
        all_harmony = []
        for q in range(min_classes, max_classes):
            if q == 1:
                self.latent_class = False
                self.num_classes = q
            else:
                self.latent_class = True
                self.num_classes = q
            logger.info("Starting search with {} classes".format(q))
            search_harmony = self.run_search(HMS=HMS, HMCR_min=HMCR_min,
                                    HMCR_max=HMCR_max, PAR_max=PAR_max,
                                    PAR_min=PAR_min, itr_max=itr_max, v=v,
                                    threshold=threshold)
            for sol_i in search_harmony:
                sol_i['class_num'] = q
            all_harmony = all_harmony + search_harmony

            if self.multi_objective:
                all_harmony = self.non_dominant_sorting(all_harmony)
                Fronts = self.get_fronts(all_harmony)
                Pareto = self.pareto(Fronts, all_harmony)
                stop_run = True
                for sol_pareto in Pareto:
                    if sol_pareto['class_num'] == q:
                        stop_run = False
                if stop_run:
                    break
                best_model_idx += 1
            else:
                solution = search_harmony[0]  # assume already sorted
                if solution['bic'] < prev_bic:
                    best_model_idx += 1
                    prev_bic = solution['bic']
                else:
                    break

        if self.multi_objective:
            logger.info("Models in Pareto front had at most {} classes".format(q-1))
            logger.info("Best models in Pareto front")
            for ii, sol in enumerate(Pareto):
                logger.info(f'Best solution - {ii}')
                for k, v in sol:
                    logger.info(f"{k}: {v}")
        else:
            logger.info("Model with best BIC had {} classes".format(q-1))
            logger.info("Best solution")
            for k, v in solution:
                logger.info(f"{k}: {v}")

        return all_harmony

    def check_dominance(self, obj1, obj2):
        """
        Function checks dominance between solutions for two objective functions
        Inputs: obj1 - List containing values of the two objective functions for solution 1
                obj2 - List containing values of the two objective functions for solution 2
        Output: Returns True if solution 1 dominates 2, False otherwise
        """
        indicator = False
        for a, b in zip(obj1, obj2):
            if a < b:
                indicator = True
            # if one of the objectives is dominated, then return False
            elif a > b:
                return False
        return indicator

    # Final Pareto-front identifier
    def get_fronts(self, HM):
        """
        Funtion for non-dominant sorting of the given set of solutions
        ni - the number of solutions which dominate the solution i
        si - a set of solutions which the solution i dominates

        Inputs: List containing set of solutions

        Output: Dict with keys indicating the Pareto rank and values containing indices of solutions in Input
        """
        si = {}
        ni = {}
        val_key = 'MAE' if self.multi_objective else 'loglik'
        for i in range(len(HM)):
            sp_i = []
            np_i = 0
            for j in range(len(HM)):
                if i != j:
                    dominance = self.check_dominance([HM[i]['bic'], HM[i][val_key]],
                                                     [HM[j]['bic'], HM[j][val_key]])
                    if dominance:
                        sp_i.append(j)
                    else:
                        dominance = self.check_dominance([HM[j]['bic'], HM[j][val_key]],
                                                         [HM[i]['bic'], HM[i][val_key]])
                        if dominance:
                            np_i += 1
            si.update({i: sp_i})
            ni.update({i: np_i})
        # Identify solutions in each front
        Fronts = {}
        itr = 0
        for k in range(max(ni.keys())):
            Fi_idx = [key for key, val in ni.items() if val == k]
            if len(Fi_idx) > 0:
                Fronts.update({'F_{}'.format(itr): Fi_idx})
                itr += 1
        logger.debug("Fronts: {}".format(str(Fronts)))
        return Fronts

    def crowding_dist(self, Fronts, HM):
        """
        Function to estimate crowding distance between 2 solutions
        Inputs:
        Fronts-Dict with keys indicating Pareto rank and values indicating indices of solutions belonging to the rank
        HM - List of solutions
        """
        v_dis = {}
        val_key = 'MAE' if self.multi_objective else 'loglik'

        for v in Fronts.values():
            v.sort(key=lambda x: HM[x]['bic'])
            for i in v:
                v_dis.update({i: 0})
        # Calculate crowding distance based on first objective
        for v in Fronts.values():
            for j in v:
                if v[0] == j or v[-1] == j:
                    v_dis.update({j: 1000000})
                else:
                    dis = abs(v_dis.get(j) +
                              ((HM[v[v.index(j) + 1]]['bic'] -
                                HM[j]['bic']) / (max(HM[x]['bic'] for x in
                                                 range(len(HM))) -
                                             min(HM[x]['bic'] for x in
                                                 range(len(HM))))))
                    v_dis.update({j: dis})

        # Calculate crowding distance based on second objective
        q_dis = {}
        for v in Fronts.values():
            v.sort(key=lambda x: HM[x][val_key])
            for k in v:
                q_dis.update({k: 0})
        for v in Fronts.values():
            for k in v:
                if v[0] == k or v[-1] == k:
                    q_dis.update({k: 1000000})
                else:
                    dis = abs(q_dis.get(k) + ((HM[v[v.index(k)+1]][val_key] -
                                               HM[k][val_key])
                                               / (max(HM[x][val_key] for x
                                                     in range(len(HM))) -
                                                 min(HM[x][val_key] for x in
                                                     range(len(HM))))))
                    q_dis.update({k: dis})
        # Adding crowding distance from both objectives
        crowd = {k: q_dis[k] + v_dis[k] for k in v_dis.keys()}
        return crowd

    def pareto(self, Fronts, HM):
        Pareto_front_id = []
        for k, v in Fronts.items():
            if len(v) > 0:
                Pareto_front_id = Fronts.get(k)
                break
        Pareto_front = [HM[x] for x in Pareto_front_id]
        return Pareto_front

    def sort_InitHM(self, Fronts, v_dis, HM):
        """
        Function to sort memory from best solution to worst solution
        Inputs:
        Fronts-Dict with keys indicating Pareto rank and values indicating indices of solutions belonging to the rank
        v_dis - Dict with keys indicating index of solution in memory and value indicating crowding distance
        Output:
        Sorted_HM - Sorted list of solutions
        """
        Sorted_HM_id = []
        for k, v in Fronts.items():
            pareto_sols = {key: val for key, val in v_dis.items() if key
                           in Fronts.get(k)}
            Sorted_HM_id.extend([ke for ke, va in
                                sorted(pareto_sols.items(),
                                       key=lambda item: item[1],
                                       reverse=True)])

            # Sorted_HM_id.extend([ke for ke, va in sorted(pareto_sols.items(), key=lambda item: item[1])])
            if len(Sorted_HM_id) >= self.HMS:
                break
        Sorted_HM = [HM[x] for x in Sorted_HM_id]
        return Sorted_HM

    def non_dominant_sorting_initHM(self, HM):
        Front = self.get_fronts(HM)
        crowd = self.crowding_dist(Front, HM)
        Final_HM = self.sort_InitHM(Front, crowd, HM)
        return Final_HM

    def sort_HM(self, Fronts, v_dis, HM):
        """
        Function to sort memory from best solution to worst solution
        Inputs:
        Fronts-Dict with keys indicating Pareto rank and values indicating indices of solutions belonging to the rank
        v_dis - Dict with keys indicating index of solution in memory and value indicating crowding distance
        Output:
        Sorted_HM - Sorted list of solutions
        """
        Sorted_HM_id = []
        for k, v in Fronts.items():
            pareto_sols = {key: val for key, val in v_dis.items()
                           if key in Fronts.get(k)}
            Sorted_HM_id.extend([ke for ke, va in
                                 sorted(pareto_sols.items(),
                                        key=lambda item: item[1])])

        Sorted_HM = [HM[x] for x in Sorted_HM_id]
        return Sorted_HM

    def non_dominant_sorting(self, HM):
        Front = self.get_fronts(HM)
        crowd = self.crowding_dist(Front, HM)
        Final_HM = self.sort_HM(Front, crowd, HM)
        return Final_HM

    def find_bestsol(self, HM):
        max_obj1 = max(HM[x]['bic'] for x in range(len(HM)))
        min_obj1 = min(HM[x]['bic'] for x in range(len(HM)))
        weights_obj1 = [(HM[x]['bic'])-min_obj1/(max_obj1-min_obj1) for x in range(len(HM))]

        if self.multi_objective:
            max_obj2 = max(HM[x]['MAE'] for x in range(len(HM)))
            min_obj2 = min(HM[x]['MAE'] for x in range(len(HM)))
            weights_obj2 = [(HM[x]['MAE'])-min_obj2/(max_obj2-min_obj2) for x in range(len(HM))]

            weights = [weights_obj1[x] + weights_obj2[x] for x in range(len(HM))]
        else:
            weights = weights_obj1
        best_solid = weights.index(min(weights))
        logger.debug("best sol for local search: {}".format(HM[best_solid]))
        return HM[best_solid]
