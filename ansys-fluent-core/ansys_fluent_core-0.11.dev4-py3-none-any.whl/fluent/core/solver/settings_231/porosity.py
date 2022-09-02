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
class porosity(Group):
    """
    'porosity' child.
    """

    fluent_name = "porosity"

    child_names = \
        ['option', 'value', 'profile_name', 'field_name', 'udf']

    option: option = option
    """
    option child of porosity.
    """
    value: value = value
    """
    value child of porosity.
    """
    profile_name: profile_name = profile_name
    """
    profile_name child of porosity.
    """
    field_name: field_name = field_name
    """
    field_name child of porosity.
    """
    udf: udf = udf
    """
    udf child of porosity.
    """
