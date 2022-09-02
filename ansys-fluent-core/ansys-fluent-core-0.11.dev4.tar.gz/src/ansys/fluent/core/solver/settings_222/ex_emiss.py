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
class ex_emiss(Group):
    """
    'ex_emiss' child.
    """

    fluent_name = "ex-emiss"

    child_names = \
        ['option', 'constant', 'profile_name', 'field_name', 'udf']

    option: option = option
    """
    option child of ex_emiss.
    """
    constant: constant = constant
    """
    constant child of ex_emiss.
    """
    profile_name: profile_name = profile_name
    """
    profile_name child of ex_emiss.
    """
    field_name: field_name = field_name
    """
    field_name child of ex_emiss.
    """
    udf: udf = udf
    """
    udf child of ex_emiss.
    """
