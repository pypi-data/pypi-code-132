#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .change_type import change_type
from .axis_child import axis_child

class overset(NamedObject[axis_child], _CreatableNamedObjectMixin[axis_child]):
    """
    'overset' child.
    """

    fluent_name = "overset"

    command_names = \
        ['change_type']

    change_type: change_type = change_type
    """
    change_type command of overset.
    """
    child_object_type: axis_child = axis_child
    """
    child_object_type of overset.
    """
