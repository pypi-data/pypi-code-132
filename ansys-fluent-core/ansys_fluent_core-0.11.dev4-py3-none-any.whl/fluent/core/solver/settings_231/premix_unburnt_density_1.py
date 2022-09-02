#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .user_defined_function import user_defined_function
from .option_8 import option
from .var_class import var_class
class premix_unburnt_density(Group):
    """
    'premix_unburnt_density' child.
    """

    fluent_name = "premix-unburnt-density"

    child_names = \
        ['user_defined_function', 'option', 'var_class']

    user_defined_function: user_defined_function = user_defined_function
    """
    user_defined_function child of premix_unburnt_density.
    """
    option: option = option
    """
    option child of premix_unburnt_density.
    """
    var_class: var_class = var_class
    """
    var_class child of premix_unburnt_density.
    """
