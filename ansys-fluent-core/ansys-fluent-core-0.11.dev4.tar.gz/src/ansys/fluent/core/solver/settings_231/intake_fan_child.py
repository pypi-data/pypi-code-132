#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .phase_6 import phase
from .geom_disable import geom_disable
from .geom_dir_spec import geom_dir_spec
from .geom_dir_x import geom_dir_x
from .geom_dir_y import geom_dir_y
from .geom_dir_z import geom_dir_z
from .geom_levels import geom_levels
from .geom_bgthread import geom_bgthread
from .open_channel import open_channel
from .inlet_number import inlet_number
from .phase_spec import phase_spec
from .frame_of_reference import frame_of_reference
from .p0 import p0
from .supersonic_or_initial_gauge_pressure import supersonic_or_initial_gauge_pressure
from .t0 import t0
from .direction_spec import direction_spec
from .flow_spec import flow_spec
from .ht_local import ht_local
from .ht_total import ht_total
from .vmag import vmag
from .ht_bottom import ht_bottom
from .den_spec import den_spec
from .coordinate_system import coordinate_system
from .flow_direction import flow_direction
from .direction_vector import direction_vector
from .axis_direction_2 import axis_direction
from .axis_origin_2 import axis_origin
from .les_spec_name import les_spec_name
from .rfg_number_of_modes import rfg_number_of_modes
from .vm_number_of_vortices import vm_number_of_vortices
from .vm_streamwise_fluct import vm_streamwise_fluct
from .vm_mass_conservation import vm_mass_conservation
from .stg_scale_limiter_type import stg_scale_limiter_type
from .stg_ti_limiter import stg_ti_limiter
from .stg_tvr_limiter import stg_tvr_limiter
from .stg_dw_limiter import stg_dw_limiter
from .volumetric_synthetic_turbulence_generator import volumetric_synthetic_turbulence_generator
from .volumetric_synthetic_turbulence_generator_option import volumetric_synthetic_turbulence_generator_option
from .volumetric_synthetic_turbulence_generator_option_thickness import volumetric_synthetic_turbulence_generator_option_thickness
from .prevent_reverse_flow import prevent_reverse_flow
from .ke_spec import ke_spec
from .nut import nut
from .kl import kl
from .intermit import intermit
from .k import k
from .e import e
from .o import o
from .v2 import v2
from .turb_intensity import turb_intensity
from .turb_length_scale import turb_length_scale
from .turb_hydraulic_diam import turb_hydraulic_diam
from .turb_viscosity_ratio import turb_viscosity_ratio
from .turb_viscosity_ratio_profile import turb_viscosity_ratio_profile
from .rst_spec import rst_spec
from .uu import uu
from .vv import vv
from .ww import ww
from .uv import uv
from .vw import vw
from .uw import uw
from .ksgs_spec import ksgs_spec
from .ksgs import ksgs
from .sgs_turb_intensity import sgs_turb_intensity
from .granular_temperature import granular_temperature
from .iac import iac
from .lsfun import lsfun
from .volume_fraction import volume_fraction
from .species_in_mole_fractions import species_in_mole_fractions
from .mf import mf
from .elec_potential_type import elec_potential_type
from .potential_value import potential_value
from .dual_potential_type import dual_potential_type
from .dual_potential_value import dual_potential_value
from .x_displacement_type import x_displacement_type
from .x_displacement_value import x_displacement_value
from .y_displacement_type import y_displacement_type
from .y_displacement_value import y_displacement_value
from .z_displacement_type import z_displacement_type
from .z_displacement_value import z_displacement_value
from .prob_mode_1 import prob_mode_1
from .prob_mode_2 import prob_mode_2
from .prob_mode_3 import prob_mode_3
from .equ_required import equ_required
from .uds_bc import uds_bc
from .uds import uds
from .pb_disc_bc import pb_disc_bc
from .pb_disc import pb_disc
from .pb_qmom_bc import pb_qmom_bc
from .pb_qmom import pb_qmom
from .pb_smm_bc import pb_smm_bc
from .pb_smm import pb_smm
from .pb_dqmom_bc import pb_dqmom_bc
from .pb_dqmom import pb_dqmom
from .radiation_bc import radiation_bc
from .radial_direction import radial_direction
from .coll_dtheta import coll_dtheta
from .coll_dphi import coll_dphi
from .band_q_irrad import band_q_irrad
from .band_q_irrad_diffuse import band_q_irrad_diffuse
from .parallel_collimated_beam import parallel_collimated_beam
from .solar_direction import solar_direction
from .solar_irradiation import solar_irradiation
from .t_b_b_spec import t_b_b_spec
from .t_b_b import t_b_b
from .in_emiss import in_emiss
from .fmean import fmean
from .fvar import fvar
from .fmean2 import fmean2
from .fvar2 import fvar2
from .premixc import premixc
from .premixc_var import premixc_var
from .ecfm_sigma import ecfm_sigma
from .inert import inert
from .pollut_no import pollut_no
from .pollut_hcn import pollut_hcn
from .pollut_nh3 import pollut_nh3
from .pollut_n2o import pollut_n2o
from .pollut_urea import pollut_urea
from .pollut_hnco import pollut_hnco
from .pollut_nco import pollut_nco
from .pollut_so2 import pollut_so2
from .pollut_h2s import pollut_h2s
from .pollut_so3 import pollut_so3
from .pollut_sh import pollut_sh
from .pollut_so import pollut_so
from .pollut_soot import pollut_soot
from .pollut_nuclei import pollut_nuclei
from .pollut_ctar import pollut_ctar
from .pollut_hg import pollut_hg
from .pollut_hgcl2 import pollut_hgcl2
from .pollut_hcl import pollut_hcl
from .pollut_hgo import pollut_hgo
from .pollut_cl import pollut_cl
from .pollut_cl2 import pollut_cl2
from .pollut_hgcl import pollut_hgcl
from .pollut_hocl import pollut_hocl
from .tss_scalar import tss_scalar
from .dpm_bc_type import dpm_bc_type
from .dpm_bc_collision_partner import dpm_bc_collision_partner
from .reinj_inj import reinj_inj
from .dpm_bc_udf import dpm_bc_udf
from .fensapice_flow_bc_subtype import fensapice_flow_bc_subtype
from .fensapice_drop_bccustom import fensapice_drop_bccustom
from .fensapice_drop_lwc import fensapice_drop_lwc
from .fensapice_drop_dtemp import fensapice_drop_dtemp
from .fensapice_drop_ddiam import fensapice_drop_ddiam
from .fensapice_drop_dv import fensapice_drop_dv
from .fensapice_drop_dx import fensapice_drop_dx
from .fensapice_drop_dy import fensapice_drop_dy
from .fensapice_drop_dz import fensapice_drop_dz
from .fensapice_dpm_surface_injection import fensapice_dpm_surface_injection
from .fensapice_dpm_inj_nstream import fensapice_dpm_inj_nstream
from .fensapice_drop_icc import fensapice_drop_icc
from .fensapice_drop_ctemp import fensapice_drop_ctemp
from .fensapice_drop_cdiam import fensapice_drop_cdiam
from .fensapice_drop_cv import fensapice_drop_cv
from .fensapice_drop_cx import fensapice_drop_cx
from .fensapice_drop_cy import fensapice_drop_cy
from .fensapice_drop_cz import fensapice_drop_cz
from .fensapice_drop_vrh import fensapice_drop_vrh
from .fensapice_drop_vrh_1 import fensapice_drop_vrh_1
from .fensapice_drop_vc import fensapice_drop_vc
from .mixing_plane_thread import mixing_plane_thread
from .wsf import wsf
from .wsb import wsb
from .wsn import wsn
from .solar_fluxes import solar_fluxes
from .solar_shining_factor import solar_shining_factor
from .radiating_s2s_surface import radiating_s2s_surface
from .ac_options import ac_options
from .impedance_0 import impedance_0
from .impedance_1 import impedance_1
from .impedance_2 import impedance_2
from .ac_wave import ac_wave
from .les_spec import les_spec
from .a_1 import a
from .swirl_model import swirl_model
from .swirl_factor import swirl_factor
from .fan_omega import fan_omega
from .fan_origin import fan_origin
from .strength import strength
from .new_fan_definition import new_fan_definition
class intake_fan_child(Group):
    """
    'child_object_type' of intake_fan.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['phase', 'geom_disable', 'geom_dir_spec', 'geom_dir_x', 'geom_dir_y',
         'geom_dir_z', 'geom_levels', 'geom_bgthread', 'open_channel',
         'inlet_number', 'phase_spec', 'frame_of_reference', 'p0',
         'supersonic_or_initial_gauge_pressure', 't0', 'direction_spec',
         'flow_spec', 'ht_local', 'ht_total', 'vmag', 'ht_bottom', 'den_spec',
         'coordinate_system', 'flow_direction', 'direction_vector',
         'axis_direction', 'axis_origin', 'les_spec_name',
         'rfg_number_of_modes', 'vm_number_of_vortices',
         'vm_streamwise_fluct', 'vm_mass_conservation',
         'stg_scale_limiter_type', 'stg_ti_limiter', 'stg_tvr_limiter',
         'stg_dw_limiter', 'volumetric_synthetic_turbulence_generator',
         'volumetric_synthetic_turbulence_generator_option',
         'volumetric_synthetic_turbulence_generator_option_thickness',
         'prevent_reverse_flow', 'ke_spec', 'nut', 'kl', 'intermit', 'k', 'e',
         'o', 'v2', 'turb_intensity', 'turb_length_scale',
         'turb_hydraulic_diam', 'turb_viscosity_ratio',
         'turb_viscosity_ratio_profile', 'rst_spec', 'uu', 'vv', 'ww', 'uv',
         'vw', 'uw', 'ksgs_spec', 'ksgs', 'sgs_turb_intensity',
         'granular_temperature', 'iac', 'lsfun', 'volume_fraction',
         'species_in_mole_fractions', 'mf', 'elec_potential_type',
         'potential_value', 'dual_potential_type', 'dual_potential_value',
         'x_displacement_type', 'x_displacement_value', 'y_displacement_type',
         'y_displacement_value', 'z_displacement_type',
         'z_displacement_value', 'prob_mode_1', 'prob_mode_2', 'prob_mode_3',
         'equ_required', 'uds_bc', 'uds', 'pb_disc_bc', 'pb_disc',
         'pb_qmom_bc', 'pb_qmom', 'pb_smm_bc', 'pb_smm', 'pb_dqmom_bc',
         'pb_dqmom', 'radiation_bc', 'radial_direction', 'coll_dtheta',
         'coll_dphi', 'band_q_irrad', 'band_q_irrad_diffuse',
         'parallel_collimated_beam', 'solar_direction', 'solar_irradiation',
         't_b_b_spec', 't_b_b', 'in_emiss', 'fmean', 'fvar', 'fmean2',
         'fvar2', 'premixc', 'premixc_var', 'ecfm_sigma', 'inert',
         'pollut_no', 'pollut_hcn', 'pollut_nh3', 'pollut_n2o', 'pollut_urea',
         'pollut_hnco', 'pollut_nco', 'pollut_so2', 'pollut_h2s',
         'pollut_so3', 'pollut_sh', 'pollut_so', 'pollut_soot',
         'pollut_nuclei', 'pollut_ctar', 'pollut_hg', 'pollut_hgcl2',
         'pollut_hcl', 'pollut_hgo', 'pollut_cl', 'pollut_cl2', 'pollut_hgcl',
         'pollut_hocl', 'tss_scalar', 'dpm_bc_type',
         'dpm_bc_collision_partner', 'reinj_inj', 'dpm_bc_udf',
         'fensapice_flow_bc_subtype', 'fensapice_drop_bccustom',
         'fensapice_drop_lwc', 'fensapice_drop_dtemp', 'fensapice_drop_ddiam',
         'fensapice_drop_dv', 'fensapice_drop_dx', 'fensapice_drop_dy',
         'fensapice_drop_dz', 'fensapice_dpm_surface_injection',
         'fensapice_dpm_inj_nstream', 'fensapice_drop_icc',
         'fensapice_drop_ctemp', 'fensapice_drop_cdiam', 'fensapice_drop_cv',
         'fensapice_drop_cx', 'fensapice_drop_cy', 'fensapice_drop_cz',
         'fensapice_drop_vrh', 'fensapice_drop_vrh_1', 'fensapice_drop_vc',
         'mixing_plane_thread', 'wsf', 'wsb', 'wsn', 'solar_fluxes',
         'solar_shining_factor', 'radiating_s2s_surface', 'ac_options',
         'impedance_0', 'impedance_1', 'impedance_2', 'ac_wave', 'les_spec',
         'a', 'swirl_model', 'swirl_factor', 'fan_omega', 'fan_origin',
         'strength', 'new_fan_definition']

    phase: phase = phase
    """
    phase child of intake_fan_child.
    """
    geom_disable: geom_disable = geom_disable
    """
    geom_disable child of intake_fan_child.
    """
    geom_dir_spec: geom_dir_spec = geom_dir_spec
    """
    geom_dir_spec child of intake_fan_child.
    """
    geom_dir_x: geom_dir_x = geom_dir_x
    """
    geom_dir_x child of intake_fan_child.
    """
    geom_dir_y: geom_dir_y = geom_dir_y
    """
    geom_dir_y child of intake_fan_child.
    """
    geom_dir_z: geom_dir_z = geom_dir_z
    """
    geom_dir_z child of intake_fan_child.
    """
    geom_levels: geom_levels = geom_levels
    """
    geom_levels child of intake_fan_child.
    """
    geom_bgthread: geom_bgthread = geom_bgthread
    """
    geom_bgthread child of intake_fan_child.
    """
    open_channel: open_channel = open_channel
    """
    open_channel child of intake_fan_child.
    """
    inlet_number: inlet_number = inlet_number
    """
    inlet_number child of intake_fan_child.
    """
    phase_spec: phase_spec = phase_spec
    """
    phase_spec child of intake_fan_child.
    """
    frame_of_reference: frame_of_reference = frame_of_reference
    """
    frame_of_reference child of intake_fan_child.
    """
    p0: p0 = p0
    """
    p0 child of intake_fan_child.
    """
    supersonic_or_initial_gauge_pressure: supersonic_or_initial_gauge_pressure = supersonic_or_initial_gauge_pressure
    """
    supersonic_or_initial_gauge_pressure child of intake_fan_child.
    """
    t0: t0 = t0
    """
    t0 child of intake_fan_child.
    """
    direction_spec: direction_spec = direction_spec
    """
    direction_spec child of intake_fan_child.
    """
    flow_spec: flow_spec = flow_spec
    """
    flow_spec child of intake_fan_child.
    """
    ht_local: ht_local = ht_local
    """
    ht_local child of intake_fan_child.
    """
    ht_total: ht_total = ht_total
    """
    ht_total child of intake_fan_child.
    """
    vmag: vmag = vmag
    """
    vmag child of intake_fan_child.
    """
    ht_bottom: ht_bottom = ht_bottom
    """
    ht_bottom child of intake_fan_child.
    """
    den_spec: den_spec = den_spec
    """
    den_spec child of intake_fan_child.
    """
    coordinate_system: coordinate_system = coordinate_system
    """
    coordinate_system child of intake_fan_child.
    """
    flow_direction: flow_direction = flow_direction
    """
    flow_direction child of intake_fan_child.
    """
    direction_vector: direction_vector = direction_vector
    """
    direction_vector child of intake_fan_child.
    """
    axis_direction: axis_direction = axis_direction
    """
    axis_direction child of intake_fan_child.
    """
    axis_origin: axis_origin = axis_origin
    """
    axis_origin child of intake_fan_child.
    """
    les_spec_name: les_spec_name = les_spec_name
    """
    les_spec_name child of intake_fan_child.
    """
    rfg_number_of_modes: rfg_number_of_modes = rfg_number_of_modes
    """
    rfg_number_of_modes child of intake_fan_child.
    """
    vm_number_of_vortices: vm_number_of_vortices = vm_number_of_vortices
    """
    vm_number_of_vortices child of intake_fan_child.
    """
    vm_streamwise_fluct: vm_streamwise_fluct = vm_streamwise_fluct
    """
    vm_streamwise_fluct child of intake_fan_child.
    """
    vm_mass_conservation: vm_mass_conservation = vm_mass_conservation
    """
    vm_mass_conservation child of intake_fan_child.
    """
    stg_scale_limiter_type: stg_scale_limiter_type = stg_scale_limiter_type
    """
    stg_scale_limiter_type child of intake_fan_child.
    """
    stg_ti_limiter: stg_ti_limiter = stg_ti_limiter
    """
    stg_ti_limiter child of intake_fan_child.
    """
    stg_tvr_limiter: stg_tvr_limiter = stg_tvr_limiter
    """
    stg_tvr_limiter child of intake_fan_child.
    """
    stg_dw_limiter: stg_dw_limiter = stg_dw_limiter
    """
    stg_dw_limiter child of intake_fan_child.
    """
    volumetric_synthetic_turbulence_generator: volumetric_synthetic_turbulence_generator = volumetric_synthetic_turbulence_generator
    """
    volumetric_synthetic_turbulence_generator child of intake_fan_child.
    """
    volumetric_synthetic_turbulence_generator_option: volumetric_synthetic_turbulence_generator_option = volumetric_synthetic_turbulence_generator_option
    """
    volumetric_synthetic_turbulence_generator_option child of intake_fan_child.
    """
    volumetric_synthetic_turbulence_generator_option_thickness: volumetric_synthetic_turbulence_generator_option_thickness = volumetric_synthetic_turbulence_generator_option_thickness
    """
    volumetric_synthetic_turbulence_generator_option_thickness child of intake_fan_child.
    """
    prevent_reverse_flow: prevent_reverse_flow = prevent_reverse_flow
    """
    prevent_reverse_flow child of intake_fan_child.
    """
    ke_spec: ke_spec = ke_spec
    """
    ke_spec child of intake_fan_child.
    """
    nut: nut = nut
    """
    nut child of intake_fan_child.
    """
    kl: kl = kl
    """
    kl child of intake_fan_child.
    """
    intermit: intermit = intermit
    """
    intermit child of intake_fan_child.
    """
    k: k = k
    """
    k child of intake_fan_child.
    """
    e: e = e
    """
    e child of intake_fan_child.
    """
    o: o = o
    """
    o child of intake_fan_child.
    """
    v2: v2 = v2
    """
    v2 child of intake_fan_child.
    """
    turb_intensity: turb_intensity = turb_intensity
    """
    turb_intensity child of intake_fan_child.
    """
    turb_length_scale: turb_length_scale = turb_length_scale
    """
    turb_length_scale child of intake_fan_child.
    """
    turb_hydraulic_diam: turb_hydraulic_diam = turb_hydraulic_diam
    """
    turb_hydraulic_diam child of intake_fan_child.
    """
    turb_viscosity_ratio: turb_viscosity_ratio = turb_viscosity_ratio
    """
    turb_viscosity_ratio child of intake_fan_child.
    """
    turb_viscosity_ratio_profile: turb_viscosity_ratio_profile = turb_viscosity_ratio_profile
    """
    turb_viscosity_ratio_profile child of intake_fan_child.
    """
    rst_spec: rst_spec = rst_spec
    """
    rst_spec child of intake_fan_child.
    """
    uu: uu = uu
    """
    uu child of intake_fan_child.
    """
    vv: vv = vv
    """
    vv child of intake_fan_child.
    """
    ww: ww = ww
    """
    ww child of intake_fan_child.
    """
    uv: uv = uv
    """
    uv child of intake_fan_child.
    """
    vw: vw = vw
    """
    vw child of intake_fan_child.
    """
    uw: uw = uw
    """
    uw child of intake_fan_child.
    """
    ksgs_spec: ksgs_spec = ksgs_spec
    """
    ksgs_spec child of intake_fan_child.
    """
    ksgs: ksgs = ksgs
    """
    ksgs child of intake_fan_child.
    """
    sgs_turb_intensity: sgs_turb_intensity = sgs_turb_intensity
    """
    sgs_turb_intensity child of intake_fan_child.
    """
    granular_temperature: granular_temperature = granular_temperature
    """
    granular_temperature child of intake_fan_child.
    """
    iac: iac = iac
    """
    iac child of intake_fan_child.
    """
    lsfun: lsfun = lsfun
    """
    lsfun child of intake_fan_child.
    """
    volume_fraction: volume_fraction = volume_fraction
    """
    volume_fraction child of intake_fan_child.
    """
    species_in_mole_fractions: species_in_mole_fractions = species_in_mole_fractions
    """
    species_in_mole_fractions child of intake_fan_child.
    """
    mf: mf = mf
    """
    mf child of intake_fan_child.
    """
    elec_potential_type: elec_potential_type = elec_potential_type
    """
    elec_potential_type child of intake_fan_child.
    """
    potential_value: potential_value = potential_value
    """
    potential_value child of intake_fan_child.
    """
    dual_potential_type: dual_potential_type = dual_potential_type
    """
    dual_potential_type child of intake_fan_child.
    """
    dual_potential_value: dual_potential_value = dual_potential_value
    """
    dual_potential_value child of intake_fan_child.
    """
    x_displacement_type: x_displacement_type = x_displacement_type
    """
    x_displacement_type child of intake_fan_child.
    """
    x_displacement_value: x_displacement_value = x_displacement_value
    """
    x_displacement_value child of intake_fan_child.
    """
    y_displacement_type: y_displacement_type = y_displacement_type
    """
    y_displacement_type child of intake_fan_child.
    """
    y_displacement_value: y_displacement_value = y_displacement_value
    """
    y_displacement_value child of intake_fan_child.
    """
    z_displacement_type: z_displacement_type = z_displacement_type
    """
    z_displacement_type child of intake_fan_child.
    """
    z_displacement_value: z_displacement_value = z_displacement_value
    """
    z_displacement_value child of intake_fan_child.
    """
    prob_mode_1: prob_mode_1 = prob_mode_1
    """
    prob_mode_1 child of intake_fan_child.
    """
    prob_mode_2: prob_mode_2 = prob_mode_2
    """
    prob_mode_2 child of intake_fan_child.
    """
    prob_mode_3: prob_mode_3 = prob_mode_3
    """
    prob_mode_3 child of intake_fan_child.
    """
    equ_required: equ_required = equ_required
    """
    equ_required child of intake_fan_child.
    """
    uds_bc: uds_bc = uds_bc
    """
    uds_bc child of intake_fan_child.
    """
    uds: uds = uds
    """
    uds child of intake_fan_child.
    """
    pb_disc_bc: pb_disc_bc = pb_disc_bc
    """
    pb_disc_bc child of intake_fan_child.
    """
    pb_disc: pb_disc = pb_disc
    """
    pb_disc child of intake_fan_child.
    """
    pb_qmom_bc: pb_qmom_bc = pb_qmom_bc
    """
    pb_qmom_bc child of intake_fan_child.
    """
    pb_qmom: pb_qmom = pb_qmom
    """
    pb_qmom child of intake_fan_child.
    """
    pb_smm_bc: pb_smm_bc = pb_smm_bc
    """
    pb_smm_bc child of intake_fan_child.
    """
    pb_smm: pb_smm = pb_smm
    """
    pb_smm child of intake_fan_child.
    """
    pb_dqmom_bc: pb_dqmom_bc = pb_dqmom_bc
    """
    pb_dqmom_bc child of intake_fan_child.
    """
    pb_dqmom: pb_dqmom = pb_dqmom
    """
    pb_dqmom child of intake_fan_child.
    """
    radiation_bc: radiation_bc = radiation_bc
    """
    radiation_bc child of intake_fan_child.
    """
    radial_direction: radial_direction = radial_direction
    """
    radial_direction child of intake_fan_child.
    """
    coll_dtheta: coll_dtheta = coll_dtheta
    """
    coll_dtheta child of intake_fan_child.
    """
    coll_dphi: coll_dphi = coll_dphi
    """
    coll_dphi child of intake_fan_child.
    """
    band_q_irrad: band_q_irrad = band_q_irrad
    """
    band_q_irrad child of intake_fan_child.
    """
    band_q_irrad_diffuse: band_q_irrad_diffuse = band_q_irrad_diffuse
    """
    band_q_irrad_diffuse child of intake_fan_child.
    """
    parallel_collimated_beam: parallel_collimated_beam = parallel_collimated_beam
    """
    parallel_collimated_beam child of intake_fan_child.
    """
    solar_direction: solar_direction = solar_direction
    """
    solar_direction child of intake_fan_child.
    """
    solar_irradiation: solar_irradiation = solar_irradiation
    """
    solar_irradiation child of intake_fan_child.
    """
    t_b_b_spec: t_b_b_spec = t_b_b_spec
    """
    t_b_b_spec child of intake_fan_child.
    """
    t_b_b: t_b_b = t_b_b
    """
    t_b_b child of intake_fan_child.
    """
    in_emiss: in_emiss = in_emiss
    """
    in_emiss child of intake_fan_child.
    """
    fmean: fmean = fmean
    """
    fmean child of intake_fan_child.
    """
    fvar: fvar = fvar
    """
    fvar child of intake_fan_child.
    """
    fmean2: fmean2 = fmean2
    """
    fmean2 child of intake_fan_child.
    """
    fvar2: fvar2 = fvar2
    """
    fvar2 child of intake_fan_child.
    """
    premixc: premixc = premixc
    """
    premixc child of intake_fan_child.
    """
    premixc_var: premixc_var = premixc_var
    """
    premixc_var child of intake_fan_child.
    """
    ecfm_sigma: ecfm_sigma = ecfm_sigma
    """
    ecfm_sigma child of intake_fan_child.
    """
    inert: inert = inert
    """
    inert child of intake_fan_child.
    """
    pollut_no: pollut_no = pollut_no
    """
    pollut_no child of intake_fan_child.
    """
    pollut_hcn: pollut_hcn = pollut_hcn
    """
    pollut_hcn child of intake_fan_child.
    """
    pollut_nh3: pollut_nh3 = pollut_nh3
    """
    pollut_nh3 child of intake_fan_child.
    """
    pollut_n2o: pollut_n2o = pollut_n2o
    """
    pollut_n2o child of intake_fan_child.
    """
    pollut_urea: pollut_urea = pollut_urea
    """
    pollut_urea child of intake_fan_child.
    """
    pollut_hnco: pollut_hnco = pollut_hnco
    """
    pollut_hnco child of intake_fan_child.
    """
    pollut_nco: pollut_nco = pollut_nco
    """
    pollut_nco child of intake_fan_child.
    """
    pollut_so2: pollut_so2 = pollut_so2
    """
    pollut_so2 child of intake_fan_child.
    """
    pollut_h2s: pollut_h2s = pollut_h2s
    """
    pollut_h2s child of intake_fan_child.
    """
    pollut_so3: pollut_so3 = pollut_so3
    """
    pollut_so3 child of intake_fan_child.
    """
    pollut_sh: pollut_sh = pollut_sh
    """
    pollut_sh child of intake_fan_child.
    """
    pollut_so: pollut_so = pollut_so
    """
    pollut_so child of intake_fan_child.
    """
    pollut_soot: pollut_soot = pollut_soot
    """
    pollut_soot child of intake_fan_child.
    """
    pollut_nuclei: pollut_nuclei = pollut_nuclei
    """
    pollut_nuclei child of intake_fan_child.
    """
    pollut_ctar: pollut_ctar = pollut_ctar
    """
    pollut_ctar child of intake_fan_child.
    """
    pollut_hg: pollut_hg = pollut_hg
    """
    pollut_hg child of intake_fan_child.
    """
    pollut_hgcl2: pollut_hgcl2 = pollut_hgcl2
    """
    pollut_hgcl2 child of intake_fan_child.
    """
    pollut_hcl: pollut_hcl = pollut_hcl
    """
    pollut_hcl child of intake_fan_child.
    """
    pollut_hgo: pollut_hgo = pollut_hgo
    """
    pollut_hgo child of intake_fan_child.
    """
    pollut_cl: pollut_cl = pollut_cl
    """
    pollut_cl child of intake_fan_child.
    """
    pollut_cl2: pollut_cl2 = pollut_cl2
    """
    pollut_cl2 child of intake_fan_child.
    """
    pollut_hgcl: pollut_hgcl = pollut_hgcl
    """
    pollut_hgcl child of intake_fan_child.
    """
    pollut_hocl: pollut_hocl = pollut_hocl
    """
    pollut_hocl child of intake_fan_child.
    """
    tss_scalar: tss_scalar = tss_scalar
    """
    tss_scalar child of intake_fan_child.
    """
    dpm_bc_type: dpm_bc_type = dpm_bc_type
    """
    dpm_bc_type child of intake_fan_child.
    """
    dpm_bc_collision_partner: dpm_bc_collision_partner = dpm_bc_collision_partner
    """
    dpm_bc_collision_partner child of intake_fan_child.
    """
    reinj_inj: reinj_inj = reinj_inj
    """
    reinj_inj child of intake_fan_child.
    """
    dpm_bc_udf: dpm_bc_udf = dpm_bc_udf
    """
    dpm_bc_udf child of intake_fan_child.
    """
    fensapice_flow_bc_subtype: fensapice_flow_bc_subtype = fensapice_flow_bc_subtype
    """
    fensapice_flow_bc_subtype child of intake_fan_child.
    """
    fensapice_drop_bccustom: fensapice_drop_bccustom = fensapice_drop_bccustom
    """
    fensapice_drop_bccustom child of intake_fan_child.
    """
    fensapice_drop_lwc: fensapice_drop_lwc = fensapice_drop_lwc
    """
    fensapice_drop_lwc child of intake_fan_child.
    """
    fensapice_drop_dtemp: fensapice_drop_dtemp = fensapice_drop_dtemp
    """
    fensapice_drop_dtemp child of intake_fan_child.
    """
    fensapice_drop_ddiam: fensapice_drop_ddiam = fensapice_drop_ddiam
    """
    fensapice_drop_ddiam child of intake_fan_child.
    """
    fensapice_drop_dv: fensapice_drop_dv = fensapice_drop_dv
    """
    fensapice_drop_dv child of intake_fan_child.
    """
    fensapice_drop_dx: fensapice_drop_dx = fensapice_drop_dx
    """
    fensapice_drop_dx child of intake_fan_child.
    """
    fensapice_drop_dy: fensapice_drop_dy = fensapice_drop_dy
    """
    fensapice_drop_dy child of intake_fan_child.
    """
    fensapice_drop_dz: fensapice_drop_dz = fensapice_drop_dz
    """
    fensapice_drop_dz child of intake_fan_child.
    """
    fensapice_dpm_surface_injection: fensapice_dpm_surface_injection = fensapice_dpm_surface_injection
    """
    fensapice_dpm_surface_injection child of intake_fan_child.
    """
    fensapice_dpm_inj_nstream: fensapice_dpm_inj_nstream = fensapice_dpm_inj_nstream
    """
    fensapice_dpm_inj_nstream child of intake_fan_child.
    """
    fensapice_drop_icc: fensapice_drop_icc = fensapice_drop_icc
    """
    fensapice_drop_icc child of intake_fan_child.
    """
    fensapice_drop_ctemp: fensapice_drop_ctemp = fensapice_drop_ctemp
    """
    fensapice_drop_ctemp child of intake_fan_child.
    """
    fensapice_drop_cdiam: fensapice_drop_cdiam = fensapice_drop_cdiam
    """
    fensapice_drop_cdiam child of intake_fan_child.
    """
    fensapice_drop_cv: fensapice_drop_cv = fensapice_drop_cv
    """
    fensapice_drop_cv child of intake_fan_child.
    """
    fensapice_drop_cx: fensapice_drop_cx = fensapice_drop_cx
    """
    fensapice_drop_cx child of intake_fan_child.
    """
    fensapice_drop_cy: fensapice_drop_cy = fensapice_drop_cy
    """
    fensapice_drop_cy child of intake_fan_child.
    """
    fensapice_drop_cz: fensapice_drop_cz = fensapice_drop_cz
    """
    fensapice_drop_cz child of intake_fan_child.
    """
    fensapice_drop_vrh: fensapice_drop_vrh = fensapice_drop_vrh
    """
    fensapice_drop_vrh child of intake_fan_child.
    """
    fensapice_drop_vrh_1: fensapice_drop_vrh_1 = fensapice_drop_vrh_1
    """
    fensapice_drop_vrh_1 child of intake_fan_child.
    """
    fensapice_drop_vc: fensapice_drop_vc = fensapice_drop_vc
    """
    fensapice_drop_vc child of intake_fan_child.
    """
    mixing_plane_thread: mixing_plane_thread = mixing_plane_thread
    """
    mixing_plane_thread child of intake_fan_child.
    """
    wsf: wsf = wsf
    """
    wsf child of intake_fan_child.
    """
    wsb: wsb = wsb
    """
    wsb child of intake_fan_child.
    """
    wsn: wsn = wsn
    """
    wsn child of intake_fan_child.
    """
    solar_fluxes: solar_fluxes = solar_fluxes
    """
    solar_fluxes child of intake_fan_child.
    """
    solar_shining_factor: solar_shining_factor = solar_shining_factor
    """
    solar_shining_factor child of intake_fan_child.
    """
    radiating_s2s_surface: radiating_s2s_surface = radiating_s2s_surface
    """
    radiating_s2s_surface child of intake_fan_child.
    """
    ac_options: ac_options = ac_options
    """
    ac_options child of intake_fan_child.
    """
    impedance_0: impedance_0 = impedance_0
    """
    impedance_0 child of intake_fan_child.
    """
    impedance_1: impedance_1 = impedance_1
    """
    impedance_1 child of intake_fan_child.
    """
    impedance_2: impedance_2 = impedance_2
    """
    impedance_2 child of intake_fan_child.
    """
    ac_wave: ac_wave = ac_wave
    """
    ac_wave child of intake_fan_child.
    """
    les_spec: les_spec = les_spec
    """
    les_spec child of intake_fan_child.
    """
    a: a = a
    """
    a child of intake_fan_child.
    """
    swirl_model: swirl_model = swirl_model
    """
    swirl_model child of intake_fan_child.
    """
    swirl_factor: swirl_factor = swirl_factor
    """
    swirl_factor child of intake_fan_child.
    """
    fan_omega: fan_omega = fan_omega
    """
    fan_omega child of intake_fan_child.
    """
    fan_origin: fan_origin = fan_origin
    """
    fan_origin child of intake_fan_child.
    """
    strength: strength = strength
    """
    strength child of intake_fan_child.
    """
    new_fan_definition: new_fan_definition = new_fan_definition
    """
    new_fan_definition child of intake_fan_child.
    """
