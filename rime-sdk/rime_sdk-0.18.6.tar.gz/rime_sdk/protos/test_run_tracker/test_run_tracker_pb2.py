# autogenerated
# mypy: ignore-errors
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/test_run_tracker/test_run_tracker.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from rime_sdk.protos.google.api import annotations_pb2 as protos_dot_google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.protos/test_run_tracker/test_run_tracker.proto\x12\x04rime\x1a#protos/google/api/annotations.proto\"*\n\x18GetOperationStateRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\t\"\x81\x05\n\x19GetOperationStateResponse\x12;\n\tjob_state\x18\x02 \x01(\x0b\x32(.rime.GetOperationStateResponse.JobState\x12H\n\x10test_suite_state\x18\x01 \x01(\x0b\x32..rime.GetOperationStateResponse.TestSuiteState\x1a;\n\x08JobState\x12/\n\x10operation_status\x18\x01 \x01(\x0e\x32\x15.rime.OperationStatus\x1a\xa3\x01\n\x0eTestSuiteState\x12\x15\n\rtest_suite_id\x18\x01 \x01(\t\x12/\n\x10operation_status\x18\x02 \x01(\x0e\x32\x15.rime.OperationStatus\x12I\n\x11test_batch_states\x18\x03 \x03(\x0b\x32..rime.GetOperationStateResponse.TestBatchState\x1a\xa1\x01\n\x0eTestBatchState\x12\x15\n\rtest_batch_id\x18\x01 \x01(\t\x12/\n\x10operation_status\x18\x02 \x01(\x0e\x32\x15.rime.OperationStatus\x12G\n\x10test_case_states\x18\x03 \x03(\x0b\x32-.rime.GetOperationStateResponse.TestCaseState\x1aV\n\rTestCaseState\x12\x14\n\x0ctest_case_id\x18\x01 \x01(\t\x12/\n\x10operation_status\x18\x02 \x01(\x0e\x32\x15.rime.OperationStatus*\x8f\x01\n\x0fOperationStatus\x12 \n\x1cOPERATION_STATUS_UNSPECIFIED\x10\x00\x12\x1c\n\x18OPERATION_STATUS_PENDING\x10\x01\x12\x1c\n\x18OPERATION_STATUS_RUNNING\x10\x02\x12\x1e\n\x1aOPERATION_STATUS_COMPLETED\x10\x03\x32\x94\x01\n\x0eTestRunTracker\x12}\n\x11GetOperationState\x12\x1e.rime.GetOperationStateRequest\x1a\x1f.rime.GetOperationStateResponse\"\'\x88\x02\x01\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/operation-state/{job_id}\x1a\x03\x88\x02\x01\x42\x1fZ\x1dri/_gen/protos/testruntrackerb\x06proto3')

_OPERATIONSTATUS = DESCRIPTOR.enum_types_by_name['OperationStatus']
OperationStatus = enum_type_wrapper.EnumTypeWrapper(_OPERATIONSTATUS)
OPERATION_STATUS_UNSPECIFIED = 0
OPERATION_STATUS_PENDING = 1
OPERATION_STATUS_RUNNING = 2
OPERATION_STATUS_COMPLETED = 3


_GETOPERATIONSTATEREQUEST = DESCRIPTOR.message_types_by_name['GetOperationStateRequest']
_GETOPERATIONSTATERESPONSE = DESCRIPTOR.message_types_by_name['GetOperationStateResponse']
_GETOPERATIONSTATERESPONSE_JOBSTATE = _GETOPERATIONSTATERESPONSE.nested_types_by_name['JobState']
_GETOPERATIONSTATERESPONSE_TESTSUITESTATE = _GETOPERATIONSTATERESPONSE.nested_types_by_name['TestSuiteState']
_GETOPERATIONSTATERESPONSE_TESTBATCHSTATE = _GETOPERATIONSTATERESPONSE.nested_types_by_name['TestBatchState']
_GETOPERATIONSTATERESPONSE_TESTCASESTATE = _GETOPERATIONSTATERESPONSE.nested_types_by_name['TestCaseState']
GetOperationStateRequest = _reflection.GeneratedProtocolMessageType('GetOperationStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETOPERATIONSTATEREQUEST,
  '__module__' : 'protos.test_run_tracker.test_run_tracker_pb2'
  # @@protoc_insertion_point(class_scope:rime.GetOperationStateRequest)
  })
