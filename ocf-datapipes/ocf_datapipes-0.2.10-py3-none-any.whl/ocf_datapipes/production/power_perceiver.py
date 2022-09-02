"""Wrapper for Power Perceiver Production Data Pipeline"""
import logging
from datetime import timedelta
from pathlib import Path
from typing import Union

import xarray
from torchdata.datapipes import functional_datapipe
from torchdata.datapipes.iter import IterDataPipe

import ocf_datapipes  # noqa
from ocf_datapipes.batch import MergeNumpyModalities
from ocf_datapipes.config.model import Configuration
from ocf_datapipes.load import (
    OpenConfiguration,
    OpenGSP,
    OpenNWP,
    OpenPVFromDB,
    OpenSatellite,
    OpenTopography,
)
from ocf_datapipes.utils.consts import NWP_MEAN, NWP_STD, SAT_MEAN, SAT_STD, BatchKey

logger = logging.getLogger(__name__)
xarray.set_options(keep_attrs=True)


@functional_datapipe("gsp_iterator")
class GSPIterator(IterDataPipe):
    """GSP iterator for live that goes one by one through GSPs"""

    def __init__(self, source_datapipe: IterDataPipe):
        """
        GSP iterator for live that goes one by one through GSPs

        Args:
            source_datapipe: Source datapipe to use
        """
        super().__init__()
        self.source_datapipe = source_datapipe

    def __iter__(self):
        """GSP iterator for live that goes one by one through GSPs"""
        for xr_dataset in self.source_datapipe:
            # Iterate through all locations in dataset
            for location_idx in range(len(xr_dataset["x_osgb"])):
                yield xr_dataset.isel(gsp_id=slice(location_idx, location_idx + 1))


