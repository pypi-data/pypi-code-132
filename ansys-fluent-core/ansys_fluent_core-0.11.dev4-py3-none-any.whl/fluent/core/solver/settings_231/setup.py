#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .general import general
from .models_1 import models
from .materials import materials
from .cell_zone_conditions import cell_zone_conditions
from .boundary_conditions import boundary_conditions
from .reference_values import reference_values
from .named_expressions import named_expressions
class setup(Group):
    """
    'setup' child.
    """

    fluent_name = "setup"

    child_names = \
        ['general', 'models', 'materials', 'cell_zone_conditions',
         'boundary_conditions', 'reference_values', 'named_expressions']

    general: general = general
    """
    general child of setup.
    """
    models: models = models
    """
    models child of setup.
    """
    materials: materials = materials
    """
    materials child of setup.
    """
    cell_zone_conditions: cell_zone_conditions = cell_zone_conditions
    """
    cell_zone_conditions child of setup.
    """
    boundary_conditions: boundary_conditions = boundary_conditions
    """
    boundary_conditions child of setup.
    """
    reference_values: reference_values = reference_values
    """
    reference_values child of setup.
    """
    named_expressions: named_expressions = named_expressions
    """
    named_expressions child of setup.
    """
