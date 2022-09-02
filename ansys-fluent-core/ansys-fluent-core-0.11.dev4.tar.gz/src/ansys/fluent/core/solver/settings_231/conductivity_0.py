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
class conductivity_0(Group):
    """
    'conductivity_0' child.
    """

    fluent_name = "conductivity-0"

    child_names = \
        ['option', 'value', 'piecewise_linear', 'piecewise_polynomial',
         'polynomial', 'user_defined_function']

    option: option = option
    """
    option child of conductivity_0.
    """
    value: value = value
    """
    value child of conductivity_0.
    """
    piecewise_linear: piecewise_linear = piecewise_linear
    """
    piecewise_linear child of conductivity_0.
    """
    piecewise_polynomial: piecewise_polynomial = piecewise_polynomial
    """
    piecewise_polynomial child of conductivity_0.
    """
    polynomial: polynomial = polynomial
    """
    polynomial child of conductivity_0.
    """
    user_defined_function: user_defined_function = user_defined_function
    """
    user_defined_function child of conductivity_0.
    """
