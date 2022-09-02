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
class ir_absp(Group):
    """
    'ir_absp' child.
    """

    fluent_name = "ir-absp"

    child_names = \
        ['option', 'value', 'profile_name', 'field_name', 'udf']

    option: option = option
    """
    option child of ir_absp.
    """
    value: value = value
    """
    value child of ir_absp.
    """
    profile_name: profile_name = profile_name
    """
    profile_name child of ir_absp.
    """
    field_name: field_name = field_name
    """
    field_name child of ir_absp.
    """
    udf: udf = udf
    """
    udf child of ir_absp.
    """
