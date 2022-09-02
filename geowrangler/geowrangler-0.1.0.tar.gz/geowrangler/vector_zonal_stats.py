# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/02_vector_zonal_stats.ipynb (unless otherwise specified).

__all__ = ["create_zonal_stats", "compute_quadkey", "create_bingtile_zonal_stats"]


# Internal Cell
GEO_INDEX_NAME = "__GeoWrangleer_aoi_index"

# Cell
from functools import partial
from typing import Any, Dict, List

import geopandas as gpd
import morecantile
import numpy as np
import pandas as pd

# Internal Cell
def _fix_agg(
    agg: Dict[str, Any],  # A dict containing at the minimum a 'func' key
) -> Dict[str, Any]:
    """
    Fix an `agg spec`.

    It outputs a dict containing the following keys:
      - 'func': a list of aggregation functions (should be a valid 'agg' function)
      - 'column': a column to apply the aggregation functions (should be a valid numeric column in data)
      - 'output': the names of the new columns containing the application of the aggregation functions (default: concat column + '_' + func)
      - 'fillna': boolean list whether to replace new columns with 'NA' values  with 0 (default: False)
    """
    if "func" not in agg:
        return agg  # skip fix as agg spec is invalid

    if type(agg["func"]) == str:
        agg["func"] = [agg["func"]]

    # optional column, default to index count
    if "column" not in agg:
        agg["column"] = GEO_INDEX_NAME

    if "output" not in agg:
        column = "index" if agg["column"] == GEO_INDEX_NAME else agg["column"]
        agg["output"] = [f"{column}_{f}" for f in agg["func"]]

    if type(agg["output"]) == str:
        agg["output"] = [agg["output"]]

    # check matching fillna
    if "fillna" not in agg:
        agg["fillna"] = [False for _ in agg["func"]]

    if type(agg["fillna"]) == bool:
        agg["fillna"] = [agg["fillna"]]

    return agg


# Internal Cell
def _check_agg(
    agg: Dict[str, Any],  # A dict containing at the minimum a 'func' key
    i: int,  # The index into the list of aggregations
    data_cols: List[str],  # list of data columns
    dtypes: pd.Series,  # series of dtypes with column names as index
) -> None:
    """
    Validate an `agg spec`.
    """

    if "func" not in agg:
        raise ValueError(f"Missing key 'func' in agg[{i}] {agg}")

    for func in agg["func"]:
        if getattr(pd.Series, func, None) is None:
            raise ValueError(f"Unknown func '{func}' in agg[{i}] {agg}")

    if agg["column"] != GEO_INDEX_NAME and agg["column"] not in data_cols:
        raise ValueError(
            f"Column '{agg['column']}' in agg[{i}] {agg} does not exist in the data"
        )

    if agg["column"] != GEO_INDEX_NAME and not np.issubdtype(
        dtypes.loc[agg["column"]], np.number
    ):
        raise ValueError(
            f"Column '{agg['column']}' in agg[{i}] {agg} is not a numeric column in the data"
        )

    if len(agg["func"]) != len(agg["output"]):
        raise ValueError(
            f"output list {agg['output']} doesn't match func list {agg['func']} in agg[{i}] {agg}"
        )

    # check matching fillna
    if len(agg["fillna"]) != len(agg["func"]):
        raise ValueError(
            f"fillna list {agg['fillna']} doesn't match func list {agg['func']} in agg[{i}] {agg}"
        )


# Internal Cell
def _validate_aggs(
    fixed_aggs: List[Dict[str, Any]],  # A list of fixed agg specs
    data: pd.DataFrame,  # Source dataframe
) -> None:
    data_cols = list(data.columns.values)
    outputs = []
    for i, agg in enumerate(fixed_aggs):
        _check_agg(agg, i, data_cols, data.dtypes)
        # check duplicate outputs
        if any(item in agg["output"] for item in outputs):
            raise ValueError(
                f"Duplicate output column name found for agg[{i}] {agg['output']}"
            )
        outputs += agg["output"]


# Internal Cell
def _validate_aoi(
    aoi: pd.DataFrame,  # Source dataframe
) -> None:
    if isinstance(aoi.index, pd.MultiIndex):
        raise ValueError(
            "AOI has a pandas.MultiIndex. Please convert the index to a single level such as pd.RangeIndex"
        )


