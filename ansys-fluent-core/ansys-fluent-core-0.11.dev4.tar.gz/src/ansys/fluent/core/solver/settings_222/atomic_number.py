#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .option import option
from .constant import constant
from .boussinesq import boussinesq
from .coefficients import coefficients
from .number_of_coefficients import number_of_coefficients
from .piecewise_polynomial import piecewise_polynomial
from .nasa_9_piecewise_polynomial import nasa_9_piecewise_polynomial
from .piecewise_linear import piecewise_linear
from .anisotropic import anisotropic
from .orthotropic import orthotropic
from .var_class import var_class
class atomic_number(Group):
    """
    'atomic_number' child.
    """

    fluent_name = "atomic-number"

    child_names = \
        ['option', 'constant', 'boussinesq', 'coefficients',
         'number_of_coefficients', 'piecewise_polynomial',
         'nasa_9_piecewise_polynomial', 'piecewise_linear', 'anisotropic',
         'orthotropic', 'var_class']

    option: option = option
    """
    option child of atomic_number.
    """
    constant: constant = constant
    """
    constant child of atomic_number.
    """
    boussinesq: boussinesq = boussinesq
    """
    boussinesq child of atomic_number.
    """
    coefficients: coefficients = coefficients
    """
    coefficients child of atomic_number.
    """
    number_of_coefficients: number_of_coefficients = number_of_coefficients
    """
    number_of_coefficients child of atomic_number.
    """
    piecewise_polynomial: piecewise_polynomial = piecewise_polynomial
    """
    piecewise_polynomial child of atomic_number.
    """
    nasa_9_piecewise_polynomial: nasa_9_piecewise_polynomial = nasa_9_piecewise_polynomial
    """
    nasa_9_piecewise_polynomial child of atomic_number.
    """
    piecewise_linear: piecewise_linear = piecewise_linear
    """
    piecewise_linear child of atomic_number.
    """
    anisotropic: anisotropic = anisotropic
    """
    anisotropic child of atomic_number.
    """
    orthotropic: orthotropic = orthotropic
    """
    orthotropic child of atomic_number.
    """
    var_class: var_class = var_class
    """
    var_class child of atomic_number.
    """
