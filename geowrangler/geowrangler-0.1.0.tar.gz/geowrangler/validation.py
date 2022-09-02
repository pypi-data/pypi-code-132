# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/01_validation.ipynb (unless otherwise specified).

__all__ = [
    "ValidationError",
    "BaseValidator",
    "OrientationValidator",
    "CrsBoundsValidator",
    "SelfIntersectingValidator",
    "NullValidator",
    "AreaValidator",
    "GeometryValidation",
]


# Internal Cell
import logging
import warnings
from abc import ABC, abstractmethod
from typing import Sequence, Union

import geopandas as gpd
import pandas as pd
from fastcore.basics import patch
from shapely import validation as shapely_validation
from shapely.algorithms.cga import signed_area
from shapely.geometry.base import BaseGeometry
from shapely.geometry.multipolygon import MultiPolygon
from shapely.geometry.polygon import orient

logger = logging.getLogger(__name__)

# Cell
class ValidationError(Exception):
    pass


# Cell
class BaseValidator(ABC):
    """Abstract Base Class for single validator"""

    fix_available = True
    warning_message = "Geometry errors found"
    geometry_types = None

    def __init__(
        self,
        add_new_column: bool = True,  # Add new column to show errors
        apply_fix: bool = True,  # Update geometry
    ):
        self.add_new_column = add_new_column
        self.apply_fix = apply_fix

    @property
    @abstractmethod
    def validator_column_name(self):  # pragma: no cover
        pass

    def get_check_arguments(
        self, gdf: gpd.GeoDataFrame  # GeoDataFrame to check
    ) -> dict:
        return {}

    def check(
        self,
        geometry: BaseGeometry,  # Geometry to check
        gdf: gpd.GeoDataFrame,  # GeoDataFrame to check
    ) -> bool:  # pragma: no cover
        pass

    def fix(self, geometry: BaseGeometry):  # pragma: no cover
        pass

    def skip(self, geometry: BaseGeometry):
        """Checks whether to skip the check. Used for skipping check that only works for certain types."""
        # Skip everything not geometry
        if not isinstance(geometry, BaseGeometry):
            return True
        # If nothing is specified always, run validator for all types
        elif self.geometry_types is None:
            return False
        elif geometry.geom_type in self.geometry_types:
            return False
        else:
            return True


# Cell


@patch
def validate(
    self: BaseValidator,
    gdf: gpd.GeoDataFrame,  # GeoDataFrame to validate
    clone=True,  # Apply validation to copy
) -> gpd.GeoDataFrame:
    """Method that checks the validity of a each geometry and applies a fix to these geometries or raise a warning"""
    if clone:
        gdf = gdf.copy()
    check_arguments = self.get_check_arguments(gdf)
    is_valid = gdf.geometry.apply(
        lambda g: self.skip(g) or self.check(g, **check_arguments),
    )
    if self.add_new_column:
        gdf[self.validator_column_name] = is_valid

    # For cases where no fix is available, run warning instead of applying fixes
    if (not self.fix_available) and (~is_valid.all()):
        warnings.warn(self.warning_message)
    # Fix geometries
    elif self.apply_fix:
        gdf.loc[~is_valid, "geometry"] = gdf[~is_valid].geometry.apply(self.fix)
    return gdf


# Cell


class OrientationValidator(BaseValidator):
    """Checks and fixes Orientation of the geometry to ensure it follows a counter-clockwise orientation"""

    validator_column_name = "is_oriented_properly"
    geometry_types = ["MultiPolygon", "Polygon"]


# Cell
@patch
def check(
    self: OrientationValidator, geometry: BaseGeometry  # Geometry to validate
) -> bool:
    """Checks if orientation is counter clockwise"""
    if geometry.geom_type == "Polygon":
        return signed_area(geometry.exterior) >= 0
    elif geometry.geom_type == "MultiPolygon":
        return all([signed_area(g.exterior) >= 0 for g in geometry.geoms])


# Cell
@patch
def fix(
    self: OrientationValidator, geometry: BaseGeometry  # Geometry to fix
) -> BaseGeometry:
    """Fixes orientation if orientation is clockwise"""
    if geometry.geom_type == "Polygon":
        return orient(geometry)
    elif geometry.geom_type == "MultiPolygon":
        return MultiPolygon([orient(g) for g in geometry.geoms])


# Cell


class CrsBoundsValidator(BaseValidator):
    """Checks bounds of the geometry to ensure it is within bounds of the crs"""

    validator_column_name = "is_within_crs_bounds"
    fix_available = False
    warning_message = "Found geometries out of bounds from crs"


# Cell


@patch
def get_check_arguments(
    self: CrsBoundsValidator, gdf: gpd.GeoDataFrame  # GeoDataFrame to check
) -> dict:
    """Return check arguments"""
    return {"gdf": gdf}


