#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .retain_instantaneous_values import retain_instantaneous_values
from .scaled import scaled
from .report_type import report_type
from .average_over import average_over
from .per_zone import per_zone
from .thread_names import thread_names
from .thread_ids import thread_ids
from .old_props import old_props
from .reference_frame import reference_frame
from .mom_axis import mom_axis
from .mom_center import mom_center
class moment_child(Group):
    """
    'child_object_type' of moment.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['retain_instantaneous_values', 'scaled', 'report_type',
         'average_over', 'per_zone', 'thread_names', 'thread_ids',
         'old_props', 'reference_frame', 'mom_axis', 'mom_center']

    retain_instantaneous_values: retain_instantaneous_values = retain_instantaneous_values
    """
    retain_instantaneous_values child of moment_child.
    """
    scaled: scaled = scaled
    """
    scaled child of moment_child.
    """
    report_type: report_type = report_type
    """
    report_type child of moment_child.
    """
    average_over: average_over = average_over
    """
    average_over child of moment_child.
    """
    per_zone: per_zone = per_zone
    """
    per_zone child of moment_child.
    """
    thread_names: thread_names = thread_names
    """
    thread_names child of moment_child.
    """
    thread_ids: thread_ids = thread_ids
    """
    thread_ids child of moment_child.
    """
    old_props: old_props = old_props
    """
    old_props child of moment_child.
    """
    reference_frame: reference_frame = reference_frame
    """
    reference_frame child of moment_child.
    """
    mom_axis: mom_axis = mom_axis
    """
    mom_axis child of moment_child.
    """
    mom_center: mom_center = mom_center
    """
    mom_center child of moment_child.
    """
