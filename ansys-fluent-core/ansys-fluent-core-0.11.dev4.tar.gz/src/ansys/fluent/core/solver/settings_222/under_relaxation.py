#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .axis_direction_component_child import axis_direction_component_child

class under_relaxation(NamedObject[axis_direction_component_child], _CreatableNamedObjectMixin[axis_direction_component_child]):
    """
    Enter Under Relaxation Menu.
    """

    fluent_name = "under-relaxation"

    child_object_type: axis_direction_component_child = axis_direction_component_child
    """
    child_object_type of under_relaxation.
    """
