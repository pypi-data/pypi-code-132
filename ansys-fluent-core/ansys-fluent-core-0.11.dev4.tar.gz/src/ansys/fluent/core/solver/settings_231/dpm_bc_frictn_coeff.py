#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .method_1 import method
from .number_of_coeff import number_of_coeff
from .function_of import function_of
from .coefficients_1 import coefficients
from .constant import constant
from .piecewise_polynomial_1 import piecewise_polynomial
from .piecewise_linear import piecewise_linear
class dpm_bc_frictn_coeff(Group):
    """
    'dpm_bc_frictn_coeff' child.
    """

    fluent_name = "dpm-bc-frictn-coeff"

    child_names = \
        ['method', 'number_of_coeff', 'function_of', 'coefficients',
         'constant', 'piecewise_polynomial', 'piecewise_linear']

    method: method = method
    """
    method child of dpm_bc_frictn_coeff.
    """
    number_of_coeff: number_of_coeff = number_of_coeff
    """
    number_of_coeff child of dpm_bc_frictn_coeff.
    """
    function_of: function_of = function_of
    """
    function_of child of dpm_bc_frictn_coeff.
    """
    coefficients: coefficients = coefficients
    """
    coefficients child of dpm_bc_frictn_coeff.
    """
    constant: constant = constant
    """
    constant child of dpm_bc_frictn_coeff.
    """
    piecewise_polynomial: piecewise_polynomial = piecewise_polynomial
    """
    piecewise_polynomial child of dpm_bc_frictn_coeff.
    """
    piecewise_linear: piecewise_linear = piecewise_linear
    """
    piecewise_linear child of dpm_bc_frictn_coeff.
    """
