"""Select overlapping time slices for training"""
from typing import Iterable

import pandas as pd
from torchdata.datapipes import functional_datapipe
from torchdata.datapipes.iter import IterDataPipe, Zipper


@functional_datapipe("select_overlapping_time_slice")
class SelectOverlappingTimeSliceIterDataPipe(IterDataPipe):
    """Source DataPipes are from the contiguous_time_period"""

    def __init__(self, source_datapipes: Iterable[IterDataPipe]):
        """
        Source DataPipes are from the contiguous_time_period

        Args:
            source_datapipes: Datapipes to compute the intersection of
        """
        super().__init__()
        self.source_datapipes = source_datapipes

    def __iter__(self) -> pd.DataFrame:
        for set_of_pd_datas in Zipper(*self.source_datapipes):
            yield intersection_of_multiple_dataframes_of_periods(list(*set_of_pd_datas))


def intersection_of_multiple_dataframes_of_periods(
    time_periods: list[pd.DataFrame],
) -> pd.DataFrame:
    """Find the intersection of a list of time periods.

    See the docstring of intersection_of_2_dataframes_of_periods() for more details.
    """
    assert len(time_periods) > 0
    if len(time_periods) == 1:
        return time_periods[0]
    intersection = intersection_of_2_dataframes_of_periods(time_periods[0], time_periods[1])
    for time_period in time_periods[2:]:
        intersection = intersection_of_2_dataframes_of_periods(intersection, time_period)
    return intersection


def intersection_of_2_dataframes_of_periods(a: pd.DataFrame, b: pd.DataFrame) -> pd.DataFrame:
    """Find the intersection of two pd.DataFrames of time periods.

    Each row of each pd.DataFrame represents a single time period.  Each pd.DataFrame has
    two columns: `start_dt` and `end_dt` (where 'dt' is short for 'datetime').

    A typical use-case is that each pd.DataFrame represents all the time periods where
    a `DataSource` has contiguous, valid data.

    Here's a graphical example of two pd.DataFrames of time periods and their intersection:

                 ----------------------> TIME ->---------------------
               a: |-----|   |----|     |----------|     |-----------|
               b:    |--------|                       |----|    |---|
    intersection:    |--|   |-|                         |--|    |---|

    Args:
        a, b: pd.DataFrame where each row represents a time period.  The pd.DataFrame has
        two columns: start_dt and end_dt.

    Returns:
        Sorted list of intersecting time periods represented as a pd.DataFrame with two columns:
        start_dt and end_dt.
    """
    if a.empty or b.empty:
        return pd.DataFrame(columns=["start_dt", "end_dt"])

    all_intersecting_periods = []
    for a_period in a.itertuples():
        # Five ways in which two periods may overlap:
        # a: |----| or |---|   or  |---| or   |--|   or |-|
        # b:  |--|       |---|   |---|      |------|    |-|
        # In all five, `a` must always start before `b` ends,
        # and `a` must always end after `b` starts:
        overlapping_periods = b[(a_period.start_dt < b.end_dt) & (a_period.end_dt > b.start_dt)]

        # There are two ways in which two periods may *not* overlap:
        # a: |---|        or        |---|
        # b:       |---|      |---|
        # `overlapping` will not include periods which do *not* overlap.

        # Now find the intersection of each period in `overlapping_periods` with
        # the period from `a` that starts at `a_start_dt` and ends at `a_end_dt`.
        # We do this by clipping each row of `overlapping_periods`
        # to start no earlier than `a_start_dt`, and end no later than `a_end_dt`.

        # First, make a copy, so we don't clip the underlying data in `b`.
        intersecting_periods = overlapping_periods.copy()
        intersecting_periods.start_dt.clip(lower=a_period.start_dt, inplace=True)
        intersecting_periods.end_dt.clip(upper=a_period.end_dt, inplace=True)

        all_intersecting_periods.append(intersecting_periods)

    all_intersecting_periods = pd.concat(all_intersecting_periods)
    return all_intersecting_periods.sort_values(by="start_dt").reset_index(drop=True)