# Internal Cell
def _expand_aggs(
    aggs: List[Dict[str, Any]],  # List of fixed valid aggs
) -> List[Dict[str, Any]]:
    """Expands agg specs with multiple funcs each into a separate agg spec"""
    expanded_aggs = []
    for agg in aggs:
        for i, func in enumerate(agg["func"]):
            expanded_agg = {
                "func": func,
                "column": agg["column"],
                "output": agg["output"][i],
                "fillna": agg["fillna"][i],
            }
            expanded_aggs += [expanded_agg]
    return expanded_aggs


# Internal Cell
def _build_agg_args(
    aggs: List[Dict[str, Any]],  # A list of expanded aggs
) -> Dict:
    """Builds a dict of args with output as key and a tuple of column and func as value from a list of expanded aggs"""
    return {agg["output"]: (agg["column"], agg["func"]) for agg in aggs}


# Internal Cell


def _prep_aoi(
    aoi: pd.DataFrame,  # Area of interest
) -> pd.DataFrame:
    """
    Prepare aoi for spatial join
      - create a column  from aoi's index which will be used as grouping key
    """
    if GEO_INDEX_NAME in list(aoi.columns.values):
        raise ValueError(
            f"Invalid column name error: AOI column should not match Geowrangler index column {GEO_INDEX_NAME}"
        )
    # prep for spatial join
    aoi = aoi.copy()
    aoi.index.name = GEO_INDEX_NAME

    # create index col for broadcast to features
    aoi.reset_index(
        level=0, inplace=True
    )  # index added as new column named GEO_INDEX_NAME
    return aoi


# Internal Cell


def _fillnas(
    expanded_aggs: List[Dict[str, Any]],  # list of expanded aggs
    results: pd.DataFrame,  # results dataframe to be filled with NAs if flag set
    aoi: pd.DataFrame,  # aoi dataframe to merge it back to
):
    # set NAs to 0 if fillna
    for agg in expanded_aggs:
        if agg["fillna"]:
            colname = agg["output"]
            if colname in list(aoi.columns.values):
                colname = colname + "_y"  # try if merged df has colname + _y
            if colname in list(results.columns.values):
                results[colname].fillna(0, inplace=True)


# Internal Cell


def _aggregate_stats(
    aoi: pd.DataFrame,  # Area of interest
    groups: pd.core.groupby.DataFrameGroupBy,  # Source data aggregated into groups by GEO_INDEX_NAME
    expanded_aggs: List[Dict[str, Any]],  # A list of expanded aggs
) -> pd.DataFrame:
    """Aggregate groups and compute the agg['func'] for agg['column'], map them to the output column in agg['column'] for all the aggs in the expanded_aggs list
    and merge them back to aoi dataframe
    """
    agg_dicts = _build_agg_args(expanded_aggs)
    aggregates = groups.agg(**agg_dicts)
    results = aoi.merge(
        aggregates, how="left", on=GEO_INDEX_NAME, suffixes=(None, "_y")
    )
    _fillnas(expanded_aggs, results, aoi)

    return results


# Cell


def create_zonal_stats(
    aoi: gpd.GeoDataFrame,  # Area of interest for which zonal stats are to be computed for
    data: gpd.GeoDataFrame,  # Source gdf containing data to compute zonal stats from
    aggregations: List[  # List of agg specs, with each agg spec applied to a data column
        Dict[str, Any]
    ],
    overlap_method: str = "intersects",  # spatial predicate to used in spatial join of aoi and data [geopandas.sjoin](https://geopandas.org/en/stable/docs/user_guide/mergingdata.html#binary-predicate-joins) for more details
    # categorical_column_options: str = None,
) -> gpd.GeoDataFrame:
    """
    Create zonal stats for area of interest from data using aggregration operations on data columns.
    Returns the same aoi with additional columns containing the computed zonal features.
    """
    _validate_aoi(aoi)
    fixed_aggs = [_fix_agg(agg) for agg in aggregations]

    _validate_aggs(fixed_aggs, data)

    # prep for spatial join
    aoi_index_name = aoi.index.name
    aoi = _prep_aoi(aoi)

    if not data.crs.equals(aoi.crs):
        data = data.to_crs(aoi.crs)

    # spatial join - broadcast aoi_index to data => features
    features = gpd.sjoin(
        aoi[[GEO_INDEX_NAME, "geometry"]], data, how="inner", predicate=overlap_method
    )

    # group
    groups = features.groupby(GEO_INDEX_NAME)

    # apply all aggregations all at once
    expanded_aggs = _expand_aggs(fixed_aggs)
    results = _aggregate_stats(aoi, groups, expanded_aggs)

    # cleanup results
    results.set_index(GEO_INDEX_NAME, inplace=True)
    results.index.name = aoi_index_name

    return results


