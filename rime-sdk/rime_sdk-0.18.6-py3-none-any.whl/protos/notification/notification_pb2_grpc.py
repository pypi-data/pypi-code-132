# autogenerated
# mypy: ignore-errors
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from rime_sdk.protos.notification import notification_pb2 as protos_dot_notification_dot_notification__pb2


class NotificationSettingStub(object):
    """CRUD endpoints for interacting with notification settings.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListNotifications = channel.unary_unary(
                '/rime.NotificationSetting/ListNotifications',
                request_serializer=protos_dot_notification_dot_notification__pb2.ListNotificationsRequest.SerializeToString,
                response_deserializer=protos_dot_notification_dot_notification__pb2.ListNotificationsResponse.FromString,
                )
        self.UpdateNotification = channel.unary_unary(
                '/rime.NotificationSetting/UpdateNotification',
                request_serializer=protos_dot_notification_dot_notification__pb2.UpdateNotificationRequest.SerializeToString,
                response_deserializer=protos_dot_notification_dot_notification__pb2.UpdateNotificationResponse.FromString,
                )
        self.CreateNotification = channel.unary_unary(
                '/rime.NotificationSetting/CreateNotification',
                request_serializer=protos_dot_notification_dot_notification__pb2.CreateNotificationRequest.SerializeToString,
                response_deserializer=protos_dot_notification_dot_notification__pb2.CreateNotificationResponse.FromString,
                )
        self.DeleteNotification = channel.unary_unary(
                '/rime.NotificationSetting/DeleteNotification',
                request_serializer=protos_dot_notification_dot_notification__pb2.DeleteNotificationRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.SendRIEmail = channel.unary_unary(
                '/rime.NotificationSetting/SendRIEmail',
                request_serializer=protos_dot_notification_dot_notification__pb2.SendRIEmailRequest.SerializeToString,
                response_deserializer=protos_dot_notification_dot_notification__pb2.SendRIEmailResponse.FromString,
                )


class NotificationSettingServicer(object):
    """CRUD endpoints for interacting with notification settings.
    """

    def ListNotifications(self, request, context):
        """ListNotifications

        Lists notification settings with options to filter by project or the
        type of notification.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateNotification(self, request, context):
        """UpdateNotification

        Updates an existing notification setting.
        The ID in the provided notification is used to identify it.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateNotification(self, request, context):
        """CreateNotification

        Creates a new notification setting.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteNotification(self, request, context):
        """DeleteNotification

        Hard-delete a notification setting.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendRIEmail(self, request, context):
        """RPC for sending emails to Robust Intelligence addresses (e.g.
        feedback or sales contact from a self serve deployment).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NotificationSettingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListNotifications': grpc.unary_unary_rpc_method_handler(
                    servicer.ListNotifications,
                    request_deserializer=protos_dot_notification_dot_notification__pb2.ListNotificationsRequest.FromString,
                    response_serializer=protos_dot_notification_dot_notification__pb2.ListNotificationsResponse.SerializeToString,
            ),
            'UpdateNotification': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateNotification,
                    request_deserializer=protos_dot_notification_dot_notification__pb2.UpdateNotificationRequest.FromString,
                    response_serializer=protos_dot_notification_dot_notification__pb2.UpdateNotificationResponse.SerializeToString,
            ),
            'CreateNotification': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateNotification,
                    request_deserializer=protos_dot_notification_dot_notification__pb2.CreateNotificationRequest.FromString,
                    response_serializer=protos_dot_notification_dot_notification__pb2.CreateNotificationResponse.SerializeToString,
            ),
            'DeleteNotification': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteNotification,
                    request_deserializer=protos_dot_notification_dot_notification__pb2.DeleteNotificationRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SendRIEmail': grpc.unary_unary_rpc_method_handler(
                    servicer.SendRIEmail,
                    request_deserializer=protos_dot_notification_dot_notification__pb2.SendRIEmailRequest.FromString,
                    response_serializer=protos_dot_notification_dot_notification__pb2.SendRIEmailResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'rime.NotificationSetting', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NotificationSetting(object):
    """CRUD endpoints for interacting with notification settings.
    """

    @staticmethod
    def ListNotifications(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rime.NotificationSetting/ListNotifications',
            protos_dot_notification_dot_notification__pb2.ListNotificationsRequest.SerializeToString,
            protos_dot_notification_dot_notification__pb2.ListNotificationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateNotification(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rime.NotificationSetting/UpdateNotification',
            protos_dot_notification_dot_notification__pb2.UpdateNotificationRequest.SerializeToString,
            protos_dot_notification_dot_notification__pb2.UpdateNotificationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateNotification(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rime.NotificationSetting/CreateNotification',
            protos_dot_notification_dot_notification__pb2.CreateNotificationRequest.SerializeToString,
            protos_dot_notification_dot_notification__pb2.CreateNotificationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteNotification(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rime.NotificationSetting/DeleteNotification',
            protos_dot_notification_dot_notification__pb2.DeleteNotificationRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendRIEmail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rime.NotificationSetting/SendRIEmail',
            protos_dot_notification_dot_notification__pb2.SendRIEmailRequest.SerializeToString,
            protos_dot_notification_dot_notification__pb2.SendRIEmailResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
