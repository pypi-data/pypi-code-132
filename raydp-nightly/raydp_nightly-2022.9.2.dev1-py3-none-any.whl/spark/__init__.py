#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from .dataset import spark_dataframe_to_ray_dataset, \
                     ray_dataset_to_spark_dataframe
from .interfaces import SparkEstimatorInterface
from .ray_cluster import SparkCluster

__all__ = [
  "SparkCluster",
  "SparkEstimatorInterface",
  "spark_dataframe_to_ray_dataset",
  "ray_dataset_to_spark_dataframe"
]

try:
    import ray.util.data
    from .dataset import RayMLDataset
    __all__.append("RayMLDataset")
except ImportError:
    # Ray MLDataset is removed in Ray 2.0
    pass