def power_perceiver_production_datapipe(configuration_filename: Union[Path, str]) -> IterDataPipe:
    """
    Create the Power Perceiver production pipeline using a configuration

    Args:
        configuration_filename: Name of the configuration

    Returns:
        DataPipe ready to be put in a Dataloader for production
    """
    ####################################
    #
    # Equivalent to PP's loading and filtering methods
    #
    #####################################
    # Normalize GSP and PV on whole dataset here
    config_dp = OpenConfiguration(configuration_filename)
    # TODO Pass the configuration through all the datapipes instead?
    configuration: Configuration = next(iter(config_dp))

    logger.debug("Opening Datasets")
    sat_hrv_dp = OpenSatellite(
        zarr_path=configuration.input_data.hrvsatellite.hrvsatellite_zarr_path
    )
    passiv_dp = OpenPVFromDB(
        providers=[pv_files.label for pv_files in configuration.input_data.pv.pv_files_groups],
        load_extra_minutes=configuration.input_data.pv.live_load_extra_minutes,
        history_minutes=configuration.input_data.pv.history_minutes,
    )
    nwp_dp = OpenNWP(configuration.input_data.nwp.nwp_zarr_path)
    topo_dp = OpenTopography(configuration.input_data.topographic.topographic_filename)
    gsp_dp = OpenGSP(configuration.input_data.gsp.gsp_zarr_path)

    logger.debug("Normalize GSP data")
    gsp_dp = gsp_dp.normalize(
        normalize_fn=lambda x: x / x.capacity_mwp
    ).add_t0_idx_and_sample_period_duration(
        sample_period_duration=timedelta(minutes=30),
        history_duration=timedelta(minutes=configuration.input_data.gsp.history_minutes),
    )
    logger.debug("Getting locations")
    location_dp1, location_dp2, location_dp3 = gsp_dp.location_picker(
        return_all_locations=True
    ).fork(3)

    logger.debug("Got locations")

    logger.debug("Making PV space slice")
    passiv_dp, pv_t0_dp = (
        passiv_dp.normalize(normalize_fn=lambda x: x / x.capacity_wp)
        .add_t0_idx_and_sample_period_duration(
            sample_period_duration=timedelta(minutes=5),
            history_duration=timedelta(minutes=configuration.input_data.pv.history_minutes),
        )
        .select_spatial_slice_meters(
            location_datapipe=location_dp1,
            roi_width_meters=configuration.input_data.pv.pv_image_size_meters_width,
            roi_height_meters=configuration.input_data.pv.pv_image_size_meters_height,
        )
        .ensure_n_pv_systems_per_example(
            n_pv_systems_per_example=configuration.input_data.pv.n_pv_systems_per_example
        )
        .fork(2)
    )
    topo_dp = topo_dp.reproject_topography().normalize(calculate_mean_std_from_example=True)
    sat_hrv_dp, sat_t0_dp = (
        sat_hrv_dp.convert_satellite_to_int8()
        .add_t0_idx_and_sample_period_duration(
            sample_period_duration=timedelta(minutes=5),
            history_duration=timedelta(
                minutes=configuration.input_data.hrvsatellite.history_minutes
            ),
        )
        .select_spatial_slice_pixels(
            location_datapipe=location_dp2,
            roi_width_pixels=configuration.input_data.hrvsatellite.hrvsatellite_image_size_pixels_width,  # noqa
            roi_height_pixels=configuration.input_data.hrvsatellite.hrvsatellite_image_size_pixels_height,  # noqa
            y_dim_name="y_geostationary",
            x_dim_name="x_geostationary",
        )
        .fork(2)
    )

    logger.debug("Making NWP space slice")
    nwp_dp, nwp_t0_dp = (
        nwp_dp.add_t0_idx_and_sample_period_duration(
            sample_period_duration=timedelta(hours=1),
            history_duration=timedelta(minutes=configuration.input_data.nwp.history_minutes),
        )
        .select_spatial_slice_pixels(
            location_datapipe=location_dp3,
            roi_width_pixels=configuration.input_data.nwp.nwp_image_size_pixels_width
            * 16,  # TODO What to do here with configurations and such
            roi_height_pixels=configuration.input_data.nwp.nwp_image_size_pixels_height * 16,
            y_dim_name="y_osgb",
            x_dim_name="x_osgb",
        )
        .downsample(y_coarsen=16, x_coarsen=16)
        .fork(2)
    )

    nwp_t0_dp = nwp_t0_dp.select_live_t0_time(dim_name="init_time_utc")
    gsp_t0_dp = gsp_dp.select_live_t0_time()
    sat_t0_dp = sat_t0_dp.select_live_t0_time()
    pv_t0_dp = pv_t0_dp.select_live_t0_time()

    logger.debug("Making GSP Time slices")
    gsp_dp = (
        gsp_dp.select_live_time_slice(
            t0_datapipe=gsp_t0_dp,
            history_duration=timedelta(minutes=configuration.input_data.gsp.history_minutes),
        )
        .gsp_iterator()
        .convert_gsp_to_numpy_batch()
        .extend_timesteps_to_future(
            forecast_duration=timedelta(minutes=configuration.input_data.gsp.forecast_minutes),
            sample_period_duration=timedelta(minutes=30),
        )
        .merge_numpy_examples_to_batch(n_examples_per_batch=configuration.process.batch_size)
    )
    logger.debug("Making Sat Time slices")
    sat_hrv_dp = (
        sat_hrv_dp.select_live_time_slice(
            t0_datapipe=sat_t0_dp,
            history_duration=timedelta(
                minutes=configuration.input_data.hrvsatellite.history_minutes
            ),
        )
        .normalize(mean=SAT_MEAN["HRV"] / 4, std=SAT_STD["HRV"] / 4)
        .map(
            lambda x: x.resample(time_utc="5T").interpolate("linear")
        )  # Interplate to 5 minutes incase its 15 minutes
        .convert_satellite_to_numpy_batch(is_hrv=True)
        .extend_timesteps_to_future(
            forecast_duration=timedelta(
                minutes=configuration.input_data.hrvsatellite.forecast_minutes
            ),
            sample_period_duration=timedelta(minutes=5),
        )
        .merge_numpy_examples_to_batch(n_examples_per_batch=configuration.process.batch_size)
    )
    passiv_dp = (
        passiv_dp.select_live_time_slice(
            t0_datapipe=pv_t0_dp,
            history_duration=timedelta(minutes=configuration.input_data.pv.history_minutes),
        )
        .convert_pv_to_numpy_batch()
        .extend_timesteps_to_future(
            forecast_duration=timedelta(minutes=configuration.input_data.pv.forecast_minutes),
            sample_period_duration=timedelta(minutes=5),
        )
        .merge_numpy_examples_to_batch(n_examples_per_batch=configuration.process.batch_size)
    )
    nwp_dp = (
        nwp_dp.convert_to_nwp_target_time(
            t0_datapipe=nwp_t0_dp,
            sample_period_duration=timedelta(hours=1),
            history_duration=timedelta(minutes=configuration.input_data.nwp.history_minutes),
            forecast_duration=timedelta(minutes=configuration.input_data.nwp.forecast_minutes),
        )
        .normalize(mean=NWP_MEAN, std=NWP_STD)
        .convert_nwp_to_numpy_batch()
        .merge_numpy_examples_to_batch(n_examples_per_batch=configuration.process.batch_size)
    )

    ####################################
    #
    # Equivalent to PP's np_batch_processors
    #
    #####################################
    logger.debug("Combine all the data sources")
    combined_dp = (
        MergeNumpyModalities([gsp_dp, passiv_dp, sat_hrv_dp, nwp_dp])
        .align_gsp_to_5_min(batch_key_for_5_min_datetimes=BatchKey.hrvsatellite_time_utc)
        .encode_space_time()
        .save_t0_time()
        .add_sun_position(modality_name="hrvsatellite")
        .add_sun_position(modality_name="pv")
        .add_sun_position(modality_name="gsp")
        .add_sun_position(modality_name="gsp_5_min")
        .add_sun_position(modality_name="nwp_target_time")
        .add_topographic_data(topo_dp)
        .set_system_ids_to_one()
    )

    return combined_dp
