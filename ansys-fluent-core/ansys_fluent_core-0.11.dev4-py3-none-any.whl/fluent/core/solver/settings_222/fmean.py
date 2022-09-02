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
class fmean(Group):
    """
    'fmean' child.
    """

    fluent_name = "fmean"

    child_names = \
        ['option', 'constant', 'profile_name', 'field_name', 'udf']

    option: option = option
    """
    option child of fmean.
    """
    constant: constant = constant
    """
    constant child of fmean.
    """
    profile_name: profile_name = profile_name
    """
    profile_name child of fmean.
    """
    field_name: field_name = field_name
    """
    field_name child of fmean.
    """
    udf: udf = udf
    """
    udf child of fmean.
    """
