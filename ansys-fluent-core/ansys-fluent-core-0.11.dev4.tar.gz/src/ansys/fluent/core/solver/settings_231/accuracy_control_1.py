#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .option_9 import option
from .step_size import step_size
from .tolerance_1 import tolerance
class accuracy_control(Group):
    """
    'accuracy_control' child.
    """

    fluent_name = "accuracy-control"

    child_names = \
        ['option', 'step_size', 'tolerance']

    option: option = option
    """
    option child of accuracy_control.
    """
    step_size: step_size = step_size
    """
    step_size child of accuracy_control.
    """
    tolerance: tolerance = tolerance
    """
    tolerance child of accuracy_control.
    """
