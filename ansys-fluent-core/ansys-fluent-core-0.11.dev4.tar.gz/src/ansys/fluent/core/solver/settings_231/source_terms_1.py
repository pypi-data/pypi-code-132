#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from .source_terms_child import source_terms_child

class source_terms(NamedObject[source_terms_child], _CreatableNamedObjectMixin[source_terms_child]):
    """
    'source_terms' child.
    """

    fluent_name = "source-terms"

    child_object_type: source_terms_child = source_terms_child
    """
    child_object_type of source_terms.
    """
