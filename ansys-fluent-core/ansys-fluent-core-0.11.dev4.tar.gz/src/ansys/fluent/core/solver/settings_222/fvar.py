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
class fvar(Group):
    """
    'fvar' child.
    """

    fluent_name = "fvar"

    child_names = \
        ['option', 'constant', 'profile_name', 'field_name', 'udf']

    option: option = option
    """
    option child of fvar.
    """
    constant: constant = constant
    """
    constant child of fvar.
    """
    profile_name: profile_name = profile_name
    """
    profile_name child of fvar.
    """
    field_name: field_name = field_name
    """
    field_name child of fvar.
    """
    udf: udf = udf
    """
    udf child of fvar.
    """
