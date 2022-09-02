#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .iter_count_3 import iter_count
from .time_steps_count_1 import time_steps_count
from .fluid_time_step_count import fluid_time_step_count
from .iter_per_time_step_count import iter_per_time_step_count
class iterate(Command):
    """
    Iteration the multidomain conjugate heat transfer.
    
    Parameters
    ----------
        iter_count : int
            'iter_count' child.
        time_steps_count : int
            'time_steps_count' child.
        fluid_time_step_count : int
            'fluid_time_step_count' child.
        iter_per_time_step_count : int
            'iter_per_time_step_count' child.
    
    """

    fluent_name = "iterate"

    argument_names = \
        ['iter_count', 'time_steps_count', 'fluid_time_step_count',
         'iter_per_time_step_count']

    iter_count: iter_count = iter_count
    """
    iter_count argument of iterate.
    """
    time_steps_count: time_steps_count = time_steps_count
    """
    time_steps_count argument of iterate.
    """
    fluid_time_step_count: fluid_time_step_count = fluid_time_step_count
    """
    fluid_time_step_count argument of iterate.
    """
    iter_per_time_step_count: iter_per_time_step_count = iter_per_time_step_count
    """
    iter_per_time_step_count argument of iterate.
    """
