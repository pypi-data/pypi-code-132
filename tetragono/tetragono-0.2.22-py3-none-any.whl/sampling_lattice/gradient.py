#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2020-2022 Hao Zhang<zh970205@mail.ustc.edu.cn>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import inspect
import signal
from datetime import datetime
import numpy as np
import TAT
from ..sampling_lattice import SamplingLattice, Observer, SweepSampling, ErgodicSampling, DirectSampling
from ..common_toolkit import (show, showln, mpi_comm, mpi_rank, mpi_size, bcast_lattice_buffer, SignalHandler,
                              seed_differ, lattice_randomize, write_to_file, read_from_file, get_imported_function)


def check_difference(state, observer, grad, energy_observer, configuration_pool, check_difference_delta):

    def get_energy():
        with energy_observer:
            for possibility, configuration in configuration_pool:
                configuration.refresh_all()
                energy_observer(possibility, configuration)
        energy, _ = energy_observer.total_energy
        return energy

    original_energy, _ = observer.total_energy
    delta = check_difference_delta
    showln(f"difference delta is set as {delta}")
    for l1 in range(state.L1):
        for l2 in range(state.L2):
            showln(l1, l2)
            s = state[l1, l2].storage
            g = grad[l1][l2].transpose(state[l1, l2].names).storage
            for i in range(len(s)):
                value = s[i]
                s[i] = value + delta
                now_energy = get_energy()
                rgrad = (now_energy - original_energy) / delta
                if state.Tensor.is_complex:
                    s[i] = value + delta * 1j
                    now_energy = get_energy()
                    igrad = (now_energy - original_energy) / delta
                    cgrad = rgrad + igrad * 1j
                else:
                    cgrad = rgrad
                s[i] = value
                showln(" ", abs(g[i] - cgrad) / abs(cgrad), cgrad, g[i])


def line_search(state, observer, grad, energy_observer, configuration_pool, step_size, line_search_amplitude,
                line_search_error_threshold):
    saved_state = [[state[l1, l2] for l2 in range(state.L2)] for l1 in range(state.L1)]

    def restore_state():
        for l1 in range(state.L1):
            for l2 in range(state.L2):
                state[l1, l2] = saved_state[l1][l2]

    grad_dot_pool = {}

    def grad_dot(eta):
        if eta not in grad_dot_pool:
            for l1 in range(state.L1):
                for l2 in range(state.L2):
                    state[l1, l2] = state[l1, l2] - eta * grad[l1][l2]
            with energy_observer:
                for possibility, configuration in configuration_pool:
                    configuration.refresh_all()
                    energy_observer(possibility, configuration)
                    show(f"predicting eta={eta}, energy={energy_observer.energy}")
            result = mpi_comm.bcast(state.lattice_dot(grad, energy_observer.gradient))
            showln(f"predict eta={eta}, energy={energy_observer.energy}, gradient dot={result}")
            grad_dot_pool[eta] = result
            restore_state()
        return grad_dot_pool[eta]

    grad_dot_pool[0] = mpi_comm.bcast(state.lattice_dot(grad, observer.gradient))
    if grad_dot(0.0) > 0:
        begin = 0.0
        end = step_size * line_search_amplitude

        if grad_dot(end) > 0:
            step_size = end
            showln(f"step_size is chosen as {step_size}, since grad_dot(begin) > 0, grad_dot(end) > 0")
        else:
            while True:
                x = (begin + end) / 2
                if grad_dot(x) > 0:
                    begin = x
                else:
                    end = x
                if (end - begin) / end < line_search_error_threshold:
                    step_size = begin
                    showln(f"step_size is chosen as {step_size}, since step size error < {line_search_error_threshold}")
                    break
    else:
        showln(f"step_size is chosen as {step_size}, since grad_dot(begin) < 0")
        step_size = step_size

    return mpi_comm.bcast(step_size)


