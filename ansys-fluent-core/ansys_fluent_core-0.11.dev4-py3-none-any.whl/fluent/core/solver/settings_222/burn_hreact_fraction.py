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
class burn_hreact_fraction(Group):
    """
    'burn_hreact_fraction' child.
    """

    fluent_name = "burn-hreact-fraction"

    child_names = \
        ['option', 'constant', 'boussinesq', 'coefficients',
         'number_of_coefficients', 'piecewise_polynomial',
         'nasa_9_piecewise_polynomial', 'piecewise_linear', 'anisotropic',
         'orthotropic', 'var_class']

    option: option = option
    """
    option child of burn_hreact_fraction.
    """
    constant: constant = constant
    """
    constant child of burn_hreact_fraction.
    """
    boussinesq: boussinesq = boussinesq
    """
    boussinesq child of burn_hreact_fraction.
    """
    coefficients: coefficients = coefficients
    """
    coefficients child of burn_hreact_fraction.
    """
    number_of_coefficients: number_of_coefficients = number_of_coefficients
    """
    number_of_coefficients child of burn_hreact_fraction.
    """
    piecewise_polynomial: piecewise_polynomial = piecewise_polynomial
    """
    piecewise_polynomial child of burn_hreact_fraction.
    """
    nasa_9_piecewise_polynomial: nasa_9_piecewise_polynomial = nasa_9_piecewise_polynomial
    """
    nasa_9_piecewise_polynomial child of burn_hreact_fraction.
    """
    piecewise_linear: piecewise_linear = piecewise_linear
    """
    piecewise_linear child of burn_hreact_fraction.
    """
    anisotropic: anisotropic = anisotropic
    """
    anisotropic child of burn_hreact_fraction.
    """
    orthotropic: orthotropic = orthotropic
    """
    orthotropic child of burn_hreact_fraction.
    """
    var_class: var_class = var_class
    """
    var_class child of burn_hreact_fraction.
    """
