#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .filepath import filepath
class export_design_table(Command):
    """
    Export Design Point Table.
    
    Parameters
    ----------
        filepath : str
            'filepath' child.
    
    """

    fluent_name = "export-design-table"

    argument_names = \
        ['filepath']

    filepath: filepath = filepath
    """
    filepath argument of export_design_table.
    """
