#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .enable_5 import enable
from .options_4 import options
class multi_phase_setting(Group):
    """
    'multi_phase_setting' child.
    """

    fluent_name = "multi-phase-setting"

    child_names = \
        ['enable', 'options']

    enable: enable = enable
    """
    enable child of multi_phase_setting.
    """
    options: options = options
    """
    options child of multi_phase_setting.
    """
