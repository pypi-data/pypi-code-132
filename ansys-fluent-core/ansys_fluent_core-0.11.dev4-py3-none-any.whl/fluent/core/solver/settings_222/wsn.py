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
class wsn(Group):
    """
    'wsn' child.
    """

    fluent_name = "wsn"

    child_names = \
        ['option', 'constant', 'profile_name', 'field_name', 'udf']

    option: option = option
    """
    option child of wsn.
    """
    constant: constant = constant
    """
    constant child of wsn.
    """
    profile_name: profile_name = profile_name
    """
    profile_name child of wsn.
    """
    field_name: field_name = field_name
    """
    field_name child of wsn.
    """
    udf: udf = udf
    """
    udf child of wsn.
    """
