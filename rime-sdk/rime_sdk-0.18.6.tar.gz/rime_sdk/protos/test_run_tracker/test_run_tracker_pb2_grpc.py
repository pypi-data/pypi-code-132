# autogenerated
# mypy: ignore-errors
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from rime_sdk.protos.test_run_tracker import test_run_tracker_pb2 as protos_dot_test__run__tracker_dot_test__run__tracker__pb2


class TestRunTrackerStub(object):
    """The TestRunTracker and all of its RPCs are deprecated.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetOperationState = channel.unary_unary(
                '/rime.TestRunTracker/GetOperationState',
                request_serializer=protos_dot_test__run__tracker_dot_test__run__tracker__pb2.GetOperationStateRequest.SerializeToString,
                response_deserializer=protos_dot_test__run__tracker_dot_test__run__tracker__pb2.GetOperationStateResponse.FromString,
                )


class TestRunTrackerServicer(object):
    """The TestRunTracker and all of its RPCs are deprecated.
    """

    def GetOperationState(self, request, context):
        """GetOperationState

        DEPRECATED: DO NOT USE.
        Get an operation's current state based on all published events for it.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TestRunTrackerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetOperationState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOperationState,
                    request_deserializer=protos_dot_test__run__tracker_dot_test__run__tracker__pb2.GetOperationStateRequest.FromString,
                    response_serializer=protos_dot_test__run__tracker_dot_test__run__tracker__pb2.GetOperationStateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'rime.TestRunTracker', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TestRunTracker(object):
    """The TestRunTracker and all of its RPCs are deprecated.
    """

    @staticmethod
    def GetOperationState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rime.TestRunTracker/GetOperationState',
            protos_dot_test__run__tracker_dot_test__run__tracker__pb2.GetOperationStateRequest.SerializeToString,
            protos_dot_test__run__tracker_dot_test__run__tracker__pb2.GetOperationStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
