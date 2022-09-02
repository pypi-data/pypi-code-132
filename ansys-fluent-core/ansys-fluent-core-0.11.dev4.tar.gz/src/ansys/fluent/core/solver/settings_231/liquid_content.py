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
class liquid_content(Group):
    """
    'liquid_content' child.
    """

    fluent_name = "liquid-content"

    child_names = \
        ['option', 'value', 'profile_name', 'field_name', 'udf']

    option: option = option
    """
    option child of liquid_content.
    """
    value: value = value
    """
    value child of liquid_content.
    """
    profile_name: profile_name = profile_name
    """
    profile_name child of liquid_content.
    """
    field_name: field_name = field_name
    """
    field_name child of liquid_content.
    """
    udf: udf = udf
    """
    udf child of liquid_content.
    """
