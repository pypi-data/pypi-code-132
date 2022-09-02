#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .project_filename import project_filename
class initialize(Command):
    """
    Start Parametric Study.
    
    Parameters
    ----------
        project_filename : str
            'project_filename' child.
    
    """

    fluent_name = "initialize"

    argument_names = \
        ['project_filename']

    project_filename: project_filename = project_filename
    """
    project_filename argument of initialize.
    """
