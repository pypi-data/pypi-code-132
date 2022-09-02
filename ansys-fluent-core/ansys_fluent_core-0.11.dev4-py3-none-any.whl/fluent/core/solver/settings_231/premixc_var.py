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
class premixc_var(Group):
    """
    'premixc_var' child.
    """

    fluent_name = "premixc-var"

    child_names = \
        ['option', 'value', 'profile_name', 'field_name', 'udf']

    option: option = option
    """
    option child of premixc_var.
    """
    value: value = value
    """
    value child of premixc_var.
    """
    profile_name: profile_name = profile_name
    """
    profile_name child of premixc_var.
    """
    field_name: field_name = field_name
    """
    field_name child of premixc_var.
    """
    udf: udf = udf
    """
    udf child of premixc_var.
    """
