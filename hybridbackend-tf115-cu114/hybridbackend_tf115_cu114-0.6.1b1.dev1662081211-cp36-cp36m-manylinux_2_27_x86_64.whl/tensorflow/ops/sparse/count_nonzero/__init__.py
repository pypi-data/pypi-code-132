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

r'''Sparse count nonzero related classes and functions.
'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os as _os


def disable_optimization():
  r'''Disable optimizations for sparse count nonzero on GPU.
  '''
  _os.environ['HB_OP_SPARSE_COUNT_NONZERO_OPTIMIZATION_DISABLED'] = '1'


def enable_optimization(logging_level=None):
  r'''Enable optimizations for sparse count nonzero on GPU.

  Args:
    logging_level: Level of details to optimize operators.
  '''
  _os.environ['HB_OP_SPARSE_COUNT_NONZERO_OPTIMIZATION_DISABLED'] = '0'
  if logging_level is not None:
    if 'TF_CPP_VMODULE' not in _os.environ:
      _os.environ['TF_CPP_VMODULE'] = ''
    if _os.environ['TF_CPP_VMODULE']:
      _os.environ['TF_CPP_VMODULE'] += ','
    _os.environ['TF_CPP_VMODULE'] += (
      f'optimize_sparse_count_nonzero={logging_level}')
