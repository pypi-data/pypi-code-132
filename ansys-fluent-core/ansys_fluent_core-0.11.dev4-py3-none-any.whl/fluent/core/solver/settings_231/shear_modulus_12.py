#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .option_8 import option
from .value import value
class shear_modulus_12(Group):
    """
    'shear_modulus_12' child.
    """

    fluent_name = "shear-modulus-12"

    child_names = \
        ['option', 'value']

    option: option = option
    """
    option child of shear_modulus_12.
    """
    value: value = value
    """
    value child of shear_modulus_12.
    """
