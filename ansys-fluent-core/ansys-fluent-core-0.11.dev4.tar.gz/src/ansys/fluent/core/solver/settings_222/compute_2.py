#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .report_defs import report_defs
class compute(Command):
    """
    'compute' command.
    
    Parameters
    ----------
        report_defs : typing.List[str]
            'report_defs' child.
    
    """

    fluent_name = "compute"

    argument_names = \
        ['report_defs']

    report_defs: report_defs = report_defs
    """
    report_defs argument of compute.
    """
