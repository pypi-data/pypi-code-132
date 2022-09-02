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
class z_displacement_value(Group):
    """
    'z_displacement_value' child.
    """

    fluent_name = "z-displacement-value"

    child_names = \
        ['option', 'value', 'profile_name', 'field_name', 'udf']

    option: option = option
    """
    option child of z_displacement_value.
    """
    value: value = value
    """
    value child of z_displacement_value.
    """
    profile_name: profile_name = profile_name
    """
    profile_name child of z_displacement_value.
    """
    field_name: field_name = field_name
    """
    field_name child of z_displacement_value.
    """
    udf: udf = udf
    """
    udf child of z_displacement_value.
    """
