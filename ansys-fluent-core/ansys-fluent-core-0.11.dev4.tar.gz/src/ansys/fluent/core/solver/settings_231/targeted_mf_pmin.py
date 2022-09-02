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
class targeted_mf_pmin(Group):
    """
    'targeted_mf_pmin' child.
    """

    fluent_name = "targeted-mf-pmin"

    child_names = \
        ['option', 'value', 'profile_name', 'field_name', 'udf']

    option: option = option
    """
    option child of targeted_mf_pmin.
    """
    value: value = value
    """
    value child of targeted_mf_pmin.
    """
    profile_name: profile_name = profile_name
    """
    profile_name child of targeted_mf_pmin.
    """
    field_name: field_name = field_name
    """
    field_name child of targeted_mf_pmin.
    """
    udf: udf = udf
    """
    udf child of targeted_mf_pmin.
    """
