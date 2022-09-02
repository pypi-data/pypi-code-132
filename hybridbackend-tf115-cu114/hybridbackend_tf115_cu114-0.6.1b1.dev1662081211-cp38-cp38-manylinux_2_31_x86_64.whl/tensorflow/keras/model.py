# Copyright 2021 Alibaba Group Holding Limited. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

r'''Utilities of keras.Model using hybrid backends.
'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import threading

import numpy as np
from tensorflow.core.protobuf import config_pb2

try:
  from tensorflow.python.distribute import distribution_strategy_context
except ImportError:
  distribution_strategy_context = None
from tensorflow.python.framework import ops
from tensorflow.python.keras import backend as K
from tensorflow.python.keras import callbacks
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.engine import training as _keras_training
from tensorflow.python.keras.engine import training_arrays as _training_arrays
from tensorflow.python.keras.engine import training_utils as _training_utils
from tensorflow.python.ops import state_ops
from tensorflow.python.platform import tf_logging as logging
from tensorflow.python.saved_model import signature_constants
from tensorflow.python.training import basic_session_run_hooks
from tensorflow.python.training import checkpoint_management
from tensorflow.python.training import session_run_hook
from tensorflow.python.training import training_util

try:
  from tensorflow.python.training.tracking import base as trackable
except ImportError:
  trackable = None
from tensorflow.python.util import nest

from hybridbackend.tensorflow.data.iterators import make_one_shot_iterator
from hybridbackend.tensorflow.framework.context import Context
from hybridbackend.tensorflow.framework.context import context_scope
from hybridbackend.tensorflow.framework.device import device_function
from hybridbackend.tensorflow.framework.ops import ModeKeys
from hybridbackend.tensorflow.training.saved_model import export_all
from hybridbackend.tensorflow.training.server import monitored_session


class PatchGetSessionForKerasModel(object):  # pylint: disable=useless-object-inheritance
  r'''Context manager that patches TF APIs for `keras.Model`.
  '''
  _lock = threading.Lock()
  _stack_depth = 0
  _sess_map = {}

  def __init__(
      self, name, checkpoint_dir,
      keep_checkpoint_max,
      keep_checkpoint_every_n_hours):
    self._name = name
    self._checkpoint_dir = checkpoint_dir
    self._keep_checkpoint_max = keep_checkpoint_max
    self._keep_checkpoint_every_n_hours = keep_checkpoint_every_n_hours
    PatchGetSessionForKerasModel._sess_map[self._name] = None

  def __enter__(self):
    with PatchGetSessionForKerasModel._lock:
      PatchGetSessionForKerasModel._stack_depth += 1
      if PatchGetSessionForKerasModel._stack_depth <= 1:

        def wraps_get_session(fn):  # pylint: disable=unused-argument
          r'''replace the default session.
          '''

          def wrapped_get_session(op_input_list=()):  # pylint: disable=unused-argument
            if PatchGetSessionForKerasModel._sess_map[self._name] is None:
              PatchGetSessionForKerasModel._sess_map[self._name] \
                = monitored_session(
                  checkpoint_dir=self._checkpoint_dir,
                  save_checkpoint_steps=sys.maxsize,
                  keep_checkpoint_max=self._keep_checkpoint_max,
                  keep_checkpoint_every_n_hours=self.
                  _keep_checkpoint_every_n_hours,
                  log_step_count_steps=None)
            return PatchGetSessionForKerasModel._sess_map[self._name]
          return wrapped_get_session
        self._prev_get_session = K._get_session
        K._get_session = wraps_get_session(self._prev_get_session)

        def wraps_should_trigger_for_step(fn):  # pylint: disable=unused-argument
          r'''handle cases where self._every_steps is set to be sys.maxsize
          '''

          def wrapped_should_trigger_for_step(cls, step):
            if cls._last_triggered_step is None:  # pylint: disable=protected-access
              return True

            if cls._last_triggered_step == step:  # pylint: disable=protected-access
              return False

            if cls._every_secs is not None:  # pylint: disable=protected-access
              if time.time() >= cls._last_triggered_time + cls._every_secs:  # pylint: disable=protected-access
                return True

            if cls._every_steps is not None and cls._every_steps != sys.maxsize:  # pylint: disable=protected-access
              if step >= cls._last_triggered_step + cls._every_steps:  # pylint: disable=protected-access
                return True

            return False
          return wrapped_should_trigger_for_step
        self._prev_should_trigger_for_step = \
          basic_session_run_hooks.SecondOrStepTimer.should_trigger_for_step
        basic_session_run_hooks.SecondOrStepTimer.should_trigger_for_step = \
          wraps_should_trigger_for_step(self._prev_should_trigger_for_step)

        def decorate_call_fn(fn):
          r'''decorete the __call__ fo GraphExecutionFunction
          '''
          def decorated(cls, inputs):
            sess = K._get_session(inputs)._sess._sess._sess  # pylint: disable=protected-access

            if sess.should_stop():
              raise RuntimeError('Run called even after should_stop requested.')
            actual_fetches = {}
            run_context = session_run_hook.SessionRunContext(
              original_args=session_run_hook.SessionRunArgs(
                [], None),
              session=sess._sess)  # pylint: disable=protected-access

            options = config_pb2.RunOptions()
            feed_dict = sess._call_hook_before_run(  # pylint: disable=protected-access
              run_context, actual_fetches, None, options)
            run_metadata = config_pb2.RunMetadata()
            ret = fn(cls, inputs)
            outputs = sess._sess.run(  # pylint: disable=protected-access
              fetches=actual_fetches,
              feed_dict=feed_dict,
              options=options,
              run_metadata=run_metadata)
            for hook in sess._hooks:  # pylint: disable=protected-access
              hook.after_run(
                run_context,
                session_run_hook.SessionRunValues(
                  results=outputs[hook] if hook in outputs else None,
                  options=options,
                  run_metadata=run_metadata))
            sess._should_stop = sess._should_stop or run_context.stop_requested  # pylint: disable=protected-access
            return ret
          return decorated
        self._prev_call_fn = K.GraphExecutionFunction.__call__
        K.GraphExecutionFunction.__call__ = decorate_call_fn(self._prev_call_fn)

      return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    with PatchGetSessionForKerasModel._lock:
      if PatchGetSessionForKerasModel._stack_depth <= 1:
        K._get_session = self._prev_get_session
        PatchGetSessionForKerasModel._sess_map[self._name] = None
        K.GraphExecutionFunction.__call__ = self._prev_call_fn
        basic_session_run_hooks.SecondOrStepTimer.should_trigger_for_step = \
          self._prev_should_trigger_for_step
      PatchGetSessionForKerasModel._stack_depth -= 1


class PatchGetIteratorForKerasModel(object):  # pylint: disable=useless-object-inheritance
  r'''Context manager that patches TF APIs for `keras.Model`.
  '''
  _lock = threading.Lock()
  _stack_depth = 0

  def __init__(self, drop_remainder):
    self._drop_remainder = drop_remainder

  def __enter__(self):
    with PatchGetIteratorForKerasModel._lock:
      PatchGetIteratorForKerasModel._stack_depth += 1
      if PatchGetIteratorForKerasModel._stack_depth <= 1:
        def wraps_get_iterator(iterator_fn):  # pylint: disable=unused-argument
          r'''replaces iterator.
          '''
          def wrapped_get_iterator(dataset):
            return make_one_shot_iterator(dataset, self._drop_remainder)
          return wrapped_get_iterator
        self._prev_get_iterator = _training_utils.get_iterator
        _training_utils.get_iterator = wraps_get_iterator(
          self._prev_get_iterator)

      return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    with PatchGetIteratorForKerasModel._lock:
      if PatchGetIteratorForKerasModel._stack_depth <= 1:
        _training_utils.get_iterator = self._prev_get_iterator
      PatchGetIteratorForKerasModel._stack_depth -= 1


class PatchCallbacksForKerasModel(object):  # pylint: disable=useless-object-inheritance
  r'''Context manager that patches CallbackList of `keras.Model`.
  '''
  _lock = threading.Lock()
  _stack_depth = 0

  def __init__(self, mode, monitor, save_best_only, save_best_mode):
    self._mode = mode
    self._monitor = monitor
    self._save_best_only = save_best_only
    self._save_best_mode = save_best_mode
    if self._save_best_mode not in ['auto', 'min', 'max']:
      logging.warning(f'Checkpoint save best mode {self._save_best_mode} '
                      'is unknown, fallback to auto mode.')
      self._save_best_mode = 'auto'

    if self._save_best_mode == 'min':
      self._monitor_op = np.less
      self._best = np.Inf
    elif self._save_best_mode == 'max':
      self._monitor_op = np.greater
      self._best = -np.Inf
    else:
      if 'acc' in self._monitor or self._monitor.startswith('fmeasure'):
        self._monitor_op = np.greater
        self._best = -np.Inf
      else:
        self._monitor_op = np.less
        self._best = np.Inf

  def _save_model(self):
    sess = K._get_session()  # pylint: disable=protected-access
    for h in sess._hooks:  # pylint: disable=protected-access
      if isinstance(h, basic_session_run_hooks.CheckpointSaverHook):
        tf_sess = sess._coordinated_creator.tf_sess  # pylint: disable=protected-access
        last_step = tf_sess.run(h._global_step_tensor)  # pylint: disable=protected-access
        if last_step != h._timer.last_triggered_step():  # pylint: disable=protected-access
          h._save(tf_sess, last_step)  # pylint: disable=protected-access

  def _close_hooks(self):
    sess = K._get_session()  # pylint: disable=protected-access
    for h in sess._hooks:  # pylint: disable=protected-access
      if not isinstance(h, basic_session_run_hooks.CheckpointSaverHook):
        h.end(sess._coordinated_creator.tf_sess)  # pylint: disable=protected-access
      else:
        tf_sess = sess._coordinated_creator.tf_sess  # pylint: disable=protected-access
        last_step = tf_sess.run(h._global_step_tensor)  # pylint: disable=protected-access
        for lsn in h._listeners:  # pylint: disable=protected-access
          lsn.end(tf_sess, last_step)

  def __enter__(self):
    with PatchCallbacksForKerasModel._lock:
      PatchCallbacksForKerasModel._stack_depth += 1
      if PatchCallbacksForKerasModel._stack_depth <= 1:
        def wraps_on_epoch_end(fn):
          r'''trigger CheckpointSaverHook at the end of each.
          '''

          def wrapped_on_epoch_end(cks, epoch, logs=None):
            r''' trigger the end of CheckpointSaverHook.
            '''
            if self._save_best_only:
              logs = logs or {}
              current = logs.get(self._monitor)
              if current is None:
                logging.warning('Can save best model only with '
                                f'{self._monitor} available, '
                                'skipping.')
              elif self._monitor_op(current, self._best):
                logging.warning(
                  f'\nEpoch {epoch + 1} {self._monitor} improved '
                  f'from {self._best} to {current} '
                  'saving model')
                self._best = current
                self._save_model()
              else:
                logging.warning(f'\nEpoch {epoch + 1} {self._monitor} '
                                f'did not improve from {self._best}')
            else:
              self._save_model()
            fn(cks, epoch, logs)
          return wrapped_on_epoch_end
        self._prev_on_epoch_end = callbacks.CallbackList.on_epoch_end
        callbacks.CallbackList.on_epoch_end = wraps_on_epoch_end(
          self._prev_on_epoch_end)

        def wraps_call_end_hook(fn):
          r'''trigger session hook end methods
          '''

          def wrapped_call_end_hook(cks, mode, *args, **kwargs):
            r'''trigger the end() method for each hooks of session.
            '''
            fn(cks, mode, *args, **kwargs)
            if self._mode == ModeKeys.TRAIN and mode == ModeKeys.TRAIN:
              self._close_hooks()
          return wrapped_call_end_hook
        self._prev_call_end_hook = callbacks.CallbackList._call_end_hook
        callbacks.CallbackList._call_end_hook = wraps_call_end_hook(
          self._prev_call_end_hook)
      return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    with PatchCallbacksForKerasModel._lock:
      if PatchCallbacksForKerasModel._stack_depth <= 1:
        callbacks.CallbackList.on_epoch_end = self._prev_on_epoch_end
        callbacks.CallbackList._call_end_hook = self._prev_call_end_hook
      PatchCallbacksForKerasModel._stack_depth -= 1


class PatchTensorflowAPIForKerasModel(object):  # pylint: disable=useless-object-inheritance
  r'''Context manager that patches TF APIs for `keras.Model`.
  '''
  _lock = threading.Lock()
  _stack_depth = 0

  def __init__(
      self, checkpoint_dir=None,
      keep_checkpoint_max=None,
      keep_checkpoint_every_n_hours=None,
      mode=None,
      monitor=None,
      save_best_only=None,
      save_best_mode=None):
    self._checkpoint_dir = checkpoint_dir
    self._keep_checkpoint_max = keep_checkpoint_max
    self._keep_checkpoint_every_n_hours = keep_checkpoint_every_n_hours
    self._mode = mode
    self._monitor = monitor
    self._save_best_only = save_best_only
    self._save_best_mode = save_best_mode

  def __enter__(self):
    with PatchTensorflowAPIForKerasModel._lock:
      PatchTensorflowAPIForKerasModel._stack_depth += 1
      if PatchTensorflowAPIForKerasModel._stack_depth <= 1:
        K.manual_variable_initialization(True)

        def wraps_model_iteration(fn):
          r'''replace the default model_iteration.
          '''

          def wrapped_model_iteration(*args, **kwargs):
            with PatchGetSessionForKerasModel(
                self._mode, self._checkpoint_dir,
                self._keep_checkpoint_max,
                self._keep_checkpoint_every_n_hours):
              with PatchCallbacksForKerasModel(
                  self._mode,
                  self._monitor,
                  self._save_best_only,
                  self._save_best_mode):
                return fn(*args, **kwargs)
          return wrapped_model_iteration
        self._prev_fit_loop = _training_arrays.fit_loop
        self._prev_test_loop = _training_arrays.test_loop
        _training_arrays.fit_loop = wraps_model_iteration(
          self._prev_fit_loop)
        _training_arrays.test_loop = wraps_model_iteration(
          self._prev_test_loop)

      return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    with PatchTensorflowAPIForKerasModel._lock:
      if PatchTensorflowAPIForKerasModel._stack_depth <= 1:
        K.manual_variable_initialization(False)
        _training_arrays.fit_loop = self._prev_fit_loop
        _training_arrays.test_loop = self._prev_test_loop
      PatchTensorflowAPIForKerasModel._stack_depth -= 1


def wraps_keras_model(cls):
  r'''Wrap up a keras model.
  '''
  if trackable is None:
    return None

  class HybridBackendKerasModel(cls):
    r'''Class to train and evaluate TensorFlow models.
    '''
    def __init__(self, *args, **kwargs):
      self._device_fn = device_function
      self._train_drop_remainder = kwargs.pop('train_drop_remainder', None)
      self._eval_drop_remainder = kwargs.pop('eval_drop_remainder', None)
      self._predict_drop_remainder = kwargs.pop('predict_drop_remainder', None)

      with PatchTensorflowAPIForKerasModel():
        super().__init__(*args, **kwargs)

    @trackable.no_automatic_dependency_tracking
    def compile(self,
                optimizer='rmsprop',
                loss=None,
                metrics=None,
                loss_weights=None,
                sample_weight_mode=None,
                weighted_metrics=None,
                target_tensors=None,
                distribute=None,
                **kwargs):
      r'''Configures the model for training.
      '''
      self._run_eagerly = kwargs.pop('run_eagerly', None)
      self._experimental_run_tf_function = kwargs.pop(
        'experimental_run_tf_function', True)
      self._set_optimizer(optimizer)
      is_any_optimizer_v1 = any(isinstance(opt, optimizers.Optimizer)
                                for opt in nest.flatten(self.optimizer))
      if ((sample_weight_mode is not None)
          or (target_tensors is not None)
          or is_any_optimizer_v1
          or not ops.executing_eagerly_outside_functions()):
        # Fallback out of things that aren't supported with v2 loops
        self._experimental_run_tf_function = False
      else:
        raise ValueError('V2 loops is not supported in HybridBackend')

      if (distribute is not None
          or (
            distribution_strategy_context is not None
            and distribution_strategy_context.has_strategy())):
        raise RuntimeError(
          'Running `keras.Model` with distributed strategy is not supported')
      if (trackable is not None
          and isinstance(self.optimizer, trackable.Trackable)):
        self._track_trackable(
          self.optimizer, name='optimizer', overwrite=True)
      self.loss = loss or {}
      self.loss_weights = loss_weights
      self.sample_weight_mode = sample_weight_mode
      self._compile_metrics = metrics or []
      self._compile_weighted_metrics = weighted_metrics
      self._training_endpoints = []

      # Used to freeze the behavior of the Model once `compile` has been called.
      self._compiled_trainable_state = self._get_trainable_state()

      # Set tf.distribute.Strategy specific parameters.
      self._distributed_model_cache = {}
      self._distributed_function_cache = {}

      # Clear any `_eager_losses` that was added.
      self._clear_losses()

      self._init_metric_attributes()
      if not self.built or not self.inputs or not self.outputs:
        return
      self._is_compiled = True
      _keras_training._keras_api_gauge.get_cell('compile').set(True)  # pylint: disable=protected-access
      self.loss_functions = _training_utils.prepare_loss_functions(
        self.loss, self.output_names)

      target_tensors = self._process_target_tensor_for_compile(target_tensors)

      for o, n, l, t in zip(self.outputs, self.output_names,
                            self.loss_functions, target_tensors):
        endpoint = _keras_training._TrainingEndpoint(o, n, l)  # pylint: disable=protected-access
        endpoint.create_training_target(t, run_eagerly=self.run_eagerly)
        self._training_endpoints.append(endpoint)

      # Prepare list loss weights, same size of model outputs.
      _training_utils.prepare_loss_weights(
        self._training_endpoints, loss_weights)

      with K.get_graph().as_default() as g, g.device(self._device_fn):
        # Save all metric attributes per output of the model.
        self._cache_output_metric_attributes(metrics, weighted_metrics)

        # Set metric attributes on model.
        self._set_metric_attributes()

        # Invoke metric functions (unweighted) for all the outputs.
        self._handle_metrics(
          self.outputs,
          targets=self._targets,
          skip_target_masks=self._prepare_skip_target_masks(),
          masks=self._prepare_output_masks())

        _training_utils.prepare_sample_weight_modes(
          self._training_endpoints, sample_weight_mode)

        # Creates the model loss and weighted metrics sub-graphs.
        self._compile_weights_loss_and_weighted_metrics()

        # Functions for train, test and predict will
        # be compiled lazily when required.
        # This saves time when the user is not using all functions.
        self._function_kwargs = kwargs

        self.train_function = None
        self.test_function = None
        self.predict_function = None

        # add variables
        global_vars = ops.get_default_graph().get_collection_ref(
          ops.GraphKeys.GLOBAL_VARIABLES)
        trainable_vars = ops.get_default_graph().get_collection_ref(
          ops.GraphKeys.TRAINABLE_VARIABLES)
        for var in global_vars:
          K.track_variable(var)
          if var in trainable_vars:
            self._trainable_weights.append(var)
          else:
            self._non_trainable_weights.append(var)
        # Collected trainable weights, sorted in topological order.
        self._collected_trainable_weights = self._unique_trainable_weights

    def fit(self, *args, **kwargs):
      r'''Trains the model for a fixed number of epochs
        (iterations on a dataset).
      '''
      self._checkpoint_dir = kwargs.pop('checkpoint_dir', None)
      self._keep_checkpoint_max = kwargs.pop('keep_checkpoint_max', None)
      self._keep_checkpoint_every_n_hours = kwargs.pop(
        'keep_checkpoint_every_n_hours', None)
      self._monitor = kwargs.pop('monitor', 'val_loss')
      self._save_best_only = kwargs.pop('save_best_only', False)
      self._save_best_mode = kwargs.pop('mode', 'auto')
      if self._save_best_only:
        self._keep_checkpoint_max = 1
      with context_scope(mode=ModeKeys.TRAIN):
        with PatchTensorflowAPIForKerasModel(
            checkpoint_dir=self._checkpoint_dir,
            keep_checkpoint_max=self._keep_checkpoint_max,
            keep_checkpoint_every_n_hours=self._keep_checkpoint_every_n_hours,
            mode=ModeKeys.TRAIN,
            monitor=self._monitor,
            save_best_only=self._save_best_only,
            save_best_mode=self._save_best_mode):
          with PatchGetIteratorForKerasModel(self._train_drop_remainder):
            super().fit(*args, **kwargs)

    def evaluate(self, *args, **kwargs):
      r'''Returns the loss value & metrics values for the model in test mode.
      '''
      with context_scope(
          mode=ModeKeys.EVAL,
          comm_pool_capacity=1,
          comm_pool_name=ModeKeys.EVAL):
        with PatchTensorflowAPIForKerasModel(mode=ModeKeys.EVAL):
          with PatchGetIteratorForKerasModel(self._eval_drop_remainder):
            super().evaluate(*args, **kwargs)

    def reset_metrics(self):
      r'''Resets the state of metrics.
      '''
      metrics = self._get_training_eval_metrics()
      if K.get_graph()._finalized:  # pylint: disable=protected-access
        K.get_graph()._unsafe_unfinalize()  # pylint: disable=protected-access
      for m in metrics:
        m.reset_states()

    def save(
        self,
        filepath,
        overwrite=True,
        include_optimizer=True,
        save_format=None,
        signatures=None):
      r'''Saves the model to Tensorflow SavedModel.
      '''
      raise RuntimeError(
        'Only SavedModel is supported, please use export_saved_model instead')

    def export_saved_model(
        self,
        saved_model_path,
        signature_def_fn,
        checkpoint_path=None,
        custom_objects=None,
        as_text=False,
        **kwargs):
      r'''Exports to a SavedModel.
      '''
      if Context.get().rank != 0:
        return None

      if not checkpoint_path:
        latest_path = checkpoint_management.latest_checkpoint(
          self._checkpoint_dir)  # pylint: disable=protected-access
        if not latest_path:
          raise ValueError(
            f'Could not find trained model in '
            f'model_dir: {self._checkpoint_dir}.')  # pylint: disable=protected-access
        checkpoint_path = latest_path

      return export_all(
        saved_model_path,
        checkpoint_path,
        lambda: {signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY:
                 signature_def_fn()},
        assets_extra=custom_objects,
        as_text=as_text,
        clear_devices=True,
        strip_default_attrs=True,
        modes=[ModeKeys.PREDICT],
        **kwargs)

    def _make_train_function(self):
      r'''Build graph for training.
      '''
      has_recompiled = self._recompile_weights_loss_and_weighted_metrics()
      self._check_trainable_weights_consistency()
      if isinstance(self.optimizer, list):
        raise ValueError('The `optimizer` in `compile` should be a single '
                         'optimizer.')
      # If we have re-compiled the loss/weighted metric sub-graphs then create
      # train function even if one exists already. This is because
      # `_feed_sample_weights` list has been updated on re-copmpile.
      if getattr(self, 'train_function', None) is None or has_recompiled:
        # Restore the compiled trainable state.
        current_trainable_state = self._get_trainable_state()
        self._set_trainable_state(self._compiled_trainable_state)

        inputs = (self._feed_inputs
                  + self._feed_targets
                  + self._feed_sample_weights)
        if not isinstance(K.symbolic_learning_phase(), int):
          inputs += [K.symbolic_learning_phase()]

        if K.get_graph()._finalized:  # pylint: disable=protected-access
          K.get_graph()._unsafe_unfinalize()  # pylint: disable=protected-access
        with K.get_graph().as_default() as g, g.device(self._device_fn):
          with K.name_scope('training'):
            # Training updates
            updates = self.optimizer.get_updates(
              params=self._collected_trainable_weights, loss=self.total_loss)
            # Unconditional updates
            updates += self.get_updates_for(None)
            # Conditional updates relevant to this model
            updates += self.get_updates_for(self.inputs)
            global_step = training_util.get_or_create_global_step()
            updates += [state_ops.assign_add(global_step, 1)]

          metrics = self._get_training_eval_metrics()
          metrics_tensors = [
            m._call_result for m in metrics if hasattr(m, '_call_result')  # pylint: disable=protected-access
          ]

        with K.name_scope('training'):
          # Gets loss and metrics. Updates weights at each call.
          fn = K.function(
            inputs, [self.total_loss] + metrics_tensors,
            updates=updates,
            name='train_function',
            **self._function_kwargs)
          setattr(self, 'train_function', fn)

        # Restore the current trainable state
        self._set_trainable_state(current_trainable_state)

    def _prepare_validation_data(self, *args, **kwargs):
      with PatchGetIteratorForKerasModel(self._eval_drop_remainder):
        return super()._prepare_validation_data(*args, **kwargs)

    def _make_test_function(self):
      r'''Build graph for testing.
      '''
      has_recompiled = self._recompile_weights_loss_and_weighted_metrics()
      # If we have re-compiled the loss/weighted metric sub-graphs then create
      # test function even if one exists already. This is because
      # `_feed_sample_weights` list has been updated on re-copmpile.
      if getattr(self, 'test_function', None) is None or has_recompiled:
        inputs = (self._feed_inputs
                  + self._feed_targets
                  + self._feed_sample_weights)
        if K.get_graph()._finalized:  # pylint: disable=protected-access
          K.get_graph()._unsafe_unfinalize()  # pylint: disable=protected-access
        with K.get_graph().as_default() as g, g.device(self._device_fn):
          metrics = self._get_training_eval_metrics()
          metrics_tensors = [
            m._call_result for m in metrics if hasattr(m, '_call_result')  # pylint: disable=protected-access
          ]

        with K.name_scope('evaluation'):
          updates = self.state_updates
          # Return loss and metrics, no gradient updates.
          # Does update the network states.
          fn = K.function(
            inputs, [self.total_loss] + metrics_tensors,
            updates=updates,
            name='test_function',
            **self._function_kwargs)
          setattr(self, 'test_function', fn)

  return HybridBackendKerasModel


Model = wraps_keras_model(_keras_training.Model)