# Internal Cell

tms = morecantile.tms.get("WebMercatorQuad")  # Tile Matrix for Bing Maps

# Internal Cell


def get_quadkey(geometry, zoom_level):
    return tms.quadkey(tms.tile(geometry.x, geometry.y, zoom_level))


# Cell


def compute_quadkey(
    data: gpd.GeoDataFrame,  # The geodataframe
    zoom_level: int,  # The quadkey zoom level (1-23)
    inplace: bool = False,  # Whether to change data inplace or not
    quadkey_column: str = "quadkey",  # The name of the quadkey output column
) -> gpd.GeoDataFrame:
    """
    Computes the quadkeys for the geometries of the data.
    If geometries are not points, the quadkeys are computed
    from the centroids of the geometries.
    """

    data = data if inplace else data.copy()

    get_zoom_quadkey = partial(get_quadkey, zoom_level=zoom_level)

    if data.crs.is_geographic:
        centroids = data.to_crs("EPSG:3857").geometry.centroid  # planar
        centroids = centroids.to_crs(data.crs)
    else:
        centroids = data.geometry.centroid
        centroids = centroids.to_crs("EPSG:4326")  # use geographic

    data[quadkey_column] = centroids.apply(get_zoom_quadkey)

    return data


# Internal Cell


def validate_aoi_quadkey(aoi, aoi_quadkey_column) -> None:

    if aoi_quadkey_column not in list(aoi.columns.values):
        raise ValueError(
            f"aoi_quadkey_column '{aoi_quadkey_column}' is not in list of aoi columns: {list(aoi.columns.values)}"
        )
    if len(aoi) == 0:
        raise ValueError("aoi dataframe is empty")

    aoi_zoom_level = len(aoi[aoi_quadkey_column].iloc[0])
    if not (aoi[aoi_quadkey_column].apply(len) == aoi_zoom_level).all(axis=None):
        raise ValueError("aoi quadkey levels are not all at the same level")


def validate_data_quadkey(data, data_quadkey_column, min_zoom_level):
    if data_quadkey_column not in list(data.columns.values):
        raise ValueError(
            f"data_quadkey_column '{data_quadkey_column}' is not in list of data columns: {list(data.columns.values)}"
        )
    if len(data) == 0:
        raise ValueError("data dataframe is empty")

    if not (data[data_quadkey_column].apply(len) >= min_zoom_level).all(axis=0):
        raise ValueError(
            f"data quadkey levels cannot be less than aoi quadkey level {min_zoom_level}"
        )


# Cell


def create_bingtile_zonal_stats(
    aoi: pd.DataFrame,  # An aoi with quadkey column
    data: pd.DataFrame,  # Data with  quadkey column
    aggregations: List[  # List of agg specs, with each agg spec applied to a data column
        Dict[str, Any]
    ],
    aoi_quadkey_column: str = "quadkey",  # Column name of aoi quadkey
    data_quadkey_column: str = "quadkey",  # Column name of data quadkey
) -> pd.DataFrame:

    # validate aoi zoom level is same for all rows
    validate_aoi_quadkey(aoi, aoi_quadkey_column)
    # get aoi zoom level
    aoi_zoom_level = len(aoi[aoi_quadkey_column].iloc[0])

    validate_data_quadkey(data, data_quadkey_column, aoi_zoom_level)

    fixed_aggs = [_fix_agg(agg) for agg in aggregations]

    _validate_aggs(fixed_aggs, data)

    # create aoi level quad_key for data (apply quadkey_to_tile)
    def quadkey4zoom_level(x):
        return x[:aoi_zoom_level]

    data = data.copy()
    data[GEO_INDEX_NAME] = data[data_quadkey_column].apply(quadkey4zoom_level)

    # filter data to include only those whose quadkeys are in aoi quadkeys
    features = data.join(
        aoi[[aoi_quadkey_column]].set_index(aoi_quadkey_column),
        how="inner",
        on=GEO_INDEX_NAME,
    )

    # groupby data on aoi level quad key
    groups = features.groupby(GEO_INDEX_NAME)

    expanded_aggs = _expand_aggs(fixed_aggs)
    aoi = aoi.copy()
    aoi[GEO_INDEX_NAME] = aoi[aoi_quadkey_column]

    results = _aggregate_stats(aoi, groups, expanded_aggs)

    results.drop(columns=[GEO_INDEX_NAME], inplace=True)

    return results
