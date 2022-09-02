#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .domain_val import domain_val
from .all_bndry_zones import all_bndry_zones
from .zone_list import zone_list
from .write_to_file import write_to_file
from .file_name_1 import file_name
from .append_data import append_data
from .overwrite import overwrite
class rad_heat_trans(Command):
    """
    Print radiation heat transfer rate at boundaries.
    
    Parameters
    ----------
        domain_val : str
            'domain_val' child.
        all_bndry_zones : bool
            Select all the boundary/interior zones.
        zone_list : typing.List[str]
            'zone_list' child.
        write_to_file : bool
            'write_to_file' child.
        file_name : str
            'file_name' child.
        append_data : bool
            'append_data' child.
        overwrite : bool
            'overwrite' child.
    
    """

    fluent_name = "rad-heat-trans"

    argument_names = \
        ['domain_val', 'all_bndry_zones', 'zone_list', 'write_to_file',
         'file_name', 'append_data', 'overwrite']

    domain_val: domain_val = domain_val
    """
    domain_val argument of rad_heat_trans.
    """
    all_bndry_zones: all_bndry_zones = all_bndry_zones
    """
    all_bndry_zones argument of rad_heat_trans.
    """
    zone_list: zone_list = zone_list
    """
    zone_list argument of rad_heat_trans.
    """
    write_to_file: write_to_file = write_to_file
    """
    write_to_file argument of rad_heat_trans.
    """
    file_name: file_name = file_name
    """
    file_name argument of rad_heat_trans.
    """
    append_data: append_data = append_data
    """
    append_data argument of rad_heat_trans.
    """
    overwrite: overwrite = overwrite
    """
    overwrite argument of rad_heat_trans.
    """
