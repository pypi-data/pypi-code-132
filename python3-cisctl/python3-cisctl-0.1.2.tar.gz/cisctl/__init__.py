# Copyright 2022 xiexianbin.cn
# All Rights Reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#        http://www.apache.org/licenses/LICENSE-2.0
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.

import pbr.version


__all__ = ['__version__']


version_info = pbr.version.VersionInfo('python3-cisctl')
# We have a circular import problem when we first run python setup.py sdist
# It's harmless, so deflect it.
try:
    __version__ = version_info.version_string()
except AttributeError:
    __version__ = None
