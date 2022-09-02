#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .geom_disable import geom_disable
from .geom_dir_spec import geom_dir_spec
from .geom_dir_x import geom_dir_x
from .geom_dir_y import geom_dir_y
from .geom_dir_z import geom_dir_z
from .geom_levels import geom_levels
from .geom_bgthread import geom_bgthread
from .angular import angular
from .p_jump import p_jump
class phase_child(Group):
    """
    'child_object_type' of phase.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['geom_disable', 'geom_dir_spec', 'geom_dir_x', 'geom_dir_y',
         'geom_dir_z', 'geom_levels', 'geom_bgthread', 'angular', 'p_jump']

    geom_disable: geom_disable = geom_disable
    """
    geom_disable child of phase_child.
    """
    geom_dir_spec: geom_dir_spec = geom_dir_spec
    """
    geom_dir_spec child of phase_child.
    """
    geom_dir_x: geom_dir_x = geom_dir_x
    """
    geom_dir_x child of phase_child.
    """
    geom_dir_y: geom_dir_y = geom_dir_y
    """
    geom_dir_y child of phase_child.
    """
    geom_dir_z: geom_dir_z = geom_dir_z
    """
    geom_dir_z child of phase_child.
    """
    geom_levels: geom_levels = geom_levels
    """
    geom_levels child of phase_child.
    """
    geom_bgthread: geom_bgthread = geom_bgthread
    """
    geom_bgthread child of phase_child.
    """
    angular: angular = angular
    """
    angular child of phase_child.
    """
    p_jump: p_jump = p_jump
    """
    p_jump child of phase_child.
    """
