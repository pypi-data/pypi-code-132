#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .turb_visc_func_mf_child import turb_visc_func_mf_child

class species_spec(NamedObject[turb_visc_func_mf_child], _CreatableNamedObjectMixin[turb_visc_func_mf_child]):
    """
    'species_spec' child.
    """

    fluent_name = "species-spec"

    child_object_type: turb_visc_func_mf_child = turb_visc_func_mf_child
    """
    child_object_type of species_spec.
    """
