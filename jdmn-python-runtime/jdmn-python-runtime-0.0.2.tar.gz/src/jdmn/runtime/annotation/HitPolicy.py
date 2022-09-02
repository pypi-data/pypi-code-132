#
# Copyright 2016 Goldman Sachs.
#
# Licensed under the Apache License, Version 2.0 (the "License") you may not use self file except in compliance with the License.
#
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.
#
from enum import Enum


class HitPolicy(Enum):
    UNIQUE = "UNIQUE"
    FIRST = "FIRST"
    PRIORITY = "PRIORITY"
    ANY = "ANY"
    COLLECT = "COLLECT"
    RULE_ORDER = "RULE ORDER"
    OUTPUT_ORDER = "OUTPUT ORDER"
    UNKNOWN = "UNKNOWN"

    def __new__(cls, *args, **kwds):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, name):
        self.displayName = name

    def fromName(self, name: str) -> 'HitPolicy':
        for policy in HitPolicy:
            if policy.displayName == name:
                return policy
        return self.UNKNOWN
