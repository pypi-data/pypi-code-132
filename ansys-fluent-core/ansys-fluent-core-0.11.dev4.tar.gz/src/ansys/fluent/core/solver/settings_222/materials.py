#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .fluid import fluid
from .solid import solid
from .mixture import mixture
from .inert_particle import inert_particle
from .droplet_particle import droplet_particle
from .combusting_particle import combusting_particle
from .particle_mixture import particle_mixture
from .list_materials import list_materials
from .copy_database_material_by_name import copy_database_material_by_name
from .copy_database_material_by_formula import copy_database_material_by_formula
class materials(Group):
    """
    'materials' child.
    """

    fluent_name = "materials"

    child_names = \
        ['fluid', 'solid', 'mixture', 'inert_particle', 'droplet_particle',
         'combusting_particle', 'particle_mixture']

    fluid: fluid = fluid
    """
    fluid child of materials.
    """
    solid: solid = solid
    """
    solid child of materials.
    """
    mixture: mixture = mixture
    """
    mixture child of materials.
    """
    inert_particle: inert_particle = inert_particle
    """
    inert_particle child of materials.
    """
    droplet_particle: droplet_particle = droplet_particle
    """
    droplet_particle child of materials.
    """
    combusting_particle: combusting_particle = combusting_particle
    """
    combusting_particle child of materials.
    """
    particle_mixture: particle_mixture = particle_mixture
    """
    particle_mixture child of materials.
    """
    command_names = \
        ['list_materials', 'copy_database_material_by_name',
         'copy_database_material_by_formula']

    list_materials: list_materials = list_materials
    """
    list_materials command of materials.
    """
    copy_database_material_by_name: copy_database_material_by_name = copy_database_material_by_name
    """
    copy_database_material_by_name command of materials.
    """
    copy_database_material_by_formula: copy_database_material_by_formula = copy_database_material_by_formula
    """
    copy_database_material_by_formula command of materials.
    """
