# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from ..._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_by_iot_hub_request(
    resource_group_name: str, resource_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-03-22"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(
    resource_group_name: str, resource_name: str, certificate_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-03-22"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, "str"),
        "certificateName": _SERIALIZER.url(
            "certificate_name", certificate_name, "str", pattern=r"^[A-Za-z0-9-._]{1,64}$"
        ),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_create_or_update_request(
    resource_group_name: str,
    resource_name: str,
    certificate_name: str,
    subscription_id: str,
    *,
    if_match: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-03-22"))  # type: str
    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, "str"),
        "certificateName": _SERIALIZER.url(
            "certificate_name", certificate_name, "str", pattern=r"^[A-Za-z0-9-._]{1,64}$"
        ),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if if_match is not None:
        _headers["If-Match"] = _SERIALIZER.header("if_match", if_match, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_delete_request(
    resource_group_name: str,
    resource_name: str,
    certificate_name: str,
    subscription_id: str,
    *,
    if_match: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-03-22"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, "str"),
        "certificateName": _SERIALIZER.url(
            "certificate_name", certificate_name, "str", pattern=r"^[A-Za-z0-9-._]{1,64}$"
        ),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["If-Match"] = _SERIALIZER.header("if_match", if_match, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, headers=_headers, **kwargs)


def build_generate_verification_code_request(
    resource_group_name: str,
    resource_name: str,
    certificate_name: str,
    subscription_id: str,
    *,
    if_match: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-03-22"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}/generateVerificationCode",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, "str"),
        "certificateName": _SERIALIZER.url(
            "certificate_name", certificate_name, "str", pattern=r"^[A-Za-z0-9-._]{1,64}$"
        ),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["If-Match"] = _SERIALIZER.header("if_match", if_match, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_verify_request(
    resource_group_name: str,
    resource_name: str,
    certificate_name: str,
    subscription_id: str,
    *,
    if_match: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-03-22"))  # type: str
    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}/verify",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, "str"),
        "certificateName": _SERIALIZER.url(
            "certificate_name", certificate_name, "str", pattern=r"^[A-Za-z0-9-._]{1,64}$"
        ),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["If-Match"] = _SERIALIZER.header("if_match", if_match, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class CertificatesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.iothub.v2019_03_22.IotHubClient`'s
        :attr:`certificates` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list_by_iot_hub(
        self, resource_group_name: str, resource_name: str, **kwargs: Any
    ) -> _models.CertificateListDescription:
        """Get the certificate list.

        Returns the list of certificates.

        :param resource_group_name: The name of the resource group that contains the IoT hub. Required.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub. Required.
        :type resource_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CertificateListDescription or the result of cls(response)
        :rtype: ~azure.mgmt.iothub.v2019_03_22.models.CertificateListDescription
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-03-22"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.CertificateListDescription]

        request = build_list_by_iot_hub_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.list_by_iot_hub.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDetails, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("CertificateListDescription", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_by_iot_hub.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates"}  # type: ignore

    @distributed_trace
    def get(
        self, resource_group_name: str, resource_name: str, certificate_name: str, **kwargs: Any
    ) -> _models.CertificateDescription:
        """Get the certificate.

        Returns the certificate.

        :param resource_group_name: The name of the resource group that contains the IoT hub. Required.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub. Required.
        :type resource_name: str
        :param certificate_name: The name of the certificate. Required.
        :type certificate_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CertificateDescription or the result of cls(response)
        :rtype: ~azure.mgmt.iothub.v2019_03_22.models.CertificateDescription
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-03-22"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.CertificateDescription]

        request = build_get_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            certificate_name=certificate_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDetails, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("CertificateDescription", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}"}  # type: ignore

    @overload
    def create_or_update(
        self,
        resource_group_name: str,
        resource_name: str,
        certificate_name: str,
        certificate_description: _models.CertificateBodyDescription,
        if_match: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CertificateDescription:
        """Upload the certificate to the IoT hub.

        Adds new or replaces existing certificate.

        :param resource_group_name: The name of the resource group that contains the IoT hub. Required.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub. Required.
        :type resource_name: str
        :param certificate_name: The name of the certificate. Required.
        :type certificate_name: str
        :param certificate_description: The certificate body. Required.
        :type certificate_description: ~azure.mgmt.iothub.v2019_03_22.models.CertificateBodyDescription
        :param if_match: ETag of the Certificate. Do not specify for creating a brand new certificate.
         Required to update an existing certificate. Default value is None.
        :type if_match: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CertificateDescription or the result of cls(response)
        :rtype: ~azure.mgmt.iothub.v2019_03_22.models.CertificateDescription
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_update(
        self,
        resource_group_name: str,
        resource_name: str,
        certificate_name: str,
        certificate_description: IO,
        if_match: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CertificateDescription:
        """Upload the certificate to the IoT hub.

        Adds new or replaces existing certificate.

        :param resource_group_name: The name of the resource group that contains the IoT hub. Required.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub. Required.
        :type resource_name: str
        :param certificate_name: The name of the certificate. Required.
        :type certificate_name: str
        :param certificate_description: The certificate body. Required.
        :type certificate_description: IO
        :param if_match: ETag of the Certificate. Do not specify for creating a brand new certificate.
         Required to update an existing certificate. Default value is None.
        :type if_match: str
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CertificateDescription or the result of cls(response)
        :rtype: ~azure.mgmt.iothub.v2019_03_22.models.CertificateDescription
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_or_update(
        self,
        resource_group_name: str,
        resource_name: str,
        certificate_name: str,
        certificate_description: Union[_models.CertificateBodyDescription, IO],
        if_match: Optional[str] = None,
        **kwargs: Any
    ) -> _models.CertificateDescription:
        """Upload the certificate to the IoT hub.

        Adds new or replaces existing certificate.

        :param resource_group_name: The name of the resource group that contains the IoT hub. Required.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub. Required.
        :type resource_name: str
        :param certificate_name: The name of the certificate. Required.
        :type certificate_name: str
        :param certificate_description: The certificate body. Is either a model type or a IO type.
         Required.
        :type certificate_description: ~azure.mgmt.iothub.v2019_03_22.models.CertificateBodyDescription
         or IO
        :param if_match: ETag of the Certificate. Do not specify for creating a brand new certificate.
         Required to update an existing certificate. Default value is None.
        :type if_match: str
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CertificateDescription or the result of cls(response)
        :rtype: ~azure.mgmt.iothub.v2019_03_22.models.CertificateDescription
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-03-22"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.CertificateDescription]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(certificate_description, (IO, bytes)):
            _content = certificate_description
        else:
            _json = self._serialize.body(certificate_description, "CertificateBodyDescription")

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            certificate_name=certificate_name,
            subscription_id=self._config.subscription_id,
            if_match=if_match,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_or_update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDetails, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("CertificateDescription", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("CertificateDescription", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}"}  # type: ignore

    @distributed_trace
    def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, resource_name: str, certificate_name: str, if_match: str, **kwargs: Any
    ) -> None:
        """Delete an X509 certificate.

        Deletes an existing X509 certificate or does nothing if it does not exist.

        :param resource_group_name: The name of the resource group that contains the IoT hub. Required.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub. Required.
        :type resource_name: str
        :param certificate_name: The name of the certificate. Required.
        :type certificate_name: str
        :param if_match: ETag of the Certificate. Required.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-03-22"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_delete_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            certificate_name=certificate_name,
            subscription_id=self._config.subscription_id,
            if_match=if_match,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDetails, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}"}  # type: ignore

    @distributed_trace
    def generate_verification_code(
        self, resource_group_name: str, resource_name: str, certificate_name: str, if_match: str, **kwargs: Any
    ) -> _models.CertificateWithNonceDescription:
        """Generate verification code for proof of possession flow.

        Generates verification code for proof of possession flow. The verification code will be used to
        generate a leaf certificate.

        :param resource_group_name: The name of the resource group that contains the IoT hub. Required.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub. Required.
        :type resource_name: str
        :param certificate_name: The name of the certificate. Required.
        :type certificate_name: str
        :param if_match: ETag of the Certificate. Required.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CertificateWithNonceDescription or the result of cls(response)
        :rtype: ~azure.mgmt.iothub.v2019_03_22.models.CertificateWithNonceDescription
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-03-22"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.CertificateWithNonceDescription]

        request = build_generate_verification_code_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            certificate_name=certificate_name,
            subscription_id=self._config.subscription_id,
            if_match=if_match,
            api_version=api_version,
            template_url=self.generate_verification_code.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDetails, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("CertificateWithNonceDescription", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    generate_verification_code.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}/generateVerificationCode"}  # type: ignore

    @overload
    def verify(
        self,
        resource_group_name: str,
        resource_name: str,
        certificate_name: str,
        if_match: str,
        certificate_verification_body: _models.CertificateVerificationDescription,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CertificateDescription:
        """Verify certificate's private key possession.

        Verifies the certificate's private key possession by providing the leaf cert issued by the
        verifying pre uploaded certificate.

        :param resource_group_name: The name of the resource group that contains the IoT hub. Required.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub. Required.
        :type resource_name: str
        :param certificate_name: The name of the certificate. Required.
        :type certificate_name: str
        :param if_match: ETag of the Certificate. Required.
        :type if_match: str
        :param certificate_verification_body: The name of the certificate. Required.
        :type certificate_verification_body:
         ~azure.mgmt.iothub.v2019_03_22.models.CertificateVerificationDescription
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CertificateDescription or the result of cls(response)
        :rtype: ~azure.mgmt.iothub.v2019_03_22.models.CertificateDescription
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def verify(
        self,
        resource_group_name: str,
        resource_name: str,
        certificate_name: str,
        if_match: str,
        certificate_verification_body: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CertificateDescription:
        """Verify certificate's private key possession.

        Verifies the certificate's private key possession by providing the leaf cert issued by the
        verifying pre uploaded certificate.

        :param resource_group_name: The name of the resource group that contains the IoT hub. Required.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub. Required.
        :type resource_name: str
        :param certificate_name: The name of the certificate. Required.
        :type certificate_name: str
        :param if_match: ETag of the Certificate. Required.
        :type if_match: str
        :param certificate_verification_body: The name of the certificate. Required.
        :type certificate_verification_body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CertificateDescription or the result of cls(response)
        :rtype: ~azure.mgmt.iothub.v2019_03_22.models.CertificateDescription
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def verify(
        self,
        resource_group_name: str,
        resource_name: str,
        certificate_name: str,
        if_match: str,
        certificate_verification_body: Union[_models.CertificateVerificationDescription, IO],
        **kwargs: Any
    ) -> _models.CertificateDescription:
        """Verify certificate's private key possession.

        Verifies the certificate's private key possession by providing the leaf cert issued by the
        verifying pre uploaded certificate.

        :param resource_group_name: The name of the resource group that contains the IoT hub. Required.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub. Required.
        :type resource_name: str
        :param certificate_name: The name of the certificate. Required.
        :type certificate_name: str
        :param if_match: ETag of the Certificate. Required.
        :type if_match: str
        :param certificate_verification_body: The name of the certificate. Is either a model type or a
         IO type. Required.
        :type certificate_verification_body:
         ~azure.mgmt.iothub.v2019_03_22.models.CertificateVerificationDescription or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CertificateDescription or the result of cls(response)
        :rtype: ~azure.mgmt.iothub.v2019_03_22.models.CertificateDescription
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-03-22"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.CertificateDescription]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(certificate_verification_body, (IO, bytes)):
            _content = certificate_verification_body
        else:
            _json = self._serialize.body(certificate_verification_body, "CertificateVerificationDescription")

        request = build_verify_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            certificate_name=certificate_name,
            subscription_id=self._config.subscription_id,
            if_match=if_match,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.verify.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDetails, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("CertificateDescription", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    verify.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}/verify"}  # type: ignore
