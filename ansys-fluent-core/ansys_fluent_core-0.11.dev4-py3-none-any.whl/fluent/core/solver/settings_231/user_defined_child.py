#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .retain_instantaneous_values import retain_instantaneous_values
from .input_params import input_params
from .function_name import function_name
from .average_over import average_over
from .old_props import old_props
class user_defined_child(Group):
    """
    'child_object_type' of user_defined.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['retain_instantaneous_values', 'input_params', 'function_name',
         'average_over', 'old_props']

    retain_instantaneous_values: retain_instantaneous_values = retain_instantaneous_values
    """
    retain_instantaneous_values child of user_defined_child.
    """
    input_params: input_params = input_params
    """
    input_params child of user_defined_child.
    """
    function_name: function_name = function_name
    """
    function_name child of user_defined_child.
    """
    average_over: average_over = average_over
    """
    average_over child of user_defined_child.
    """
    old_props: old_props = old_props
    """
    old_props child of user_defined_child.
    """
