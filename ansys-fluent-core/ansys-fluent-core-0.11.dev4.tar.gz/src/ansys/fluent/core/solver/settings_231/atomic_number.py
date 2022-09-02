#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .value import value
from .option_8 import option
from .var_class import var_class
class atomic_number(Group):
    """
    'atomic_number' child.
    """

    fluent_name = "atomic-number"

    child_names = \
        ['value', 'option', 'var_class']

    value: value = value
    """
    value child of atomic_number.
    """
    option: option = option
    """
    option child of atomic_number.
    """
    var_class: var_class = var_class
    """
    var_class child of atomic_number.
    """
