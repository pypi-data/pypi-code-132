# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: imp/response/response_imp.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from volcengine.imp.models.base import base_pb2 as base_dot_base__pb2
from volcengine.imp.models.business import imp_common_pb2 as imp_dot_business_dot_imp__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='imp/response/response_imp.proto',
  package='Volcengine.Imp.Models.Response',
  syntax='proto3',
  serialized_options=b'\n)com.volcengine.service.imp.model.responseB\013ImpResponseP\001ZAgithub.com/volcengine/volc-sdk-golang/service/imp/models/response\240\001\001\330\001\001\312\002 Volc\\Service\\Imp\\Models\\Response\342\002#Volc\\Service\\Imp\\Models\\GPBMetadata',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fimp/response/response_imp.proto\x12\x1eVolcengine.Imp.Models.Response\x1a\x0f\x62\x61se/base.proto\x1a\x1dimp/business/imp_common.proto\"n\n\x14ImpSubmitJobResponse\x12\x46\n\x10ResponseMetadata\x18\x01 \x01(\x0b\x32,.Volcengine.Vod.Models.Base.ResponseMetadata\x12\x0e\n\x06Result\x18\x02 \x01(\t\"\\\n\x12ImpKillJobResponse\x12\x46\n\x10ResponseMetadata\x18\x01 \x01(\x0b\x32,.Volcengine.Vod.Models.Base.ResponseMetadata\"\x91\x02\n\x16ImpRetrieveJobResponse\x12\x46\n\x10ResponseMetadata\x18\x01 \x01(\x0b\x32,.Volcengine.Vod.Models.Base.ResponseMetadata\x12R\n\x06Result\x18\x02 \x03(\x0b\x32\x42.Volcengine.Imp.Models.Response.ImpRetrieveJobResponse.ResultEntry\x1a[\n\x0bResultEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12;\n\x05value\x18\x02 \x01(\x0b\x32,.Volcengine.Imp.Models.Business.JobExecution:\x02\x38\x01\x42\xcc\x01\n)com.volcengine.service.imp.model.responseB\x0bImpResponseP\x01ZAgithub.com/volcengine/volc-sdk-golang/service/imp/models/response\xa0\x01\x01\xd8\x01\x01\xca\x02 Volc\\Service\\Imp\\Models\\Response\xe2\x02#Volc\\Service\\Imp\\Models\\GPBMetadatab\x06proto3'
  ,
  dependencies=[base_dot_base__pb2.DESCRIPTOR,imp_dot_business_dot_imp__common__pb2.DESCRIPTOR,])




_IMPSUBMITJOBRESPONSE = _descriptor.Descriptor(
  name='ImpSubmitJobResponse',
  full_name='Volcengine.Imp.Models.Response.ImpSubmitJobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ResponseMetadata', full_name='Volcengine.Imp.Models.Response.ImpSubmitJobResponse.ResponseMetadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Result', full_name='Volcengine.Imp.Models.Response.ImpSubmitJobResponse.Result', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=225,
)


_IMPKILLJOBRESPONSE = _descriptor.Descriptor(
  name='ImpKillJobResponse',
  full_name='Volcengine.Imp.Models.Response.ImpKillJobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ResponseMetadata', full_name='Volcengine.Imp.Models.Response.ImpKillJobResponse.ResponseMetadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=227,
  serialized_end=319,
)


_IMPRETRIEVEJOBRESPONSE_RESULTENTRY = _descriptor.Descriptor(
  name='ResultEntry',
  full_name='Volcengine.Imp.Models.Response.ImpRetrieveJobResponse.ResultEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Volcengine.Imp.Models.Response.ImpRetrieveJobResponse.ResultEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='Volcengine.Imp.Models.Response.ImpRetrieveJobResponse.ResultEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=504,
  serialized_end=595,
)

_IMPRETRIEVEJOBRESPONSE = _descriptor.Descriptor(
  name='ImpRetrieveJobResponse',
  full_name='Volcengine.Imp.Models.Response.ImpRetrieveJobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ResponseMetadata', full_name='Volcengine.Imp.Models.Response.ImpRetrieveJobResponse.ResponseMetadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Result', full_name='Volcengine.Imp.Models.Response.ImpRetrieveJobResponse.Result', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_IMPRETRIEVEJOBRESPONSE_RESULTENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=322,
  serialized_end=595,
)

_IMPSUBMITJOBRESPONSE.fields_by_name['ResponseMetadata'].message_type = base_dot_base__pb2._RESPONSEMETADATA
_IMPKILLJOBRESPONSE.fields_by_name['ResponseMetadata'].message_type = base_dot_base__pb2._RESPONSEMETADATA
_IMPRETRIEVEJOBRESPONSE_RESULTENTRY.fields_by_name['value'].message_type = imp_dot_business_dot_imp__common__pb2._JOBEXECUTION
_IMPRETRIEVEJOBRESPONSE_RESULTENTRY.containing_type = _IMPRETRIEVEJOBRESPONSE
_IMPRETRIEVEJOBRESPONSE.fields_by_name['ResponseMetadata'].message_type = base_dot_base__pb2._RESPONSEMETADATA
_IMPRETRIEVEJOBRESPONSE.fields_by_name['Result'].message_type = _IMPRETRIEVEJOBRESPONSE_RESULTENTRY
DESCRIPTOR.message_types_by_name['ImpSubmitJobResponse'] = _IMPSUBMITJOBRESPONSE
DESCRIPTOR.message_types_by_name['ImpKillJobResponse'] = _IMPKILLJOBRESPONSE
DESCRIPTOR.message_types_by_name['ImpRetrieveJobResponse'] = _IMPRETRIEVEJOBRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImpSubmitJobResponse = _reflection.GeneratedProtocolMessageType('ImpSubmitJobResponse', (_message.Message,), {
  'DESCRIPTOR' : _IMPSUBMITJOBRESPONSE,
  '__module__' : 'imp.response.response_imp_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Imp.Models.Response.ImpSubmitJobResponse)
  })
_sym_db.RegisterMessage(ImpSubmitJobResponse)

ImpKillJobResponse = _reflection.GeneratedProtocolMessageType('ImpKillJobResponse', (_message.Message,), {
  'DESCRIPTOR' : _IMPKILLJOBRESPONSE,
  '__module__' : 'imp.response.response_imp_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Imp.Models.Response.ImpKillJobResponse)
  })
_sym_db.RegisterMessage(ImpKillJobResponse)

ImpRetrieveJobResponse = _reflection.GeneratedProtocolMessageType('ImpRetrieveJobResponse', (_message.Message,), {

  'ResultEntry' : _reflection.GeneratedProtocolMessageType('ResultEntry', (_message.Message,), {
    'DESCRIPTOR' : _IMPRETRIEVEJOBRESPONSE_RESULTENTRY,
    '__module__' : 'imp.response.response_imp_pb2'
    # @@protoc_insertion_point(class_scope:Volcengine.Imp.Models.Response.ImpRetrieveJobResponse.ResultEntry)
    })
  ,
  'DESCRIPTOR' : _IMPRETRIEVEJOBRESPONSE,
  '__module__' : 'imp.response.response_imp_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Imp.Models.Response.ImpRetrieveJobResponse)
  })
_sym_db.RegisterMessage(ImpRetrieveJobResponse)
_sym_db.RegisterMessage(ImpRetrieveJobResponse.ResultEntry)


DESCRIPTOR._options = None
_IMPRETRIEVEJOBRESPONSE_RESULTENTRY._options = None
# @@protoc_insertion_point(module_scope)
