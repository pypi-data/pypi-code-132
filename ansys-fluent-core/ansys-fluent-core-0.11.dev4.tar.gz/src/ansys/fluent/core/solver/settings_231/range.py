#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .option_9 import option
from .auto_range import auto_range
from .clip_to_range_1 import clip_to_range
class range(Group):
    """
    'range' child.
    """

    fluent_name = "range"

    child_names = \
        ['option', 'auto_range', 'clip_to_range']

    option: option = option
    """
    option child of range.
    """
    auto_range: auto_range = auto_range
    """
    auto_range child of range.
    """
    clip_to_range: clip_to_range = clip_to_range
    """
    clip_to_range child of range.
    """