# Cell


@patch
def check(
    self: CrsBoundsValidator,
    geometry: BaseGeometry,  # Geometry to validate
    gdf: gpd.GeoDataFrame,  # GeoDataframe to check
) -> bool:
    """Checks if polygon is within bounds of crs."""
    # If area of use or crs is not defined, mark check as failed
    if gdf.crs is None or gdf.crs.area_of_use is None:
        return False
    xmin, ymin, xmax, ymax = gdf.crs.area_of_use.bounds
    b_xmin, b_ymin, b_xmax, b_ymax = geometry.bounds
    return (
        (b_xmin >= xmin) and (b_ymin >= ymin) and (b_xmax <= xmax) and (b_ymax <= ymax)
    )


# Cell
@patch
def fix(
    self: CrsBoundsValidator, geometry: BaseGeometry  # Geometry to fix
) -> BaseGeometry:  # pragma: no cover
    """No fix available"""
    return geometry


# Cell


class SelfIntersectingValidator(BaseValidator):
    """Checks bounds of the geometry to ensure it is within bounds or crs"""

    validator_column_name = "is_not_self_intersecting"


# Cell
@patch
def check(
    self: SelfIntersectingValidator, geometry: BaseGeometry  # Geometry to check
) -> bool:
    explanation = shapely_validation.explain_validity(geometry)
    return "Self-intersection" not in explanation


# Cell
@patch
def fix(self: SelfIntersectingValidator, geometry: BaseGeometry) -> BaseGeometry:
    """Fix intersection geometry by applying shapely.validation.make_valid"""
    return shapely_validation.make_valid(geometry)


# Cell


class NullValidator(BaseValidator):
    """Checks bounds of the geometry to ensure it is within bounds or crs"""

    validator_column_name = "is_not_null"
    fix_available = False
    warning_message = "Found null geometries"
    geometry_types = [None]

    # special case where we want to run the validator on non geometries
    def skip(self, geometry: BaseGeometry):
        return False


# Cell
@patch
def check(self: NullValidator, geometry: BaseGeometry) -> bool:  # Geometry to check
    """Checks if polygon is null"""
    return not pd.isnull(geometry)


# Cell
@patch
def fix(
    self: NullValidator, geometry: BaseGeometry  # Geometry to fix
) -> BaseGeometry:  # pragma: no cover
    """No fix available"""
    return geometry


# Cell
class AreaValidator(BaseValidator):
    """Checks area of the geometry to ensure it greater than 0"""

    validator_column_name = "area_is_not_zero"
    fix_available = False
    warning_message = "Found geometries with area equals or less than zero"
    geometry_types = ["MultiPolygon", "Polygon"]


# Cell
@patch
def check(self: AreaValidator, geometry: BaseGeometry) -> bool:
    """Checks if area is greater than 0"""
    return geometry.area > 0


# Cell
@patch
def fix(
    self: AreaValidator, geometry: BaseGeometry  # Geometry to fix
) -> BaseGeometry:  # pragma: no cover
    """No fix available"""
    return geometry


# Cell


class GeometryValidation:
    """Applies a list of validation checks and tries to fix them"""

    validators_map = {
        "orientation": OrientationValidator,
        "crs_bounds": CrsBoundsValidator,
        "self_intersecting": SelfIntersectingValidator,
        "null": NullValidator,
        "area": AreaValidator,
    }

    def __init__(
        self,
        gdf: gpd.GeoDataFrame,  # GeoDataFrame to validate
        validators: Sequence[Union[str, BaseValidator]] = (  # Validators to apply
            "null",
            "self_intersecting",
            "orientation",
            "crs_bounds",
            "area",
        ),
        add_validation_columns: bool = True,  # Add column to show errors
        apply_fixes: bool = True,  # Update geometry
    ) -> gpd.GeoDataFrame:
        self.gdf = gdf
        self.validators = validators
        self.add_validation_columns = add_validation_columns
        self.apply_fixes = apply_fixes

    def _get_validators(self) -> Sequence[BaseValidator]:
        """Gets a list of Validator Classes based on string"""
        validators_classes = []
        for validator in self.validators:
            if isinstance(validator, str):
                if validator not in self.validators_map:
                    raise ValidationError("Invalid validator.")
                validators_classes.append(self.validators_map[validator])
            elif issubclass(validator, BaseValidator):
                validators_classes.append(validator)
            else:
                raise ValidationError("Invalid validator.")
        return validators_classes


# Cell


@patch
def validate_all(self: GeometryValidation) -> gpd.GeoDataFrame:
    """Sequentially run validators"""
    validators = self._get_validators()
    gdf = self.gdf
    for validator in validators:
        gdf = validator(
            add_new_column=self.add_validation_columns,
            apply_fix=self.apply_fixes,
        ).validate(gdf)
    return gdf
