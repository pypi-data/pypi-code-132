#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .axis import axis
from .degassing import degassing
from .exhaust_fan import exhaust_fan
from .fan import fan
from .geometry_1 import geometry
from .inlet_vent import inlet_vent
from .intake_fan import intake_fan
from .interface import interface
from .interior import interior
from .mass_flow_inlet import mass_flow_inlet
from .mass_flow_outlet import mass_flow_outlet
from .network import network
from .network_end import network_end
from .outflow import outflow
from .outlet_vent import outlet_vent
from .overset import overset
from .periodic import periodic
from .porous_jump import porous_jump
from .pressure_far_field import pressure_far_field
from .pressure_inlet import pressure_inlet
from .pressure_outlet import pressure_outlet
from .radiator import radiator
from .rans_les_interface import rans_les_interface
from .recirculation_inlet import recirculation_inlet
from .recirculation_outlet import recirculation_outlet
from .shadow import shadow
from .symmetry import symmetry
from .velocity_inlet import velocity_inlet
from .wall import wall
from .change_type import change_type
from .slit_face_zone import slit_face_zone
from .slit_interior_between_diff_solids import slit_interior_between_diff_solids
from .create_all_shell_threads import create_all_shell_threads
from .recreate_all_shells import recreate_all_shells
from .delete_all_shells import delete_all_shells
from .orient_face_zone import orient_face_zone
class boundary_conditions(Group, _ChildNamedObjectAccessorMixin):
    """
    'boundary_conditions' child.
    """

    fluent_name = "boundary-conditions"

    child_names = \
        ['axis', 'degassing', 'exhaust_fan', 'fan', 'geometry', 'inlet_vent',
         'intake_fan', 'interface', 'interior', 'mass_flow_inlet',
         'mass_flow_outlet', 'network', 'network_end', 'outflow',
         'outlet_vent', 'overset', 'periodic', 'porous_jump',
         'pressure_far_field', 'pressure_inlet', 'pressure_outlet',
         'radiator', 'rans_les_interface', 'recirculation_inlet',
         'recirculation_outlet', 'shadow', 'symmetry', 'velocity_inlet',
         'wall']

    axis: axis = axis
    """
    axis child of boundary_conditions.
    """
    degassing: degassing = degassing
    """
    degassing child of boundary_conditions.
    """
    exhaust_fan: exhaust_fan = exhaust_fan
    """
    exhaust_fan child of boundary_conditions.
    """
    fan: fan = fan
    """
    fan child of boundary_conditions.
    """
    geometry: geometry = geometry
    """
    geometry child of boundary_conditions.
    """
    inlet_vent: inlet_vent = inlet_vent
    """
    inlet_vent child of boundary_conditions.
    """
    intake_fan: intake_fan = intake_fan
    """
    intake_fan child of boundary_conditions.
    """
    interface: interface = interface
    """
    interface child of boundary_conditions.
    """
    interior: interior = interior
    """
    interior child of boundary_conditions.
    """
    mass_flow_inlet: mass_flow_inlet = mass_flow_inlet
    """
    mass_flow_inlet child of boundary_conditions.
    """
    mass_flow_outlet: mass_flow_outlet = mass_flow_outlet
    """
    mass_flow_outlet child of boundary_conditions.
    """
    network: network = network
    """
    network child of boundary_conditions.
    """
    network_end: network_end = network_end
    """
    network_end child of boundary_conditions.
    """
    outflow: outflow = outflow
    """
    outflow child of boundary_conditions.
    """
    outlet_vent: outlet_vent = outlet_vent
    """
    outlet_vent child of boundary_conditions.
    """
    overset: overset = overset
    """
    overset child of boundary_conditions.
    """
    periodic: periodic = periodic
    """
    periodic child of boundary_conditions.
    """
    porous_jump: porous_jump = porous_jump
    """
    porous_jump child of boundary_conditions.
    """
    pressure_far_field: pressure_far_field = pressure_far_field
    """
    pressure_far_field child of boundary_conditions.
    """
    pressure_inlet: pressure_inlet = pressure_inlet
    """
    pressure_inlet child of boundary_conditions.
    """
    pressure_outlet: pressure_outlet = pressure_outlet
    """
    pressure_outlet child of boundary_conditions.
    """
    radiator: radiator = radiator
    """
    radiator child of boundary_conditions.
    """
    rans_les_interface: rans_les_interface = rans_les_interface
    """
    rans_les_interface child of boundary_conditions.
    """
    recirculation_inlet: recirculation_inlet = recirculation_inlet
    """
    recirculation_inlet child of boundary_conditions.
    """
    recirculation_outlet: recirculation_outlet = recirculation_outlet
    """
    recirculation_outlet child of boundary_conditions.
    """
    shadow: shadow = shadow
    """
    shadow child of boundary_conditions.
    """
    symmetry: symmetry = symmetry
    """
    symmetry child of boundary_conditions.
    """
    velocity_inlet: velocity_inlet = velocity_inlet
    """
    velocity_inlet child of boundary_conditions.
    """
    wall: wall = wall
    """
    wall child of boundary_conditions.
    """
    command_names = \
        ['change_type', 'slit_face_zone', 'slit_interior_between_diff_solids',
         'create_all_shell_threads', 'recreate_all_shells',
         'delete_all_shells', 'orient_face_zone']

    change_type: change_type = change_type
    """
    change_type command of boundary_conditions.
    """
    slit_face_zone: slit_face_zone = slit_face_zone
    """
    slit_face_zone command of boundary_conditions.
    """
    slit_interior_between_diff_solids: slit_interior_between_diff_solids = slit_interior_between_diff_solids
    """
    slit_interior_between_diff_solids command of boundary_conditions.
    """
    create_all_shell_threads: create_all_shell_threads = create_all_shell_threads
    """
    create_all_shell_threads command of boundary_conditions.
    """
    recreate_all_shells: recreate_all_shells = recreate_all_shells
    """
    recreate_all_shells command of boundary_conditions.
    """
    delete_all_shells: delete_all_shells = delete_all_shells
    """
    delete_all_shells command of boundary_conditions.
    """
    orient_face_zone: orient_face_zone = orient_face_zone
    """
    orient_face_zone command of boundary_conditions.
    """
