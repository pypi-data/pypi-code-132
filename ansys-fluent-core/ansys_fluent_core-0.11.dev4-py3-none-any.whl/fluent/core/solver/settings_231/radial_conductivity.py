#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .option_8 import option
from .value import value
from .piecewise_linear import piecewise_linear
from .piecewise_polynomial import piecewise_polynomial
from .polynomial import polynomial
from .user_defined_function import user_defined_function
class radial_conductivity(Group):
    """
    'radial_conductivity' child.
    """

    fluent_name = "radial-conductivity"

    child_names = \
        ['option', 'value', 'piecewise_linear', 'piecewise_polynomial',
         'polynomial', 'user_defined_function']

    option: option = option
    """
    option child of radial_conductivity.
    """
    value: value = value
    """
    value child of radial_conductivity.
    """
    piecewise_linear: piecewise_linear = piecewise_linear
    """
    piecewise_linear child of radial_conductivity.
    """
    piecewise_polynomial: piecewise_polynomial = piecewise_polynomial
    """
    piecewise_polynomial child of radial_conductivity.
    """
    polynomial: polynomial = polynomial
    """
    polynomial child of radial_conductivity.
    """
    user_defined_function: user_defined_function = user_defined_function
    """
    user_defined_function child of radial_conductivity.
    """
