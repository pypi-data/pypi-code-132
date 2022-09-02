# type: ignore
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: raft.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\nraft.proto"\x94\x01\n\x14\x41ppendEntriesRequest\x12\x0c\n\x04term\x18\x01 \x01(\x04\x12\x11\n\tleader_id\x18\x02 \x01(\t\x12\x16\n\x0eprev_log_index\x18\x03 \x01(\x04\x12\x15\n\rprev_log_term\x18\x04 \x01(\x04\x12\x15\n\x07\x65ntries\x18\x05 \x03(\x0b\x32\x04.Log\x12\x15\n\rleader_commit\x18\x06 \x01(\x04"6\n\x15\x41ppendEntriesResponse\x12\x0c\n\x04term\x18\x01 \x01(\x04\x12\x0f\n\x07success\x18\x02 \x01(\x08"g\n\x12RequestVoteRequest\x12\x0c\n\x04term\x18\x01 \x01(\x04\x12\x14\n\x0c\x63\x61ndidate_id\x18\x02 \x01(\t\x12\x16\n\x0elast_log_index\x18\x03 \x01(\x04\x12\x15\n\rlast_log_term\x18\x04 \x01(\x04"9\n\x13RequestVoteResponse\x12\x0c\n\x04term\x18\x01 \x01(\x04\x12\x14\n\x0cvote_granted\x18\x02 \x01(\x08"3\n\x03Log\x12\r\n\x05index\x18\x01 \x01(\x04\x12\x0c\n\x04term\x18\x02 \x01(\x04\x12\x0f\n\x07\x63ommand\x18\x03 \x01(\t2\x87\x01\n\x0bRaftService\x12>\n\rAppendEntries\x12\x15.AppendEntriesRequest\x1a\x16.AppendEntriesResponse\x12\x38\n\x0bRequestVote\x12\x13.RequestVoteRequest\x1a\x14.RequestVoteResponseb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "raft_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _APPENDENTRIESREQUEST._serialized_start = 15
    _APPENDENTRIESREQUEST._serialized_end = 163
    _APPENDENTRIESRESPONSE._serialized_start = 165
    _APPENDENTRIESRESPONSE._serialized_end = 219
    _REQUESTVOTEREQUEST._serialized_start = 221
    _REQUESTVOTEREQUEST._serialized_end = 324
    _REQUESTVOTERESPONSE._serialized_start = 326
    _REQUESTVOTERESPONSE._serialized_end = 383
    _LOG._serialized_start = 385
    _LOG._serialized_end = 436
    _RAFTSERVICE._serialized_start = 439
    _RAFTSERVICE._serialized_end = 574
# @@protoc_insertion_point(module_scope)
