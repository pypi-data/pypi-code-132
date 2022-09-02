#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .option import option
from .constant import constant
from .profile_name import profile_name
from .field_name import field_name
from .udf import udf
class dp_profile(Group):
    """
    'dp_profile' child.
    """

    fluent_name = "dp-profile"

    child_names = \
        ['option', 'constant', 'profile_name', 'field_name', 'udf']

    option: option = option
    """
    option child of dp_profile.
    """
    constant: constant = constant
    """
    constant child of dp_profile.
    """
    profile_name: profile_name = profile_name
    """
    profile_name child of dp_profile.
    """
    field_name: field_name = field_name
    """
    field_name child of dp_profile.
    """
    udf: udf = udf
    """
    udf child of dp_profile.
    """