def gradient_descent(
        state: SamplingLattice,
        sampling_total_step=0,
        grad_total_step=1,
        grad_step_size=0,
        *,
        # About observer
        cache_configuration=False,
        classical_energy=None,
        # About sampling
        sampling_method="direct",
        configuration_cut_dimension=None,
        direct_sampling_cut_dimension=4,
        sampling_configurations=[],
        sweep_hopping_hamiltonians=None,
        # About subspace
        restrict_subspace=None,
        # About gradient method
        use_check_difference=False,
        use_line_search=False,
        use_fix_relative_step_size=False,
        use_random_gradient=False,
        momentum_parameter=0.0,
        # About natural gradient
        use_natural_gradient=False,
        conjugate_gradient_method_step=20,
        conjugate_gradient_method_error=0.0,
        metric_inverse_epsilon=0.01,
        cache_natural_delta=None,
        # About gauge fixing
        fix_gauge=False,
        # About log and save state
        log_file=None,
        save_state_interval=None,
        save_state_file=None,
        save_configuration_file=None,
        # About line search
        line_search_amplitude=1.25,
        line_search_error_threshold=0.1,
        # About momentum
        orthogonalize_momentum=False,
        # About check difference
        check_difference_delta=1e-8,
        # About Measurement
        measurement=None):

    if save_state_interval is not None:
        showln(" ##### DEPRECATE WARNING BEGIN #####")
        showln(" save_state_interval is deprecated, state will be saved for every step in future")
        showln(" ###### DEPRECATE WARNING END ######")
    else:
        save_state_interval = 1

    time_str = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")

    # Gradient step
    use_gradient = grad_step_size != 0 or use_check_difference
    if use_gradient:
        if use_check_difference:
            grad_total_step = 1
        else:
            grad_total_step = grad_total_step
    else:
        grad_total_step = 1
    showln(f"gradient total step={grad_total_step}")

    # Restrict subspace
    if restrict_subspace is not None:
        origin_restrict = get_imported_function(restrict_subspace, "restrict")
        if len(inspect.signature(origin_restrict).parameters) == 1:

            def restrict(configuration, replacement=None):
                if replacement is None:
                    return origin_restrict(configuration)
                else:
                    configuration = configuration.copy()
                    for [l1, l2, orbit], new_site_config in replacement.items():
                        configuration[l1, l2, orbit] = new_site_config
                    return origin_restrict(configuration)
        else:
            restrict = origin_restrict
    else:
        restrict = None

    # Classical energy
    if classical_energy is not None:
        classical_energy = get_imported_function(classical_energy, "classical_energy")

    # Prepare observers
    observer = Observer(
        state,
        enable_energy=True,
        enable_gradient=use_gradient,
        enable_natural_gradient=use_natural_gradient,
        cache_natural_delta=cache_natural_delta,
        cache_configuration=cache_configuration,
        restrict_subspace=restrict,
        classical_energy=classical_energy,
    )
    if measurement:
        measurement_names = measurement.split(",")
        for measurement_name in measurement_names:
            observer.add_observer(measurement_name, get_imported_function(measurement_name, "measurement")(state))
    if use_gradient:
        need_energy_observer = use_line_search or use_check_difference
    else:
        need_energy_observer = False
    if need_energy_observer:
        energy_observer = Observer(
            state,
            enable_energy=True,
            enable_gradient=use_line_search,
            cache_configuration=cache_configuration,
            restrict_subspace=restrict,
            classical_energy=classical_energy,
        )

    # Main loop
    with SignalHandler(signal.SIGINT) as sigint_handler:
        for grad_step in range(grad_total_step):
            if need_energy_observer:
                configuration_pool = []
            # Sampling and observe
            with seed_differ, observer:
                # Sampling method
                if sampling_method == "sweep":
                    if sweep_hopping_hamiltonians is not None:
                        hopping_hamiltonians = get_imported_function(sweep_hopping_hamiltonians,
                                                                     "hopping_hamiltonians")(state)
                    else:
                        hopping_hamiltonians = None
                    sampling = SweepSampling(state, configuration_cut_dimension, restrict, hopping_hamiltonians)
                    sampling_total_step = sampling_total_step
                    # Initial sweep configuration
                    if len(sampling_configurations) < mpi_size:
                        choose = TAT.random.uniform_int(0, len(sampling_configurations) - 1)()
                    else:
                        choose = mpi_rank
                    sampling.configuration.import_configuration(sampling_configurations[choose])
                elif sampling_method == "ergodic":
                    sampling = ErgodicSampling(state, configuration_cut_dimension, restrict)
                    sampling_total_step = sampling.total_step
                elif sampling_method == "direct":
                    sampling = DirectSampling(state, configuration_cut_dimension, restrict,
                                              direct_sampling_cut_dimension)
                    sampling_total_step = sampling_total_step
                else:
                    raise ValueError("Invalid sampling method")
                # Sampling run
                for sampling_step in range(sampling_total_step):
                    if sampling_step % mpi_size == mpi_rank:
                        possibility, configuration = sampling()
                        observer(possibility, configuration)
                        if need_energy_observer:
                            configuration_pool.append((possibility, configuration))
                        show(f"sampling {sampling_step}/{sampling_total_step}, energy={observer.energy}")
                # Save configuration
                gathered_configurations = mpi_comm.allgather(configuration.export_configuration())
                sampling_configurations.clear()
                sampling_configurations += gathered_configurations
            showln(f"sampling done, total_step={sampling_total_step}, energy={observer.energy}")

            # Measure log
            if measurement and mpi_rank == 0:
                for measurement_name in measurement_names:
                    measurement_result = observer.result[measurement_name]
                    get_imported_function(measurement_name, "save_result")(state, measurement_result, grad_step)
            # Energy log
            if log_file and mpi_rank == 0:
                with open(log_file.replace("%t", time_str), "a", encoding="utf-8") as file:
                    print(*observer.energy, file=file)

            if use_gradient:

                # Get gradient
                if use_natural_gradient:
                    grad = observer.natural_gradient(conjugate_gradient_method_step, conjugate_gradient_method_error,
                                                     metric_inverse_epsilon)
                else:
                    grad = observer.gradient

                # Change state
                if use_check_difference:
                    showln("checking difference")
                    check_difference(state, observer, grad, energy_observer, configuration_pool, check_difference_delta)

                elif use_line_search:
                    showln("line searching")
                    grad *= (state.lattice_dot() / state.lattice_dot(grad, grad))**0.5
                    grad_step_size = line_search(state, observer, grad, energy_observer, configuration_pool,
                                                 grad_step_size, line_search_amplitude, line_search_error_threshold)
                    state._lattice -= grad_step_size * grad
                else:
                    if grad_step == 0 or momentum_parameter == 0.0:
                        total_grad = grad
                    else:
                        if orthogonalize_momentum:
                            total_grad -= state._lattice * (state.lattice_dot(total_grad) / state.lattice_dot())
                        total_grad = total_grad * momentum_parameter + grad * (1 - momentum_parameter)
                    if use_random_gradient:
                        this_grad = lattice_randomize(total_grad)
                    else:
                        this_grad = total_grad
                    if use_fix_relative_step_size:
                        this_grad *= (state.lattice_dot() / state.lattice_dot(this_grad, this_grad))**0.5
                    state._lattice -= grad_step_size * this_grad
                showln(f"grad {grad_step}/{grad_total_step}, step_size={grad_step_size}")

                # Fix gauge
                if fix_gauge:
                    state.expand_dimension(1.0, 0)
                # Normalize state
                observer.normalize_lattice()
                # Bcast state
                bcast_lattice_buffer(state._lattice)
                # sampling is not needed to refresh since every gradient step will use a new sampling object.

                # Save state
                if save_state_interval and (grad_step + 1) % save_state_interval == 0 and save_state_file:
                    write_to_file(state, save_state_file.replace("%s", str(grad_step)).replace("%t", time_str))
                if save_configuration_file:
                    write_to_file(sampling_configurations, save_configuration_file)
            if sigint_handler():
                break