_sym_db.RegisterMessage(GetOperationStateRequest)

GetOperationStateResponse = _reflection.GeneratedProtocolMessageType('GetOperationStateResponse', (_message.Message,), {

  'JobState' : _reflection.GeneratedProtocolMessageType('JobState', (_message.Message,), {
    'DESCRIPTOR' : _GETOPERATIONSTATERESPONSE_JOBSTATE,
    '__module__' : 'protos.test_run_tracker.test_run_tracker_pb2'
    # @@protoc_insertion_point(class_scope:rime.GetOperationStateResponse.JobState)
    })
  ,

  'TestSuiteState' : _reflection.GeneratedProtocolMessageType('TestSuiteState', (_message.Message,), {
    'DESCRIPTOR' : _GETOPERATIONSTATERESPONSE_TESTSUITESTATE,
    '__module__' : 'protos.test_run_tracker.test_run_tracker_pb2'
    # @@protoc_insertion_point(class_scope:rime.GetOperationStateResponse.TestSuiteState)
    })
  ,

  'TestBatchState' : _reflection.GeneratedProtocolMessageType('TestBatchState', (_message.Message,), {
    'DESCRIPTOR' : _GETOPERATIONSTATERESPONSE_TESTBATCHSTATE,
    '__module__' : 'protos.test_run_tracker.test_run_tracker_pb2'
    # @@protoc_insertion_point(class_scope:rime.GetOperationStateResponse.TestBatchState)
    })
  ,

  'TestCaseState' : _reflection.GeneratedProtocolMessageType('TestCaseState', (_message.Message,), {
    'DESCRIPTOR' : _GETOPERATIONSTATERESPONSE_TESTCASESTATE,
    '__module__' : 'protos.test_run_tracker.test_run_tracker_pb2'
    # @@protoc_insertion_point(class_scope:rime.GetOperationStateResponse.TestCaseState)
    })
  ,
  'DESCRIPTOR' : _GETOPERATIONSTATERESPONSE,
  '__module__' : 'protos.test_run_tracker.test_run_tracker_pb2'
  # @@protoc_insertion_point(class_scope:rime.GetOperationStateResponse)
  })
_sym_db.RegisterMessage(GetOperationStateResponse)
_sym_db.RegisterMessage(GetOperationStateResponse.JobState)
_sym_db.RegisterMessage(GetOperationStateResponse.TestSuiteState)
_sym_db.RegisterMessage(GetOperationStateResponse.TestBatchState)
_sym_db.RegisterMessage(GetOperationStateResponse.TestCaseState)

_TESTRUNTRACKER = DESCRIPTOR.services_by_name['TestRunTracker']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\035ri/_gen/protos/testruntracker'
  _TESTRUNTRACKER._options = None
  _TESTRUNTRACKER._serialized_options = b'\210\002\001'
  _TESTRUNTRACKER.methods_by_name['GetOperationState']._options = None
  _TESTRUNTRACKER.methods_by_name['GetOperationState']._serialized_options = b'\210\002\001\202\323\344\223\002\036\022\034/v1/operation-state/{job_id}'
  _OPERATIONSTATUS._serialized_start=782
  _OPERATIONSTATUS._serialized_end=925
  _GETOPERATIONSTATEREQUEST._serialized_start=93
  _GETOPERATIONSTATEREQUEST._serialized_end=135
  _GETOPERATIONSTATERESPONSE._serialized_start=138
  _GETOPERATIONSTATERESPONSE._serialized_end=779
  _GETOPERATIONSTATERESPONSE_JOBSTATE._serialized_start=302
  _GETOPERATIONSTATERESPONSE_JOBSTATE._serialized_end=361
  _GETOPERATIONSTATERESPONSE_TESTSUITESTATE._serialized_start=364
  _GETOPERATIONSTATERESPONSE_TESTSUITESTATE._serialized_end=527
  _GETOPERATIONSTATERESPONSE_TESTBATCHSTATE._serialized_start=530
  _GETOPERATIONSTATERESPONSE_TESTBATCHSTATE._serialized_end=691
  _GETOPERATIONSTATERESPONSE_TESTCASESTATE._serialized_start=693
  _GETOPERATIONSTATERESPONSE_TESTCASESTATE._serialized_end=779
  _TESTRUNTRACKER._serialized_start=928
  _TESTRUNTRACKER._serialized_end=1076
# @@protoc_insertion_point(module_scope)
