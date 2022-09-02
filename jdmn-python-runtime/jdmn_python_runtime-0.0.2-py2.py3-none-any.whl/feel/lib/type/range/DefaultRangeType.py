#
# Copyright 2016 Goldman Sachs.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
#
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.
#
from typing import Any

from jdmn.feel.lib.Types import BOOLEAN
from jdmn.feel.lib.type.BaseType import BaseType
from jdmn.runtime.Range import Range


class DefaultRangeType(BaseType):
    def __init__(self):
        BaseType.__init__(self)

    def isRange(self, value: Any) -> bool:
        raise Exception("Not supported yet")

    def rangeValue(self, value: Range) -> Range:
        raise Exception("Not supported yet")

    def rangeIs(self, c1: Any, c2: Any) -> BOOLEAN:
        raise Exception("Not supported yet")

    def rangeEqual(self, c1: Any, c2: Any) -> BOOLEAN:
        raise Exception("Not supported yet")

    def rangeNotEqual(self, c1: Any, c2: Any) -> BOOLEAN:
        raise Exception("Not supported yet")
