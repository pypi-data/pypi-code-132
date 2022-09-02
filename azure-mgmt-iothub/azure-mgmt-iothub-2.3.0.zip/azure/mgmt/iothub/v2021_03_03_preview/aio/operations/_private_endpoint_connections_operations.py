# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, List, Optional, TypeVar, Union, cast, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._private_endpoint_connections_operations import (
    build_delete_request,
    build_get_request,
    build_list_request,
    build_update_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PrivateEndpointConnectionsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.iothub.v2021_03_03_preview.aio.IotHubClient`'s
        :attr:`private_endpoint_connections` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def list(
        self, resource_group_name: str, resource_name: str, **kwargs: Any
    ) -> List[_models.PrivateEndpointConnection]:
        """List private endpoint connections.

        List private endpoint connection properties.

        :param resource_group_name: The name of the resource group that contains the IoT hub. Required.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub. Required.
        :type resource_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of PrivateEndpointConnection or the result of cls(response)
        :rtype: list[~azure.mgmt.iothub.v2021_03_03_preview.models.PrivateEndpointConnection]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-03-03-preview"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[List[_models.PrivateEndpointConnection]]

        request = build_list_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.list.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDetails, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("[PrivateEndpointConnection]", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/iotHubs/{resourceName}/privateEndpointConnections"}  # type: ignore

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, resource_name: str, private_endpoint_connection_name: str, **kwargs: Any
    ) -> _models.PrivateEndpointConnection:
        """Get private endpoint connection.

        Get private endpoint connection properties.

        :param resource_group_name: The name of the resource group that contains the IoT hub. Required.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub. Required.
        :type resource_name: str
        :param private_endpoint_connection_name: The name of the private endpoint connection. Required.
        :type private_endpoint_connection_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PrivateEndpointConnection or the result of cls(response)
        :rtype: ~azure.mgmt.iothub.v2021_03_03_preview.models.PrivateEndpointConnection
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-03-03-preview"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.PrivateEndpointConnection]

        request = build_get_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            private_endpoint_connection_name=private_endpoint_connection_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDetails, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("PrivateEndpointConnection", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/iotHubs/{resourceName}/privateEndpointConnections/{privateEndpointConnectionName}"}  # type: ignore

    async def _update_initial(
        self,
        resource_group_name: str,
        resource_name: str,
        private_endpoint_connection_name: str,
        private_endpoint_connection: Union[_models.PrivateEndpointConnection, IO],
        **kwargs: Any
    ) -> _models.PrivateEndpointConnection:
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-03-03-preview"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.PrivateEndpointConnection]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(private_endpoint_connection, (IO, bytes)):
            _content = private_endpoint_connection
        else:
            _json = self._serialize.body(private_endpoint_connection, "PrivateEndpointConnection")

        request = build_update_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            private_endpoint_connection_name=private_endpoint_connection_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self._update_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDetails, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("PrivateEndpointConnection", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("PrivateEndpointConnection", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _update_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/iotHubs/{resourceName}/privateEndpointConnections/{privateEndpointConnectionName}"}  # type: ignore

    @overload
    async def begin_update(
        self,
        resource_group_name: str,
        resource_name: str,
        private_endpoint_connection_name: str,
        private_endpoint_connection: _models.PrivateEndpointConnection,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.PrivateEndpointConnection]:
        """Update private endpoint connection.

        Update the status of a private endpoint connection with the specified name.

        :param resource_group_name: The name of the resource group that contains the IoT hub. Required.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub. Required.
        :type resource_name: str
        :param private_endpoint_connection_name: The name of the private endpoint connection. Required.
        :type private_endpoint_connection_name: str
        :param private_endpoint_connection: The private endpoint connection with updated properties.
         Required.
        :type private_endpoint_connection:
         ~azure.mgmt.iothub.v2021_03_03_preview.models.PrivateEndpointConnection
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either PrivateEndpointConnection or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.iothub.v2021_03_03_preview.models.PrivateEndpointConnection]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_update(
        self,
        resource_group_name: str,
        resource_name: str,
        private_endpoint_connection_name: str,
        private_endpoint_connection: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.PrivateEndpointConnection]:
        """Update private endpoint connection.

        Update the status of a private endpoint connection with the specified name.

        :param resource_group_name: The name of the resource group that contains the IoT hub. Required.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub. Required.
        :type resource_name: str
        :param private_endpoint_connection_name: The name of the private endpoint connection. Required.
        :type private_endpoint_connection_name: str
        :param private_endpoint_connection: The private endpoint connection with updated properties.
         Required.
        :type private_endpoint_connection: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either PrivateEndpointConnection or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.iothub.v2021_03_03_preview.models.PrivateEndpointConnection]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_update(
        self,
        resource_group_name: str,
        resource_name: str,
        private_endpoint_connection_name: str,
        private_endpoint_connection: Union[_models.PrivateEndpointConnection, IO],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.PrivateEndpointConnection]:
        """Update private endpoint connection.

        Update the status of a private endpoint connection with the specified name.

        :param resource_group_name: The name of the resource group that contains the IoT hub. Required.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub. Required.
        :type resource_name: str
        :param private_endpoint_connection_name: The name of the private endpoint connection. Required.
        :type private_endpoint_connection_name: str
        :param private_endpoint_connection: The private endpoint connection with updated properties. Is
         either a model type or a IO type. Required.
        :type private_endpoint_connection:
         ~azure.mgmt.iothub.v2021_03_03_preview.models.PrivateEndpointConnection or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either PrivateEndpointConnection or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.iothub.v2021_03_03_preview.models.PrivateEndpointConnection]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-03-03-preview"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.PrivateEndpointConnection]
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._update_initial(  # type: ignore
                resource_group_name=resource_group_name,
                resource_name=resource_name,
                private_endpoint_connection_name=private_endpoint_connection_name,
                private_endpoint_connection=private_endpoint_connection,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("PrivateEndpointConnection", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))  # type: AsyncPollingMethod
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/iotHubs/{resourceName}/privateEndpointConnections/{privateEndpointConnectionName}"}  # type: ignore

    async def _delete_initial(
        self, resource_group_name: str, resource_name: str, private_endpoint_connection_name: str, **kwargs: Any
    ) -> Optional[_models.PrivateEndpointConnection]:
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-03-03-preview"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional[_models.PrivateEndpointConnection]]

        request = build_delete_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            private_endpoint_connection_name=private_endpoint_connection_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self._delete_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDetails, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize("PrivateEndpointConnection", pipeline_response)

        if response.status_code == 202:
            deserialized = self._deserialize("PrivateEndpointConnection", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _delete_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/iotHubs/{resourceName}/privateEndpointConnections/{privateEndpointConnectionName}"}  # type: ignore

    @distributed_trace_async
    async def begin_delete(
        self, resource_group_name: str, resource_name: str, private_endpoint_connection_name: str, **kwargs: Any
    ) -> AsyncLROPoller[_models.PrivateEndpointConnection]:
        """Delete private endpoint connection.

        Delete private endpoint connection with the specified name.

        :param resource_group_name: The name of the resource group that contains the IoT hub. Required.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub. Required.
        :type resource_name: str
        :param private_endpoint_connection_name: The name of the private endpoint connection. Required.
        :type private_endpoint_connection_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either PrivateEndpointConnection or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.iothub.v2021_03_03_preview.models.PrivateEndpointConnection]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-03-03-preview"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.PrivateEndpointConnection]
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._delete_initial(  # type: ignore
                resource_group_name=resource_group_name,
                resource_name=resource_name,
                private_endpoint_connection_name=private_endpoint_connection_name,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("PrivateEndpointConnection", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))  # type: AsyncPollingMethod
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_delete.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/iotHubs/{resourceName}/privateEndpointConnections/{privateEndpointConnectionName}"}  # type: ignore
