#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .option_9 import option
from .value import value
from .profile_name import profile_name
from .field_name import field_name
from .udf import udf
class ocw_ship_vmag(Group):
    """
    'ocw_ship_vmag' child.
    """

    fluent_name = "ocw-ship-vmag"

    child_names = \
        ['option', 'value', 'profile_name', 'field_name', 'udf']

    option: option = option
    """
    option child of ocw_ship_vmag.
    """
    value: value = value
    """
    value child of ocw_ship_vmag.
    """
    profile_name: profile_name = profile_name
    """
    profile_name child of ocw_ship_vmag.
    """
    field_name: field_name = field_name
    """
    field_name child of ocw_ship_vmag.
    """
    udf: udf = udf
    """
    udf child of ocw_ship_vmag.
    """
