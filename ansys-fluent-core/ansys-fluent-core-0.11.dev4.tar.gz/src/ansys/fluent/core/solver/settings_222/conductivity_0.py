#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .option import option
from .constant import constant
from .coefficients import coefficients
from .number_of_coefficients import number_of_coefficients
from .piecewise_linear import piecewise_linear
from .piecewise_polynomial import piecewise_polynomial
class conductivity_0(Group):
    """
    'conductivity_0' child.
    """

    fluent_name = "conductivity-0"

    child_names = \
        ['option', 'constant', 'coefficients', 'number_of_coefficients',
         'piecewise_linear', 'piecewise_polynomial']

    option: option = option
    """
    option child of conductivity_0.
    """
    constant: constant = constant
    """
    constant child of conductivity_0.
    """
    coefficients: coefficients = coefficients
    """
    coefficients child of conductivity_0.
    """
    number_of_coefficients: number_of_coefficients = number_of_coefficients
    """
    number_of_coefficients child of conductivity_0.
    """
    piecewise_linear: piecewise_linear = piecewise_linear
    """
    piecewise_linear child of conductivity_0.
    """
    piecewise_polynomial: piecewise_polynomial = piecewise_polynomial
    """
    piecewise_polynomial child of conductivity_0.
    """
