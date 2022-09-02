# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin

from .._serialization import Deserializer, Serializer
from ._configuration import IotHubClientConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class IotHubClient(MultiApiClientMixin, _SDKClient):
    """Use this API to manage the IoT hubs in your Azure subscription.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The subscription identifier. Required.
    :type subscription_id: str
    :param api_version: API version to use if no profile is provided, or if missing in profile.
    :type api_version: str
    :param base_url: Service URL
    :type base_url: str
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    DEFAULT_API_VERSION = '2021-07-02'
    _PROFILE_TAG = "azure.mgmt.iothub.IotHubClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        api_version: Optional[str] = None,
        base_url: str = "https://management.azure.com",
        profile: KnownProfiles = KnownProfiles.default,
        **kwargs  # type: Any
    ) -> None:
        self._config = IotHubClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(IotHubClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2016-02-03: :mod:`v2016_02_03.models<azure.mgmt.iothub.v2016_02_03.models>`
           * 2017-01-19: :mod:`v2017_01_19.models<azure.mgmt.iothub.v2017_01_19.models>`
           * 2017-07-01: :mod:`v2017_07_01.models<azure.mgmt.iothub.v2017_07_01.models>`
           * 2018-01-22: :mod:`v2018_01_22.models<azure.mgmt.iothub.v2018_01_22.models>`
           * 2018-04-01: :mod:`v2018_04_01.models<azure.mgmt.iothub.v2018_04_01.models>`
           * 2019-03-22: :mod:`v2019_03_22.models<azure.mgmt.iothub.v2019_03_22.models>`
           * 2019-07-01-preview: :mod:`v2019_07_01_preview.models<azure.mgmt.iothub.v2019_07_01_preview.models>`
           * 2019-11-04: :mod:`v2019_11_04.models<azure.mgmt.iothub.v2019_11_04.models>`
           * 2020-03-01: :mod:`v2020_03_01.models<azure.mgmt.iothub.v2020_03_01.models>`
           * 2021-03-03-preview: :mod:`v2021_03_03_preview.models<azure.mgmt.iothub.v2021_03_03_preview.models>`
           * 2021-03-31: :mod:`v2021_03_31.models<azure.mgmt.iothub.v2021_03_31.models>`
           * 2021-07-01: :mod:`v2021_07_01.models<azure.mgmt.iothub.v2021_07_01.models>`
           * 2021-07-02: :mod:`v2021_07_02.models<azure.mgmt.iothub.v2021_07_02.models>`
           * 2022-04-30-preview: :mod:`v2022_04_30_preview.models<azure.mgmt.iothub.v2022_04_30_preview.models>`
        """
        if api_version == '2016-02-03':
            from ..v2016_02_03 import models
            return models
        elif api_version == '2017-01-19':
            from ..v2017_01_19 import models
            return models
        elif api_version == '2017-07-01':
            from ..v2017_07_01 import models
            return models
        elif api_version == '2018-01-22':
            from ..v2018_01_22 import models
            return models
        elif api_version == '2018-04-01':
            from ..v2018_04_01 import models
            return models
        elif api_version == '2019-03-22':
            from ..v2019_03_22 import models
            return models
        elif api_version == '2019-07-01-preview':
            from ..v2019_07_01_preview import models
            return models
        elif api_version == '2019-11-04':
            from ..v2019_11_04 import models
            return models
        elif api_version == '2020-03-01':
            from ..v2020_03_01 import models
            return models
        elif api_version == '2021-03-03-preview':
            from ..v2021_03_03_preview import models
            return models
        elif api_version == '2021-03-31':
            from ..v2021_03_31 import models
            return models
        elif api_version == '2021-07-01':
            from ..v2021_07_01 import models
            return models
        elif api_version == '2021-07-02':
            from ..v2021_07_02 import models
            return models
        elif api_version == '2022-04-30-preview':
            from ..v2022_04_30_preview import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def certificates(self):
        """Instance depends on the API version:

           * 2017-07-01: :class:`CertificatesOperations<azure.mgmt.iothub.v2017_07_01.aio.operations.CertificatesOperations>`
           * 2018-01-22: :class:`CertificatesOperations<azure.mgmt.iothub.v2018_01_22.aio.operations.CertificatesOperations>`
           * 2018-04-01: :class:`CertificatesOperations<azure.mgmt.iothub.v2018_04_01.aio.operations.CertificatesOperations>`
           * 2019-03-22: :class:`CertificatesOperations<azure.mgmt.iothub.v2019_03_22.aio.operations.CertificatesOperations>`
           * 2019-07-01-preview: :class:`CertificatesOperations<azure.mgmt.iothub.v2019_07_01_preview.aio.operations.CertificatesOperations>`
           * 2019-11-04: :class:`CertificatesOperations<azure.mgmt.iothub.v2019_11_04.aio.operations.CertificatesOperations>`
           * 2020-03-01: :class:`CertificatesOperations<azure.mgmt.iothub.v2020_03_01.aio.operations.CertificatesOperations>`
           * 2021-03-03-preview: :class:`CertificatesOperations<azure.mgmt.iothub.v2021_03_03_preview.aio.operations.CertificatesOperations>`
           * 2021-03-31: :class:`CertificatesOperations<azure.mgmt.iothub.v2021_03_31.aio.operations.CertificatesOperations>`
           * 2021-07-01: :class:`CertificatesOperations<azure.mgmt.iothub.v2021_07_01.aio.operations.CertificatesOperations>`
           * 2021-07-02: :class:`CertificatesOperations<azure.mgmt.iothub.v2021_07_02.aio.operations.CertificatesOperations>`
           * 2022-04-30-preview: :class:`CertificatesOperations<azure.mgmt.iothub.v2022_04_30_preview.aio.operations.CertificatesOperations>`
        """
        api_version = self._get_api_version('certificates')
        if api_version == '2017-07-01':
            from ..v2017_07_01.aio.operations import CertificatesOperations as OperationClass
        elif api_version == '2018-01-22':
            from ..v2018_01_22.aio.operations import CertificatesOperations as OperationClass
        elif api_version == '2018-04-01':
            from ..v2018_04_01.aio.operations import CertificatesOperations as OperationClass
        elif api_version == '2019-03-22':
            from ..v2019_03_22.aio.operations import CertificatesOperations as OperationClass
        elif api_version == '2019-07-01-preview':
            from ..v2019_07_01_preview.aio.operations import CertificatesOperations as OperationClass
        elif api_version == '2019-11-04':
            from ..v2019_11_04.aio.operations import CertificatesOperations as OperationClass
        elif api_version == '2020-03-01':
            from ..v2020_03_01.aio.operations import CertificatesOperations as OperationClass
        elif api_version == '2021-03-03-preview':
            from ..v2021_03_03_preview.aio.operations import CertificatesOperations as OperationClass
        elif api_version == '2021-03-31':
            from ..v2021_03_31.aio.operations import CertificatesOperations as OperationClass
        elif api_version == '2021-07-01':
            from ..v2021_07_01.aio.operations import CertificatesOperations as OperationClass
        elif api_version == '2021-07-02':
            from ..v2021_07_02.aio.operations import CertificatesOperations as OperationClass
        elif api_version == '2022-04-30-preview':
            from ..v2022_04_30_preview.aio.operations import CertificatesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'certificates'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def iot_hub(self):
        """Instance depends on the API version:

           * 2019-03-22: :class:`IotHubOperations<azure.mgmt.iothub.v2019_03_22.aio.operations.IotHubOperations>`
           * 2019-07-01-preview: :class:`IotHubOperations<azure.mgmt.iothub.v2019_07_01_preview.aio.operations.IotHubOperations>`
           * 2019-11-04: :class:`IotHubOperations<azure.mgmt.iothub.v2019_11_04.aio.operations.IotHubOperations>`
           * 2020-03-01: :class:`IotHubOperations<azure.mgmt.iothub.v2020_03_01.aio.operations.IotHubOperations>`
           * 2021-03-03-preview: :class:`IotHubOperations<azure.mgmt.iothub.v2021_03_03_preview.aio.operations.IotHubOperations>`
           * 2021-03-31: :class:`IotHubOperations<azure.mgmt.iothub.v2021_03_31.aio.operations.IotHubOperations>`
           * 2021-07-01: :class:`IotHubOperations<azure.mgmt.iothub.v2021_07_01.aio.operations.IotHubOperations>`
           * 2021-07-02: :class:`IotHubOperations<azure.mgmt.iothub.v2021_07_02.aio.operations.IotHubOperations>`
           * 2022-04-30-preview: :class:`IotHubOperations<azure.mgmt.iothub.v2022_04_30_preview.aio.operations.IotHubOperations>`
        """
        api_version = self._get_api_version('iot_hub')
        if api_version == '2019-03-22':
            from ..v2019_03_22.aio.operations import IotHubOperations as OperationClass
        elif api_version == '2019-07-01-preview':
            from ..v2019_07_01_preview.aio.operations import IotHubOperations as OperationClass
        elif api_version == '2019-11-04':
            from ..v2019_11_04.aio.operations import IotHubOperations as OperationClass
        elif api_version == '2020-03-01':
            from ..v2020_03_01.aio.operations import IotHubOperations as OperationClass
        elif api_version == '2021-03-03-preview':
            from ..v2021_03_03_preview.aio.operations import IotHubOperations as OperationClass
        elif api_version == '2021-03-31':
            from ..v2021_03_31.aio.operations import IotHubOperations as OperationClass
        elif api_version == '2021-07-01':
            from ..v2021_07_01.aio.operations import IotHubOperations as OperationClass
        elif api_version == '2021-07-02':
            from ..v2021_07_02.aio.operations import IotHubOperations as OperationClass
        elif api_version == '2022-04-30-preview':
            from ..v2022_04_30_preview.aio.operations import IotHubOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'iot_hub'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def iot_hub_resource(self):
        """Instance depends on the API version:

           * 2016-02-03: :class:`IotHubResourceOperations<azure.mgmt.iothub.v2016_02_03.aio.operations.IotHubResourceOperations>`
           * 2017-01-19: :class:`IotHubResourceOperations<azure.mgmt.iothub.v2017_01_19.aio.operations.IotHubResourceOperations>`
           * 2017-07-01: :class:`IotHubResourceOperations<azure.mgmt.iothub.v2017_07_01.aio.operations.IotHubResourceOperations>`
           * 2018-01-22: :class:`IotHubResourceOperations<azure.mgmt.iothub.v2018_01_22.aio.operations.IotHubResourceOperations>`
           * 2018-04-01: :class:`IotHubResourceOperations<azure.mgmt.iothub.v2018_04_01.aio.operations.IotHubResourceOperations>`
           * 2019-03-22: :class:`IotHubResourceOperations<azure.mgmt.iothub.v2019_03_22.aio.operations.IotHubResourceOperations>`
           * 2019-07-01-preview: :class:`IotHubResourceOperations<azure.mgmt.iothub.v2019_07_01_preview.aio.operations.IotHubResourceOperations>`
           * 2019-11-04: :class:`IotHubResourceOperations<azure.mgmt.iothub.v2019_11_04.aio.operations.IotHubResourceOperations>`
           * 2020-03-01: :class:`IotHubResourceOperations<azure.mgmt.iothub.v2020_03_01.aio.operations.IotHubResourceOperations>`
           * 2021-03-03-preview: :class:`IotHubResourceOperations<azure.mgmt.iothub.v2021_03_03_preview.aio.operations.IotHubResourceOperations>`
           * 2021-03-31: :class:`IotHubResourceOperations<azure.mgmt.iothub.v2021_03_31.aio.operations.IotHubResourceOperations>`
           * 2021-07-01: :class:`IotHubResourceOperations<azure.mgmt.iothub.v2021_07_01.aio.operations.IotHubResourceOperations>`
           * 2021-07-02: :class:`IotHubResourceOperations<azure.mgmt.iothub.v2021_07_02.aio.operations.IotHubResourceOperations>`
           * 2022-04-30-preview: :class:`IotHubResourceOperations<azure.mgmt.iothub.v2022_04_30_preview.aio.operations.IotHubResourceOperations>`
        """
        api_version = self._get_api_version('iot_hub_resource')
        if api_version == '2016-02-03':
            from ..v2016_02_03.aio.operations import IotHubResourceOperations as OperationClass
        elif api_version == '2017-01-19':
            from ..v2017_01_19.aio.operations import IotHubResourceOperations as OperationClass
        elif api_version == '2017-07-01':
            from ..v2017_07_01.aio.operations import IotHubResourceOperations as OperationClass
        elif api_version == '2018-01-22':
            from ..v2018_01_22.aio.operations import IotHubResourceOperations as OperationClass
        elif api_version == '2018-04-01':
            from ..v2018_04_01.aio.operations import IotHubResourceOperations as OperationClass
        elif api_version == '2019-03-22':
            from ..v2019_03_22.aio.operations import IotHubResourceOperations as OperationClass
        elif api_version == '2019-07-01-preview':
            from ..v2019_07_01_preview.aio.operations import IotHubResourceOperations as OperationClass
        elif api_version == '2019-11-04':
            from ..v2019_11_04.aio.operations import IotHubResourceOperations as OperationClass
        elif api_version == '2020-03-01':
            from ..v2020_03_01.aio.operations import IotHubResourceOperations as OperationClass
        elif api_version == '2021-03-03-preview':
            from ..v2021_03_03_preview.aio.operations import IotHubResourceOperations as OperationClass
        elif api_version == '2021-03-31':
            from ..v2021_03_31.aio.operations import IotHubResourceOperations as OperationClass
        elif api_version == '2021-07-01':
            from ..v2021_07_01.aio.operations import IotHubResourceOperations as OperationClass
        elif api_version == '2021-07-02':
            from ..v2021_07_02.aio.operations import IotHubResourceOperations as OperationClass
        elif api_version == '2022-04-30-preview':
            from ..v2022_04_30_preview.aio.operations import IotHubResourceOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'iot_hub_resource'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2017-07-01: :class:`Operations<azure.mgmt.iothub.v2017_07_01.aio.operations.Operations>`
           * 2018-01-22: :class:`Operations<azure.mgmt.iothub.v2018_01_22.aio.operations.Operations>`
           * 2018-04-01: :class:`Operations<azure.mgmt.iothub.v2018_04_01.aio.operations.Operations>`
           * 2019-03-22: :class:`Operations<azure.mgmt.iothub.v2019_03_22.aio.operations.Operations>`
           * 2019-07-01-preview: :class:`Operations<azure.mgmt.iothub.v2019_07_01_preview.aio.operations.Operations>`
           * 2019-11-04: :class:`Operations<azure.mgmt.iothub.v2019_11_04.aio.operations.Operations>`
           * 2020-03-01: :class:`Operations<azure.mgmt.iothub.v2020_03_01.aio.operations.Operations>`
           * 2021-03-03-preview: :class:`Operations<azure.mgmt.iothub.v2021_03_03_preview.aio.operations.Operations>`
           * 2021-03-31: :class:`Operations<azure.mgmt.iothub.v2021_03_31.aio.operations.Operations>`
           * 2021-07-01: :class:`Operations<azure.mgmt.iothub.v2021_07_01.aio.operations.Operations>`
           * 2021-07-02: :class:`Operations<azure.mgmt.iothub.v2021_07_02.aio.operations.Operations>`
           * 2022-04-30-preview: :class:`Operations<azure.mgmt.iothub.v2022_04_30_preview.aio.operations.Operations>`
        """
        api_version = self._get_api_version('operations')
        if api_version == '2017-07-01':
            from ..v2017_07_01.aio.operations import Operations as OperationClass
        elif api_version == '2018-01-22':
            from ..v2018_01_22.aio.operations import Operations as OperationClass
        elif api_version == '2018-04-01':
            from ..v2018_04_01.aio.operations import Operations as OperationClass
        elif api_version == '2019-03-22':
            from ..v2019_03_22.aio.operations import Operations as OperationClass
        elif api_version == '2019-07-01-preview':
            from ..v2019_07_01_preview.aio.operations import Operations as OperationClass
        elif api_version == '2019-11-04':
            from ..v2019_11_04.aio.operations import Operations as OperationClass
        elif api_version == '2020-03-01':
            from ..v2020_03_01.aio.operations import Operations as OperationClass
        elif api_version == '2021-03-03-preview':
            from ..v2021_03_03_preview.aio.operations import Operations as OperationClass
        elif api_version == '2021-03-31':
            from ..v2021_03_31.aio.operations import Operations as OperationClass
        elif api_version == '2021-07-01':
            from ..v2021_07_01.aio.operations import Operations as OperationClass
        elif api_version == '2021-07-02':
            from ..v2021_07_02.aio.operations import Operations as OperationClass
        elif api_version == '2022-04-30-preview':
            from ..v2022_04_30_preview.aio.operations import Operations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'operations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def private_endpoint_connections(self):
        """Instance depends on the API version:

           * 2020-03-01: :class:`PrivateEndpointConnectionsOperations<azure.mgmt.iothub.v2020_03_01.aio.operations.PrivateEndpointConnectionsOperations>`
           * 2021-03-03-preview: :class:`PrivateEndpointConnectionsOperations<azure.mgmt.iothub.v2021_03_03_preview.aio.operations.PrivateEndpointConnectionsOperations>`
           * 2021-03-31: :class:`PrivateEndpointConnectionsOperations<azure.mgmt.iothub.v2021_03_31.aio.operations.PrivateEndpointConnectionsOperations>`
           * 2021-07-01: :class:`PrivateEndpointConnectionsOperations<azure.mgmt.iothub.v2021_07_01.aio.operations.PrivateEndpointConnectionsOperations>`
           * 2021-07-02: :class:`PrivateEndpointConnectionsOperations<azure.mgmt.iothub.v2021_07_02.aio.operations.PrivateEndpointConnectionsOperations>`
           * 2022-04-30-preview: :class:`PrivateEndpointConnectionsOperations<azure.mgmt.iothub.v2022_04_30_preview.aio.operations.PrivateEndpointConnectionsOperations>`
        """
        api_version = self._get_api_version('private_endpoint_connections')
        if api_version == '2020-03-01':
            from ..v2020_03_01.aio.operations import PrivateEndpointConnectionsOperations as OperationClass
        elif api_version == '2021-03-03-preview':
            from ..v2021_03_03_preview.aio.operations import PrivateEndpointConnectionsOperations as OperationClass
        elif api_version == '2021-03-31':
            from ..v2021_03_31.aio.operations import PrivateEndpointConnectionsOperations as OperationClass
        elif api_version == '2021-07-01':
            from ..v2021_07_01.aio.operations import PrivateEndpointConnectionsOperations as OperationClass
        elif api_version == '2021-07-02':
            from ..v2021_07_02.aio.operations import PrivateEndpointConnectionsOperations as OperationClass
        elif api_version == '2022-04-30-preview':
            from ..v2022_04_30_preview.aio.operations import PrivateEndpointConnectionsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'private_endpoint_connections'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def private_link_resources(self):
        """Instance depends on the API version:

           * 2020-03-01: :class:`PrivateLinkResourcesOperations<azure.mgmt.iothub.v2020_03_01.aio.operations.PrivateLinkResourcesOperations>`
           * 2021-03-03-preview: :class:`PrivateLinkResourcesOperations<azure.mgmt.iothub.v2021_03_03_preview.aio.operations.PrivateLinkResourcesOperations>`
           * 2021-03-31: :class:`PrivateLinkResourcesOperations<azure.mgmt.iothub.v2021_03_31.aio.operations.PrivateLinkResourcesOperations>`
           * 2021-07-01: :class:`PrivateLinkResourcesOperations<azure.mgmt.iothub.v2021_07_01.aio.operations.PrivateLinkResourcesOperations>`
           * 2021-07-02: :class:`PrivateLinkResourcesOperations<azure.mgmt.iothub.v2021_07_02.aio.operations.PrivateLinkResourcesOperations>`
           * 2022-04-30-preview: :class:`PrivateLinkResourcesOperations<azure.mgmt.iothub.v2022_04_30_preview.aio.operations.PrivateLinkResourcesOperations>`
        """
        api_version = self._get_api_version('private_link_resources')
        if api_version == '2020-03-01':
            from ..v2020_03_01.aio.operations import PrivateLinkResourcesOperations as OperationClass
        elif api_version == '2021-03-03-preview':
            from ..v2021_03_03_preview.aio.operations import PrivateLinkResourcesOperations as OperationClass
        elif api_version == '2021-03-31':
            from ..v2021_03_31.aio.operations import PrivateLinkResourcesOperations as OperationClass
        elif api_version == '2021-07-01':
            from ..v2021_07_01.aio.operations import PrivateLinkResourcesOperations as OperationClass
        elif api_version == '2021-07-02':
            from ..v2021_07_02.aio.operations import PrivateLinkResourcesOperations as OperationClass
        elif api_version == '2022-04-30-preview':
            from ..v2022_04_30_preview.aio.operations import PrivateLinkResourcesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'private_link_resources'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def resource_provider_common(self):
        """Instance depends on the API version:

           * 2018-04-01: :class:`ResourceProviderCommonOperations<azure.mgmt.iothub.v2018_04_01.aio.operations.ResourceProviderCommonOperations>`
           * 2019-03-22: :class:`ResourceProviderCommonOperations<azure.mgmt.iothub.v2019_03_22.aio.operations.ResourceProviderCommonOperations>`
           * 2019-07-01-preview: :class:`ResourceProviderCommonOperations<azure.mgmt.iothub.v2019_07_01_preview.aio.operations.ResourceProviderCommonOperations>`
           * 2019-11-04: :class:`ResourceProviderCommonOperations<azure.mgmt.iothub.v2019_11_04.aio.operations.ResourceProviderCommonOperations>`
           * 2020-03-01: :class:`ResourceProviderCommonOperations<azure.mgmt.iothub.v2020_03_01.aio.operations.ResourceProviderCommonOperations>`
           * 2021-03-03-preview: :class:`ResourceProviderCommonOperations<azure.mgmt.iothub.v2021_03_03_preview.aio.operations.ResourceProviderCommonOperations>`
           * 2021-03-31: :class:`ResourceProviderCommonOperations<azure.mgmt.iothub.v2021_03_31.aio.operations.ResourceProviderCommonOperations>`
           * 2021-07-01: :class:`ResourceProviderCommonOperations<azure.mgmt.iothub.v2021_07_01.aio.operations.ResourceProviderCommonOperations>`
           * 2021-07-02: :class:`ResourceProviderCommonOperations<azure.mgmt.iothub.v2021_07_02.aio.operations.ResourceProviderCommonOperations>`
           * 2022-04-30-preview: :class:`ResourceProviderCommonOperations<azure.mgmt.iothub.v2022_04_30_preview.aio.operations.ResourceProviderCommonOperations>`
        """
        api_version = self._get_api_version('resource_provider_common')
        if api_version == '2018-04-01':
            from ..v2018_04_01.aio.operations import ResourceProviderCommonOperations as OperationClass
        elif api_version == '2019-03-22':
            from ..v2019_03_22.aio.operations import ResourceProviderCommonOperations as OperationClass
        elif api_version == '2019-07-01-preview':
            from ..v2019_07_01_preview.aio.operations import ResourceProviderCommonOperations as OperationClass
        elif api_version == '2019-11-04':
            from ..v2019_11_04.aio.operations import ResourceProviderCommonOperations as OperationClass
        elif api_version == '2020-03-01':
            from ..v2020_03_01.aio.operations import ResourceProviderCommonOperations as OperationClass
        elif api_version == '2021-03-03-preview':
            from ..v2021_03_03_preview.aio.operations import ResourceProviderCommonOperations as OperationClass
        elif api_version == '2021-03-31':
            from ..v2021_03_31.aio.operations import ResourceProviderCommonOperations as OperationClass
        elif api_version == '2021-07-01':
            from ..v2021_07_01.aio.operations import ResourceProviderCommonOperations as OperationClass
        elif api_version == '2021-07-02':
            from ..v2021_07_02.aio.operations import ResourceProviderCommonOperations as OperationClass
        elif api_version == '2022-04-30-preview':
            from ..v2022_04_30_preview.aio.operations import ResourceProviderCommonOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'resource_provider_common'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    async def close(self):
        await self._client.close()
    async def __aenter__(self):
        await self._client.__aenter__()
        return self
    async def __aexit__(self, *exc_details):
        await self._client.__aexit__(*exc_details)
