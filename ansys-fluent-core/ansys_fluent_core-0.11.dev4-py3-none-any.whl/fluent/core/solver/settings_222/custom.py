#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .phase_child_10 import phase_child

class custom(NamedObject[phase_child], _CreatableNamedObjectMixin[phase_child]):
    """
    'custom' child.
    """

    fluent_name = "custom"

    child_object_type: phase_child = phase_child
    """
    child_object_type of custom.
    """
