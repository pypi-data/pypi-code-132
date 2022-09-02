#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .enable_fast_mode import enable_fast_mode
from .enable_memory_saving_mode import enable_memory_saving_mode
from .disable_warped_face_gradient_correction import disable_warped_face_gradient_correction
class enable(Group):
    """
    'enable' child.
    """

    fluent_name = "enable?"

    child_names = \
        ['enable_fast_mode', 'enable_memory_saving_mode']

    enable_fast_mode: enable_fast_mode = enable_fast_mode
    """
    enable_fast_mode child of enable.
    """
    enable_memory_saving_mode: enable_memory_saving_mode = enable_memory_saving_mode
    """
    enable_memory_saving_mode child of enable.
    """
    command_names = \
        ['disable_warped_face_gradient_correction']

    disable_warped_face_gradient_correction: disable_warped_face_gradient_correction = disable_warped_face_gradient_correction
    """
    disable_warped_face_gradient_correction command of enable.
    """
