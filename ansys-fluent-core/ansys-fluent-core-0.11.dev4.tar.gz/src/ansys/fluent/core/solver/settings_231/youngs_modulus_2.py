#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .option_8 import option
from .value import value
class youngs_modulus_2(Group):
    """
    'youngs_modulus_2' child.
    """

    fluent_name = "youngs-modulus-2"

    child_names = \
        ['option', 'value']

    option: option = option
    """
    option child of youngs_modulus_2.
    """
    value: value = value
    """
    value child of youngs_modulus_2.
    """
