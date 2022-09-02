#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .scale_2 import scale
from .sphere_lod import sphere_lod
from .options_9 import options
class sphere_settings(Group):
    """
    'sphere_settings' child.
    """

    fluent_name = "sphere-settings"

    child_names = \
        ['scale', 'sphere_lod', 'options']

    scale: scale = scale
    """
    scale child of sphere_settings.
    """
    sphere_lod: sphere_lod = sphere_lod
    """
    sphere_lod child of sphere_settings.
    """
    options: options = options
    """
    options child of sphere_settings.
    """
