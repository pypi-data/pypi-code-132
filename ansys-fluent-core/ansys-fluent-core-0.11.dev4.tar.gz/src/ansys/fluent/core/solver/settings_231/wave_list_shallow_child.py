#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .theory import theory
from .wave_ht import wave_ht
from .wave_len import wave_len
from .offset_1 import offset
from .heading_angle import heading_angle
class wave_list_shallow_child(Group):
    """
    'child_object_type' of wave_list_shallow.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['theory', 'wave_ht', 'wave_len', 'offset', 'heading_angle']

    theory: theory = theory
    """
    theory child of wave_list_shallow_child.
    """
    wave_ht: wave_ht = wave_ht
    """
    wave_ht child of wave_list_shallow_child.
    """
    wave_len: wave_len = wave_len
    """
    wave_len child of wave_list_shallow_child.
    """
    offset: offset = offset
    """
    offset child of wave_list_shallow_child.
    """
    heading_angle: heading_angle = heading_angle
    """
    heading_angle child of wave_list_shallow_child.
    """
