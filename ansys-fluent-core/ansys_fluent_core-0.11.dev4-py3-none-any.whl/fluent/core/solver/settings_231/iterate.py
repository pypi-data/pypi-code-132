#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .number_of_iterations_1 import number_of_iterations
class iterate(Command):
    """
    Perform a specified number of iterations.
    
    Parameters
    ----------
        number_of_iterations : int
            Set incremental number of time steps.
    
    """

    fluent_name = "iterate"

    argument_names = \
        ['number_of_iterations']

    number_of_iterations: number_of_iterations = number_of_iterations
    """
    number_of_iterations argument of iterate.
    """
