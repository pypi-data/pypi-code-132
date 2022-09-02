#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .option import option
from .smooth import smooth
from .banded import banded
class coloring(Group):
    """
    'coloring' child.
    """

    fluent_name = "coloring"

    child_names = \
        ['option', 'smooth', 'banded']

    option: option = option
    """
    option child of coloring.
    """
    smooth: smooth = smooth
    """
    smooth child of coloring.
    """
    banded: banded = banded
    """
    banded child of coloring.
    """
