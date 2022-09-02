# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AccessRights(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The permissions assigned to the shared access policy."""

    REGISTRY_READ = "RegistryRead"
    REGISTRY_WRITE = "RegistryWrite"
    SERVICE_CONNECT = "ServiceConnect"
    DEVICE_CONNECT = "DeviceConnect"
    REGISTRY_READ_REGISTRY_WRITE = "RegistryRead, RegistryWrite"
    REGISTRY_READ_SERVICE_CONNECT = "RegistryRead, ServiceConnect"
    REGISTRY_READ_DEVICE_CONNECT = "RegistryRead, DeviceConnect"
    REGISTRY_WRITE_SERVICE_CONNECT = "RegistryWrite, ServiceConnect"
    REGISTRY_WRITE_DEVICE_CONNECT = "RegistryWrite, DeviceConnect"
    SERVICE_CONNECT_DEVICE_CONNECT = "ServiceConnect, DeviceConnect"
    REGISTRY_READ_REGISTRY_WRITE_SERVICE_CONNECT = "RegistryRead, RegistryWrite, ServiceConnect"
    REGISTRY_READ_REGISTRY_WRITE_DEVICE_CONNECT = "RegistryRead, RegistryWrite, DeviceConnect"
    REGISTRY_READ_SERVICE_CONNECT_DEVICE_CONNECT = "RegistryRead, ServiceConnect, DeviceConnect"
    REGISTRY_WRITE_SERVICE_CONNECT_DEVICE_CONNECT = "RegistryWrite, ServiceConnect, DeviceConnect"
    REGISTRY_READ_REGISTRY_WRITE_SERVICE_CONNECT_DEVICE_CONNECT = (
        "RegistryRead, RegistryWrite, ServiceConnect, DeviceConnect"
    )


class AuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies authentication type being used for connecting to the storage account."""

    KEY_BASED = "keyBased"
    IDENTITY_BASED = "identityBased"


class Capabilities(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The capabilities and features enabled for the IoT hub."""

    NONE = "None"
    DEVICE_MANAGEMENT = "DeviceManagement"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class DefaultAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Default Action for Network Rule Set."""

    DENY = "Deny"
    ALLOW = "Allow"


class EndpointHealthStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Health statuses have following meanings. The 'healthy' status shows that the endpoint is
    accepting messages as expected. The 'unhealthy' status shows that the endpoint is not accepting
    messages as expected and IoT Hub is retrying to send data to this endpoint. The status of an
    unhealthy endpoint will be updated to healthy when IoT Hub has established an eventually
    consistent state of health. The 'dead' status shows that the endpoint is not accepting
    messages, after IoT Hub retried sending messages for the retrial period. See IoT Hub metrics to
    identify errors and monitor issues with endpoints. The 'unknown' status shows that the IoT Hub
    has not established a connection with the endpoint. No messages have been delivered to or
    rejected from this endpoint.
    """

    UNKNOWN = "unknown"
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"
    DEAD = "dead"


class IotHubNameUnavailabilityReason(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The reason for unavailability."""

    INVALID = "Invalid"
    ALREADY_EXISTS = "AlreadyExists"


class IotHubReplicaRoleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The role of the region, can be either primary or secondary. The primary region is where the IoT
    hub is currently provisioned. The secondary region is the Azure disaster recovery (DR) paired
    region and also the region where the IoT hub can failover to.
    """

    PRIMARY = "primary"
    SECONDARY = "secondary"


class IotHubScaleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the scaling enabled."""

    AUTOMATIC = "Automatic"
    MANUAL = "Manual"
    NONE = "None"


class IotHubSku(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The name of the SKU."""

    F1 = "F1"
    S1 = "S1"
    S2 = "S2"
    S3 = "S3"
    B1 = "B1"
    B2 = "B2"
    B3 = "B3"


class IotHubSkuTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The billing tier for the IoT hub."""

    FREE = "Free"
    STANDARD = "Standard"
    BASIC = "Basic"


class IpFilterActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The desired action for requests captured by this rule."""

    ACCEPT = "Accept"
    REJECT = "Reject"


class JobStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of the job."""

    UNKNOWN = "unknown"
    ENQUEUED = "enqueued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class JobType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the job."""

    UNKNOWN = "unknown"
    EXPORT = "export"
    IMPORT = "import"
    BACKUP = "backup"
    READ_DEVICE_PROPERTIES = "readDeviceProperties"
    WRITE_DEVICE_PROPERTIES = "writeDeviceProperties"
    UPDATE_DEVICE_CONFIGURATION = "updateDeviceConfiguration"
    REBOOT_DEVICE = "rebootDevice"
    FACTORY_RESET_DEVICE = "factoryResetDevice"
    FIRMWARE_UPDATE = "firmwareUpdate"


class NetworkRuleIPAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """IP Filter Action."""

    ALLOW = "Allow"


class PrivateLinkServiceConnectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of a private endpoint connection."""

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"


class PublicNetworkAccess(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether requests from Public Network are allowed."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ResourceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes
    both an implicitly created identity and a set of user assigned identities. The type 'None' will
    remove any identities from the service.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    NONE = "None"


class RouteErrorSeverity(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Severity of the route error."""

    ERROR = "error"
    WARNING = "warning"


class RoutingSource(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The source that the routing rule is to be applied to, such as DeviceMessages."""

    INVALID = "Invalid"
    DEVICE_MESSAGES = "DeviceMessages"
    TWIN_CHANGE_EVENTS = "TwinChangeEvents"
    DEVICE_LIFECYCLE_EVENTS = "DeviceLifecycleEvents"
    DEVICE_JOB_LIFECYCLE_EVENTS = "DeviceJobLifecycleEvents"
    DIGITAL_TWIN_CHANGE_EVENTS = "DigitalTwinChangeEvents"
    DEVICE_CONNECTION_STATE_EVENTS = "DeviceConnectionStateEvents"
    MQTT_BROKER_MESSAGES = "MqttBrokerMessages"


class RoutingStorageContainerPropertiesEncoding(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Encoding that is used to serialize messages to blobs. Supported values are 'avro',
    'avrodeflate', and 'JSON'. Default value is 'avro'.
    """

    AVRO = "Avro"
    AVRO_DEFLATE = "AvroDeflate"
    JSON = "JSON"


class TestResultStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Result of testing route."""

    UNDEFINED = "undefined"
    FALSE = "false"
    TRUE = "true"
