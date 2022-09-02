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
class nk(Group):
    """
    'nk' child.
    """

    fluent_name = "nk"

    child_names = \
        ['option', 'constant', 'profile_name', 'field_name', 'udf']

    option: option = option
    """
    option child of nk.
    """
    constant: constant = constant
    """
    constant child of nk.
    """
    profile_name: profile_name = profile_name
    """
    profile_name child of nk.
    """
    field_name: field_name = field_name
    """
    field_name child of nk.
    """
    udf: udf = udf
    """
    udf child of nk.
    """
