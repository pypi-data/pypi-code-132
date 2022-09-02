# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from userwatch import userwatch_public_pb2 as userwatch_dot_userwatch__public__pb2
from userwatch import userwatch_shepherd_pb2 as userwatch_dot_userwatch__shepherd__pb2


class ShepherdStub(object):
    """Server to server APIs

    Shepherd is the service by which customer servers can talk with Userwatch
    in backend integrations. While we may wrap it in libraries, customers can
    interact with it directly too. The caller is authenticated via project
    private api keys.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Track = channel.unary_unary(
                '/uwproto.Shepherd/Track',
                request_serializer=userwatch_dot_userwatch__shepherd__pb2.TrackEventRequest.SerializeToString,
                response_deserializer=userwatch_dot_userwatch__public__pb2.AnalysisResponse.FromString,
                )
        self.Verify = channel.unary_unary(
                '/uwproto.Shepherd/Verify',
                request_serializer=userwatch_dot_userwatch__shepherd__pb2.VerifyRequest.SerializeToString,
                response_deserializer=userwatch_dot_userwatch__public__pb2.AnalysisResponse.FromString,
                )
        self.CreateChallenge = channel.unary_unary(
                '/uwproto.Shepherd/CreateChallenge',
                request_serializer=userwatch_dot_userwatch__shepherd__pb2.CreateChallengeRequest.SerializeToString,
                response_deserializer=userwatch_dot_userwatch__shepherd__pb2.CreateChallengeResponse.FromString,
                )
        self.VerifyChallenge = channel.unary_unary(
                '/uwproto.Shepherd/VerifyChallenge',
                request_serializer=userwatch_dot_userwatch__shepherd__pb2.ChallengeVerificationRequest.SerializeToString,
                response_deserializer=userwatch_dot_userwatch__shepherd__pb2.ChallengeVerificationResponse.FromString,
                )
        self.ApproveDevice = channel.unary_unary(
                '/uwproto.Shepherd/ApproveDevice',
                request_serializer=userwatch_dot_userwatch__shepherd__pb2.DeviceRequest.SerializeToString,
                response_deserializer=userwatch_dot_userwatch__shepherd__pb2.DeviceResponse.FromString,
                )
        self.ReportDevice = channel.unary_unary(
                '/uwproto.Shepherd/ReportDevice',
                request_serializer=userwatch_dot_userwatch__shepherd__pb2.DeviceRequest.SerializeToString,
                response_deserializer=userwatch_dot_userwatch__shepherd__pb2.DeviceResponse.FromString,
                )
        self.GetDeviceList = channel.unary_unary(
                '/uwproto.Shepherd/GetDeviceList',
                request_serializer=userwatch_dot_userwatch__shepherd__pb2.DeviceListRequest.SerializeToString,
                response_deserializer=userwatch_dot_userwatch__shepherd__pb2.DeviceListResponse.FromString,
                )


class ShepherdServicer(object):
    """Server to server APIs

    Shepherd is the service by which customer servers can talk with Userwatch
    in backend integrations. While we may wrap it in libraries, customers can
    interact with it directly too. The caller is authenticated via project
    private api keys.
    """

    def Track(self, request, context):
        """Inform Userwatch of an event in your application.

        Include any UserInfo you have, or an empty UserInfo if you have none.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Verify(self, request, context):
        """Access the assessment of a user for whom an event was previously
        registered with Userwatch via a track(UserInfo, EventType) call from
        your client application.

        At this point you can also attach any additional UserInfo your server
        has which your client might not have had available.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateChallenge(self, request, context):
        """Verifying Challenge Responses
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VerifyChallenge(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ApproveDevice(self, request, context):
        """User Management
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReportDevice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDeviceList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ShepherdServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Track': grpc.unary_unary_rpc_method_handler(
                    servicer.Track,
                    request_deserializer=userwatch_dot_userwatch__shepherd__pb2.TrackEventRequest.FromString,
                    response_serializer=userwatch_dot_userwatch__public__pb2.AnalysisResponse.SerializeToString,
            ),
            'Verify': grpc.unary_unary_rpc_method_handler(
                    servicer.Verify,
                    request_deserializer=userwatch_dot_userwatch__shepherd__pb2.VerifyRequest.FromString,
                    response_serializer=userwatch_dot_userwatch__public__pb2.AnalysisResponse.SerializeToString,
            ),
            'CreateChallenge': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateChallenge,
                    request_deserializer=userwatch_dot_userwatch__shepherd__pb2.CreateChallengeRequest.FromString,
                    response_serializer=userwatch_dot_userwatch__shepherd__pb2.CreateChallengeResponse.SerializeToString,
            ),
            'VerifyChallenge': grpc.unary_unary_rpc_method_handler(
                    servicer.VerifyChallenge,
                    request_deserializer=userwatch_dot_userwatch__shepherd__pb2.ChallengeVerificationRequest.FromString,
                    response_serializer=userwatch_dot_userwatch__shepherd__pb2.ChallengeVerificationResponse.SerializeToString,
            ),
            'ApproveDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.ApproveDevice,
                    request_deserializer=userwatch_dot_userwatch__shepherd__pb2.DeviceRequest.FromString,
                    response_serializer=userwatch_dot_userwatch__shepherd__pb2.DeviceResponse.SerializeToString,
            ),
            'ReportDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.ReportDevice,
                    request_deserializer=userwatch_dot_userwatch__shepherd__pb2.DeviceRequest.FromString,
                    response_serializer=userwatch_dot_userwatch__shepherd__pb2.DeviceResponse.SerializeToString,
            ),
            'GetDeviceList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDeviceList,
                    request_deserializer=userwatch_dot_userwatch__shepherd__pb2.DeviceListRequest.FromString,
                    response_serializer=userwatch_dot_userwatch__shepherd__pb2.DeviceListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'uwproto.Shepherd', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Shepherd(object):
    """Server to server APIs

    Shepherd is the service by which customer servers can talk with Userwatch
    in backend integrations. While we may wrap it in libraries, customers can
    interact with it directly too. The caller is authenticated via project
    private api keys.
    """

    @staticmethod
    def Track(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uwproto.Shepherd/Track',
            userwatch_dot_userwatch__shepherd__pb2.TrackEventRequest.SerializeToString,
            userwatch_dot_userwatch__public__pb2.AnalysisResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Verify(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uwproto.Shepherd/Verify',
            userwatch_dot_userwatch__shepherd__pb2.VerifyRequest.SerializeToString,
            userwatch_dot_userwatch__public__pb2.AnalysisResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateChallenge(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uwproto.Shepherd/CreateChallenge',
            userwatch_dot_userwatch__shepherd__pb2.CreateChallengeRequest.SerializeToString,
            userwatch_dot_userwatch__shepherd__pb2.CreateChallengeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VerifyChallenge(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uwproto.Shepherd/VerifyChallenge',
            userwatch_dot_userwatch__shepherd__pb2.ChallengeVerificationRequest.SerializeToString,
            userwatch_dot_userwatch__shepherd__pb2.ChallengeVerificationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ApproveDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uwproto.Shepherd/ApproveDevice',
            userwatch_dot_userwatch__shepherd__pb2.DeviceRequest.SerializeToString,
            userwatch_dot_userwatch__shepherd__pb2.DeviceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReportDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uwproto.Shepherd/ReportDevice',
            userwatch_dot_userwatch__shepherd__pb2.DeviceRequest.SerializeToString,
            userwatch_dot_userwatch__shepherd__pb2.DeviceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDeviceList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uwproto.Shepherd/GetDeviceList',
            userwatch_dot_userwatch__shepherd__pb2.DeviceListRequest.SerializeToString,
            userwatch_dot_userwatch__shepherd__pb2.DeviceListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
