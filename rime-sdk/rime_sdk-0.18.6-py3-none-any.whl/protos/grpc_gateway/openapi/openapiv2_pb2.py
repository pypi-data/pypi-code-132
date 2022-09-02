# autogenerated
# mypy: ignore-errors
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/grpc_gateway/openapi/openapiv2.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+protos/grpc_gateway/openapi/openapiv2.proto\x12\x14grpc_gateway.openapi\x1a\x1cgoogle/protobuf/struct.proto\"\xb5\x05\n\x07Swagger\x12\x0f\n\x07swagger\x18\x01 \x01(\t\x12(\n\x04info\x18\x02 \x01(\x0b\x32\x1a.grpc_gateway.openapi.Info\x12\x0c\n\x04host\x18\x03 \x01(\t\x12\x11\n\tbase_path\x18\x04 \x01(\t\x12-\n\x07schemes\x18\x05 \x03(\x0e\x32\x1c.grpc_gateway.openapi.Scheme\x12\x10\n\x08\x63onsumes\x18\x06 \x03(\t\x12\x10\n\x08produces\x18\x07 \x03(\t\x12?\n\tresponses\x18\n \x03(\x0b\x32,.grpc_gateway.openapi.Swagger.ResponsesEntry\x12G\n\x14security_definitions\x18\x0b \x01(\x0b\x32).grpc_gateway.openapi.SecurityDefinitions\x12;\n\x08security\x18\x0c \x03(\x0b\x32).grpc_gateway.openapi.SecurityRequirement\x12\x42\n\rexternal_docs\x18\x0e \x01(\x0b\x32+.grpc_gateway.openapi.ExternalDocumentation\x12\x41\n\nextensions\x18\x0f \x03(\x0b\x32-.grpc_gateway.openapi.Swagger.ExtensionsEntry\x1aP\n\x0eResponsesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12-\n\x05value\x18\x02 \x01(\x0b\x32\x1e.grpc_gateway.openapi.Response:\x02\x38\x01\x1aI\n\x0f\x45xtensionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value:\x02\x38\x01J\x04\x08\x08\x10\tJ\x04\x08\t\x10\nJ\x04\x08\r\x10\x0e\"\xe8\x04\n\tOperation\x12\x0c\n\x04tags\x18\x01 \x03(\t\x12\x0f\n\x07summary\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x42\n\rexternal_docs\x18\x04 \x01(\x0b\x32+.grpc_gateway.openapi.ExternalDocumentation\x12\x14\n\x0coperation_id\x18\x05 \x01(\t\x12\x10\n\x08\x63onsumes\x18\x06 \x03(\t\x12\x10\n\x08produces\x18\x07 \x03(\t\x12\x41\n\tresponses\x18\t \x03(\x0b\x32..grpc_gateway.openapi.Operation.ResponsesEntry\x12-\n\x07schemes\x18\n \x03(\x0e\x32\x1c.grpc_gateway.openapi.Scheme\x12\x12\n\ndeprecated\x18\x0b \x01(\x08\x12;\n\x08security\x18\x0c \x03(\x0b\x32).grpc_gateway.openapi.SecurityRequirement\x12\x43\n\nextensions\x18\r \x03(\x0b\x32/.grpc_gateway.openapi.Operation.ExtensionsEntry\x1aP\n\x0eResponsesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12-\n\x05value\x18\x02 \x01(\x0b\x32\x1e.grpc_gateway.openapi.Response:\x02\x38\x01\x1aI\n\x0f\x45xtensionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value:\x02\x38\x01J\x04\x08\x08\x10\t\"\xab\x01\n\x06Header\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x06 \x01(\t\x12\x0f\n\x07pattern\x18\r \x01(\tJ\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06J\x04\x08\x07\x10\x08J\x04\x08\x08\x10\tJ\x04\x08\t\x10\nJ\x04\x08\n\x10\x0bJ\x04\x08\x0b\x10\x0cJ\x04\x08\x0c\x10\rJ\x04\x08\x0e\x10\x0fJ\x04\x08\x0f\x10\x10J\x04\x08\x10\x10\x11J\x04\x08\x11\x10\x12J\x04\x08\x12\x10\x13\"\xd9\x03\n\x08Response\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12,\n\x06schema\x18\x02 \x01(\x0b\x32\x1c.grpc_gateway.openapi.Schema\x12<\n\x07headers\x18\x03 \x03(\x0b\x32+.grpc_gateway.openapi.Response.HeadersEntry\x12>\n\x08\x65xamples\x18\x04 \x03(\x0b\x32,.grpc_gateway.openapi.Response.ExamplesEntry\x12\x42\n\nextensions\x18\x05 \x03(\x0b\x32..grpc_gateway.openapi.Response.ExtensionsEntry\x1aL\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.grpc_gateway.openapi.Header:\x02\x38\x01\x1a/\n\rExamplesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aI\n\x0f\x45xtensionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value:\x02\x38\x01\"\xc0\x02\n\x04Info\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x18\n\x10terms_of_service\x18\x03 \x01(\t\x12.\n\x07\x63ontact\x18\x04 \x01(\x0b\x32\x1d.grpc_gateway.openapi.Contact\x12.\n\x07license\x18\x05 \x01(\x0b\x32\x1d.grpc_gateway.openapi.License\x12\x0f\n\x07version\x18\x06 \x01(\t\x12>\n\nextensions\x18\x07 \x03(\x0b\x32*.grpc_gateway.openapi.Info.ExtensionsEntry\x1aI\n\x0f\x45xtensionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value:\x02\x38\x01\"3\n\x07\x43ontact\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"$\n\x07License\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\"9\n\x15\x45xternalDocumentation\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\"\xc4\x01\n\x06Schema\x12\x35\n\x0bjson_schema\x18\x01 \x01(\x0b\x32 .grpc_gateway.openapi.JSONSchema\x12\x15\n\rdiscriminator\x18\x02 \x01(\t\x12\x11\n\tread_only\x18\x03 \x01(\x08\x12\x42\n\rexternal_docs\x18\x05 \x01(\x0b\x32+.grpc_gateway.openapi.ExternalDocumentation\x12\x0f\n\x07\x65xample\x18\x06 \x01(\tJ\x04\x08\x04\x10\x05\"\xd2\x06\n\nJSONSchema\x12\x0b\n\x03ref\x18\x03 \x01(\t\x12\r\n\x05title\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x07 \x01(\t\x12\x11\n\tread_only\x18\x08 \x01(\x08\x12\x0f\n\x07\x65xample\x18\t \x01(\t\x12\x13\n\x0bmultiple_of\x18\n \x01(\x01\x12\x0f\n\x07maximum\x18\x0b \x01(\x01\x12\x19\n\x11\x65xclusive_maximum\x18\x0c \x01(\x08\x12\x0f\n\x07minimum\x18\r \x01(\x01\x12\x19\n\x11\x65xclusive_minimum\x18\x0e \x01(\x08\x12\x12\n\nmax_length\x18\x0f \x01(\x04\x12\x12\n\nmin_length\x18\x10 \x01(\x04\x12\x0f\n\x07pattern\x18\x11 \x01(\t\x12\x11\n\tmax_items\x18\x14 \x01(\x04\x12\x11\n\tmin_items\x18\x15 \x01(\x04\x12\x14\n\x0cunique_items\x18\x16 \x01(\x08\x12\x16\n\x0emax_properties\x18\x18 \x01(\x04\x12\x16\n\x0emin_properties\x18\x19 \x01(\x04\x12\x10\n\x08required\x18\x1a \x03(\t\x12\r\n\x05\x61rray\x18\" \x03(\t\x12\x44\n\x04type\x18# \x03(\x0e\x32\x36.grpc_gateway.openapi.JSONSchema.JSONSchemaSimpleTypes\x12\x0e\n\x06\x66ormat\x18$ \x01(\t\x12\x0c\n\x04\x65num\x18. \x03(\t\x12Q\n\x13\x66ield_configuration\x18\xe9\x07 \x01(\x0b\x32\x33.grpc_gateway.openapi.JSONSchema.FieldConfiguration\x1a-\n\x12\x46ieldConfiguration\x12\x17\n\x0fpath_param_name\x18/ \x01(\t\"w\n\x15JSONSchemaSimpleTypes\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05\x41RRAY\x10\x01\x12\x0b\n\x07\x42OOLEAN\x10\x02\x12\x0b\n\x07INTEGER\x10\x03\x12\x08\n\x04NULL\x10\x04\x12\n\n\x06NUMBER\x10\x05\x12\n\n\x06OBJECT\x10\x06\x12\n\n\x06STRING\x10\x07J\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x04\x10\x05J\x04\x08\x12\x10\x13J\x04\x08\x13\x10\x14J\x04\x08\x17\x10\x18J\x04\x08\x1b\x10\x1cJ\x04\x08\x1c\x10\x1dJ\x04\x08\x1d\x10\x1eJ\x04\x08\x1e\x10\"J\x04\x08%\x10*J\x04\x08*\x10+J\x04\x08+\x10.\"d\n\x03Tag\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x42\n\rexternal_docs\x18\x03 \x01(\x0b\x32+.grpc_gateway.openapi.ExternalDocumentationJ\x04\x08\x01\x10\x02\"\xb7\x01\n\x13SecurityDefinitions\x12I\n\x08security\x18\x01 \x03(\x0b\x32\x37.grpc_gateway.openapi.SecurityDefinitions.SecurityEntry\x1aU\n\rSecurityEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32$.grpc_gateway.openapi.SecurityScheme:\x02\x38\x01\"\xb7\x05\n\x0eSecurityScheme\x12\x37\n\x04type\x18\x01 \x01(\x0e\x32).grpc_gateway.openapi.SecurityScheme.Type\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x33\n\x02in\x18\x04 \x01(\x0e\x32\'.grpc_gateway.openapi.SecurityScheme.In\x12\x37\n\x04\x66low\x18\x05 \x01(\x0e\x32).grpc_gateway.openapi.SecurityScheme.Flow\x12\x19\n\x11\x61uthorization_url\x18\x06 \x01(\t\x12\x11\n\ttoken_url\x18\x07 \x01(\t\x12,\n\x06scopes\x18\x08 \x01(\x0b\x32\x1c.grpc_gateway.openapi.Scopes\x12H\n\nextensions\x18\t \x03(\x0b\x32\x34.grpc_gateway.openapi.SecurityScheme.ExtensionsEntry\x1aI\n\x0f\x45xtensionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value:\x02\x38\x01\"K\n\x04Type\x12\x10\n\x0cTYPE_INVALID\x10\x00\x12\x0e\n\nTYPE_BASIC\x10\x01\x12\x10\n\x0cTYPE_API_KEY\x10\x02\x12\x0f\n\x0bTYPE_OAUTH2\x10\x03\"1\n\x02In\x12\x0e\n\nIN_INVALID\x10\x00\x12\x0c\n\x08IN_QUERY\x10\x01\x12\r\n\tIN_HEADER\x10\x02\"j\n\x04\x46low\x12\x10\n\x0c\x46LOW_INVALID\x10\x00\x12\x11\n\rFLOW_IMPLICIT\x10\x01\x12\x11\n\rFLOW_PASSWORD\x10\x02\x12\x14\n\x10\x46LOW_APPLICATION\x10\x03\x12\x14\n\x10\x46LOW_ACCESS_CODE\x10\x04\"\xa2\x02\n\x13SecurityRequirement\x12`\n\x14security_requirement\x18\x01 \x03(\x0b\x32\x42.grpc_gateway.openapi.SecurityRequirement.SecurityRequirementEntry\x1a)\n\x18SecurityRequirementValue\x12\r\n\x05scope\x18\x01 \x03(\t\x1a~\n\x18SecurityRequirementEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12Q\n\x05value\x18\x02 \x01(\x0b\x32\x42.grpc_gateway.openapi.SecurityRequirement.SecurityRequirementValue:\x02\x38\x01\"n\n\x06Scopes\x12\x36\n\x05scope\x18\x01 \x03(\x0b\x32\'.grpc_gateway.openapi.Scopes.ScopeEntry\x1a,\n\nScopeEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01*;\n\x06Scheme\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04HTTP\x10\x01\x12\t\n\x05HTTPS\x10\x02\x12\x06\n\x02WS\x10\x03\x12\x07\n\x03WSS\x10\x04\x42\x18Z\x16ri/_gen/protos/openapib\x06proto3')

_SCHEME = DESCRIPTOR.enum_types_by_name['Scheme']
Scheme = enum_type_wrapper.EnumTypeWrapper(_SCHEME)
UNKNOWN = 0
HTTP = 1
HTTPS = 2
WS = 3
WSS = 4


_SWAGGER = DESCRIPTOR.message_types_by_name['Swagger']
_SWAGGER_RESPONSESENTRY = _SWAGGER.nested_types_by_name['ResponsesEntry']
_SWAGGER_EXTENSIONSENTRY = _SWAGGER.nested_types_by_name['ExtensionsEntry']
_OPERATION = DESCRIPTOR.message_types_by_name['Operation']
_OPERATION_RESPONSESENTRY = _OPERATION.nested_types_by_name['ResponsesEntry']
_OPERATION_EXTENSIONSENTRY = _OPERATION.nested_types_by_name['ExtensionsEntry']
_HEADER = DESCRIPTOR.message_types_by_name['Header']
_RESPONSE = DESCRIPTOR.message_types_by_name['Response']
_RESPONSE_HEADERSENTRY = _RESPONSE.nested_types_by_name['HeadersEntry']
_RESPONSE_EXAMPLESENTRY = _RESPONSE.nested_types_by_name['ExamplesEntry']
_RESPONSE_EXTENSIONSENTRY = _RESPONSE.nested_types_by_name['ExtensionsEntry']
_INFO = DESCRIPTOR.message_types_by_name['Info']
_INFO_EXTENSIONSENTRY = _INFO.nested_types_by_name['ExtensionsEntry']
_CONTACT = DESCRIPTOR.message_types_by_name['Contact']
_LICENSE = DESCRIPTOR.message_types_by_name['License']
_EXTERNALDOCUMENTATION = DESCRIPTOR.message_types_by_name['ExternalDocumentation']
_SCHEMA = DESCRIPTOR.message_types_by_name['Schema']
_JSONSCHEMA = DESCRIPTOR.message_types_by_name['JSONSchema']
_JSONSCHEMA_FIELDCONFIGURATION = _JSONSCHEMA.nested_types_by_name['FieldConfiguration']
_TAG = DESCRIPTOR.message_types_by_name['Tag']
_SECURITYDEFINITIONS = DESCRIPTOR.message_types_by_name['SecurityDefinitions']
_SECURITYDEFINITIONS_SECURITYENTRY = _SECURITYDEFINITIONS.nested_types_by_name['SecurityEntry']
_SECURITYSCHEME = DESCRIPTOR.message_types_by_name['SecurityScheme']
_SECURITYSCHEME_EXTENSIONSENTRY = _SECURITYSCHEME.nested_types_by_name['ExtensionsEntry']
_SECURITYREQUIREMENT = DESCRIPTOR.message_types_by_name['SecurityRequirement']
_SECURITYREQUIREMENT_SECURITYREQUIREMENTVALUE = _SECURITYREQUIREMENT.nested_types_by_name['SecurityRequirementValue']
_SECURITYREQUIREMENT_SECURITYREQUIREMENTENTRY = _SECURITYREQUIREMENT.nested_types_by_name['SecurityRequirementEntry']
_SCOPES = DESCRIPTOR.message_types_by_name['Scopes']
_SCOPES_SCOPEENTRY = _SCOPES.nested_types_by_name['ScopeEntry']
_JSONSCHEMA_JSONSCHEMASIMPLETYPES = _JSONSCHEMA.enum_types_by_name['JSONSchemaSimpleTypes']
_SECURITYSCHEME_TYPE = _SECURITYSCHEME.enum_types_by_name['Type']
_SECURITYSCHEME_IN = _SECURITYSCHEME.enum_types_by_name['In']
_SECURITYSCHEME_FLOW = _SECURITYSCHEME.enum_types_by_name['Flow']
Swagger = _reflection.GeneratedProtocolMessageType('Swagger', (_message.Message,), {

  'ResponsesEntry' : _reflection.GeneratedProtocolMessageType('ResponsesEntry', (_message.Message,), {
    'DESCRIPTOR' : _SWAGGER_RESPONSESENTRY,
    '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
    # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.Swagger.ResponsesEntry)
    })
  ,

  'ExtensionsEntry' : _reflection.GeneratedProtocolMessageType('ExtensionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SWAGGER_EXTENSIONSENTRY,
    '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
    # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.Swagger.ExtensionsEntry)
    })
  ,
  'DESCRIPTOR' : _SWAGGER,
  '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
  # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.Swagger)
  })
_sym_db.RegisterMessage(Swagger)
_sym_db.RegisterMessage(Swagger.ResponsesEntry)
_sym_db.RegisterMessage(Swagger.ExtensionsEntry)

Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), {

  'ResponsesEntry' : _reflection.GeneratedProtocolMessageType('ResponsesEntry', (_message.Message,), {
    'DESCRIPTOR' : _OPERATION_RESPONSESENTRY,
    '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
    # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.Operation.ResponsesEntry)
    })
  ,

  'ExtensionsEntry' : _reflection.GeneratedProtocolMessageType('ExtensionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _OPERATION_EXTENSIONSENTRY,
    '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
    # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.Operation.ExtensionsEntry)
    })
  ,
  'DESCRIPTOR' : _OPERATION,
  '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
  # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.Operation)
  })
_sym_db.RegisterMessage(Operation)
_sym_db.RegisterMessage(Operation.ResponsesEntry)
_sym_db.RegisterMessage(Operation.ExtensionsEntry)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
  'DESCRIPTOR' : _HEADER,
  '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
  # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.Header)
  })
_sym_db.RegisterMessage(Header)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {

  'HeadersEntry' : _reflection.GeneratedProtocolMessageType('HeadersEntry', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSE_HEADERSENTRY,
    '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
    # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.Response.HeadersEntry)
    })
  ,

  'ExamplesEntry' : _reflection.GeneratedProtocolMessageType('ExamplesEntry', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSE_EXAMPLESENTRY,
    '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
    # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.Response.ExamplesEntry)
    })
  ,

  'ExtensionsEntry' : _reflection.GeneratedProtocolMessageType('ExtensionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSE_EXTENSIONSENTRY,
    '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
    # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.Response.ExtensionsEntry)
    })
  ,
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
  # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.Response)
  })
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.HeadersEntry)
_sym_db.RegisterMessage(Response.ExamplesEntry)
_sym_db.RegisterMessage(Response.ExtensionsEntry)

Info = _reflection.GeneratedProtocolMessageType('Info', (_message.Message,), {

  'ExtensionsEntry' : _reflection.GeneratedProtocolMessageType('ExtensionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _INFO_EXTENSIONSENTRY,
    '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
    # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.Info.ExtensionsEntry)
    })
  ,
  'DESCRIPTOR' : _INFO,
  '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
  # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.Info)
  })
_sym_db.RegisterMessage(Info)
_sym_db.RegisterMessage(Info.ExtensionsEntry)

Contact = _reflection.GeneratedProtocolMessageType('Contact', (_message.Message,), {
  'DESCRIPTOR' : _CONTACT,
  '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
  # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.Contact)
  })
_sym_db.RegisterMessage(Contact)

License = _reflection.GeneratedProtocolMessageType('License', (_message.Message,), {
  'DESCRIPTOR' : _LICENSE,
  '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
  # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.License)
  })
_sym_db.RegisterMessage(License)

ExternalDocumentation = _reflection.GeneratedProtocolMessageType('ExternalDocumentation', (_message.Message,), {
  'DESCRIPTOR' : _EXTERNALDOCUMENTATION,
  '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
  # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.ExternalDocumentation)
  })
_sym_db.RegisterMessage(ExternalDocumentation)

Schema = _reflection.GeneratedProtocolMessageType('Schema', (_message.Message,), {
  'DESCRIPTOR' : _SCHEMA,
  '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
  # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.Schema)
  })
_sym_db.RegisterMessage(Schema)

JSONSchema = _reflection.GeneratedProtocolMessageType('JSONSchema', (_message.Message,), {

  'FieldConfiguration' : _reflection.GeneratedProtocolMessageType('FieldConfiguration', (_message.Message,), {
    'DESCRIPTOR' : _JSONSCHEMA_FIELDCONFIGURATION,
    '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
    # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.JSONSchema.FieldConfiguration)
    })
  ,
  'DESCRIPTOR' : _JSONSCHEMA,
  '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
  # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.JSONSchema)
  })
_sym_db.RegisterMessage(JSONSchema)
_sym_db.RegisterMessage(JSONSchema.FieldConfiguration)

Tag = _reflection.GeneratedProtocolMessageType('Tag', (_message.Message,), {
  'DESCRIPTOR' : _TAG,
  '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
  # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.Tag)
  })
_sym_db.RegisterMessage(Tag)

SecurityDefinitions = _reflection.GeneratedProtocolMessageType('SecurityDefinitions', (_message.Message,), {

  'SecurityEntry' : _reflection.GeneratedProtocolMessageType('SecurityEntry', (_message.Message,), {
    'DESCRIPTOR' : _SECURITYDEFINITIONS_SECURITYENTRY,
    '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
    # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.SecurityDefinitions.SecurityEntry)
    })
  ,
  'DESCRIPTOR' : _SECURITYDEFINITIONS,
  '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
  # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.SecurityDefinitions)
  })
_sym_db.RegisterMessage(SecurityDefinitions)
_sym_db.RegisterMessage(SecurityDefinitions.SecurityEntry)

SecurityScheme = _reflection.GeneratedProtocolMessageType('SecurityScheme', (_message.Message,), {

  'ExtensionsEntry' : _reflection.GeneratedProtocolMessageType('ExtensionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SECURITYSCHEME_EXTENSIONSENTRY,
    '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
    # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.SecurityScheme.ExtensionsEntry)
    })
  ,
  'DESCRIPTOR' : _SECURITYSCHEME,
  '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
  # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.SecurityScheme)
  })
_sym_db.RegisterMessage(SecurityScheme)
_sym_db.RegisterMessage(SecurityScheme.ExtensionsEntry)

SecurityRequirement = _reflection.GeneratedProtocolMessageType('SecurityRequirement', (_message.Message,), {

  'SecurityRequirementValue' : _reflection.GeneratedProtocolMessageType('SecurityRequirementValue', (_message.Message,), {
    'DESCRIPTOR' : _SECURITYREQUIREMENT_SECURITYREQUIREMENTVALUE,
    '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
    # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.SecurityRequirement.SecurityRequirementValue)
    })
  ,

  'SecurityRequirementEntry' : _reflection.GeneratedProtocolMessageType('SecurityRequirementEntry', (_message.Message,), {
    'DESCRIPTOR' : _SECURITYREQUIREMENT_SECURITYREQUIREMENTENTRY,
    '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
    # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.SecurityRequirement.SecurityRequirementEntry)
    })
  ,
  'DESCRIPTOR' : _SECURITYREQUIREMENT,
  '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
  # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.SecurityRequirement)
  })
_sym_db.RegisterMessage(SecurityRequirement)
_sym_db.RegisterMessage(SecurityRequirement.SecurityRequirementValue)
_sym_db.RegisterMessage(SecurityRequirement.SecurityRequirementEntry)

Scopes = _reflection.GeneratedProtocolMessageType('Scopes', (_message.Message,), {

  'ScopeEntry' : _reflection.GeneratedProtocolMessageType('ScopeEntry', (_message.Message,), {
    'DESCRIPTOR' : _SCOPES_SCOPEENTRY,
    '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
    # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.Scopes.ScopeEntry)
    })
  ,
  'DESCRIPTOR' : _SCOPES,
  '__module__' : 'protos.grpc_gateway.openapi.openapiv2_pb2'
  # @@protoc_insertion_point(class_scope:grpc_gateway.openapi.Scopes)
  })
_sym_db.RegisterMessage(Scopes)
_sym_db.RegisterMessage(Scopes.ScopeEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\026ri/_gen/protos/openapi'
  _SWAGGER_RESPONSESENTRY._options = None
  _SWAGGER_RESPONSESENTRY._serialized_options = b'8\001'
  _SWAGGER_EXTENSIONSENTRY._options = None
  _SWAGGER_EXTENSIONSENTRY._serialized_options = b'8\001'
  _OPERATION_RESPONSESENTRY._options = None
  _OPERATION_RESPONSESENTRY._serialized_options = b'8\001'
  _OPERATION_EXTENSIONSENTRY._options = None
  _OPERATION_EXTENSIONSENTRY._serialized_options = b'8\001'
  _RESPONSE_HEADERSENTRY._options = None
  _RESPONSE_HEADERSENTRY._serialized_options = b'8\001'
  _RESPONSE_EXAMPLESENTRY._options = None
  _RESPONSE_EXAMPLESENTRY._serialized_options = b'8\001'
  _RESPONSE_EXTENSIONSENTRY._options = None
  _RESPONSE_EXTENSIONSENTRY._serialized_options = b'8\001'
  _INFO_EXTENSIONSENTRY._options = None
  _INFO_EXTENSIONSENTRY._serialized_options = b'8\001'
  _SECURITYDEFINITIONS_SECURITYENTRY._options = None
  _SECURITYDEFINITIONS_SECURITYENTRY._serialized_options = b'8\001'
  _SECURITYSCHEME_EXTENSIONSENTRY._options = None
  _SECURITYSCHEME_EXTENSIONSENTRY._serialized_options = b'8\001'
  _SECURITYREQUIREMENT_SECURITYREQUIREMENTENTRY._options = None
  _SECURITYREQUIREMENT_SECURITYREQUIREMENTENTRY._serialized_options = b'8\001'
  _SCOPES_SCOPEENTRY._options = None
  _SCOPES_SCOPEENTRY._serialized_options = b'8\001'
  _SCHEME._serialized_start=4980
  _SCHEME._serialized_end=5039
  _SWAGGER._serialized_start=100
  _SWAGGER._serialized_end=793
  _SWAGGER_RESPONSESENTRY._serialized_start=620
  _SWAGGER_RESPONSESENTRY._serialized_end=700
  _SWAGGER_EXTENSIONSENTRY._serialized_start=702
  _SWAGGER_EXTENSIONSENTRY._serialized_end=775
  _OPERATION._serialized_start=796
  _OPERATION._serialized_end=1412
  _OPERATION_RESPONSESENTRY._serialized_start=620
  _OPERATION_RESPONSESENTRY._serialized_end=700
  _OPERATION_EXTENSIONSENTRY._serialized_start=702
  _OPERATION_EXTENSIONSENTRY._serialized_end=775
  _HEADER._serialized_start=1415
  _HEADER._serialized_end=1586
  _RESPONSE._serialized_start=1589
  _RESPONSE._serialized_end=2062
  _RESPONSE_HEADERSENTRY._serialized_start=1862
  _RESPONSE_HEADERSENTRY._serialized_end=1938
  _RESPONSE_EXAMPLESENTRY._serialized_start=1940
  _RESPONSE_EXAMPLESENTRY._serialized_end=1987
  _RESPONSE_EXTENSIONSENTRY._serialized_start=702
  _RESPONSE_EXTENSIONSENTRY._serialized_end=775
  _INFO._serialized_start=2065
  _INFO._serialized_end=2385
  _INFO_EXTENSIONSENTRY._serialized_start=702
  _INFO_EXTENSIONSENTRY._serialized_end=775
  _CONTACT._serialized_start=2387
  _CONTACT._serialized_end=2438
  _LICENSE._serialized_start=2440
  _LICENSE._serialized_end=2476
  _EXTERNALDOCUMENTATION._serialized_start=2478
  _EXTERNALDOCUMENTATION._serialized_end=2535
  _SCHEMA._serialized_start=2538
  _SCHEMA._serialized_end=2734
  _JSONSCHEMA._serialized_start=2737
  _JSONSCHEMA._serialized_end=3587
  _JSONSCHEMA_FIELDCONFIGURATION._serialized_start=3343
  _JSONSCHEMA_FIELDCONFIGURATION._serialized_end=3388
  _JSONSCHEMA_JSONSCHEMASIMPLETYPES._serialized_start=3390
  _JSONSCHEMA_JSONSCHEMASIMPLETYPES._serialized_end=3509
  _TAG._serialized_start=3589
  _TAG._serialized_end=3689
  _SECURITYDEFINITIONS._serialized_start=3692
  _SECURITYDEFINITIONS._serialized_end=3875
  _SECURITYDEFINITIONS_SECURITYENTRY._serialized_start=3790
  _SECURITYDEFINITIONS_SECURITYENTRY._serialized_end=3875
  _SECURITYSCHEME._serialized_start=3878
  _SECURITYSCHEME._serialized_end=4573
  _SECURITYSCHEME_EXTENSIONSENTRY._serialized_start=702
  _SECURITYSCHEME_EXTENSIONSENTRY._serialized_end=775
  _SECURITYSCHEME_TYPE._serialized_start=4339
  _SECURITYSCHEME_TYPE._serialized_end=4414
  _SECURITYSCHEME_IN._serialized_start=4416
  _SECURITYSCHEME_IN._serialized_end=4465
  _SECURITYSCHEME_FLOW._serialized_start=4467
  _SECURITYSCHEME_FLOW._serialized_end=4573
  _SECURITYREQUIREMENT._serialized_start=4576
  _SECURITYREQUIREMENT._serialized_end=4866
  _SECURITYREQUIREMENT_SECURITYREQUIREMENTVALUE._serialized_start=4697
  _SECURITYREQUIREMENT_SECURITYREQUIREMENTVALUE._serialized_end=4738
  _SECURITYREQUIREMENT_SECURITYREQUIREMENTENTRY._serialized_start=4740
  _SECURITYREQUIREMENT_SECURITYREQUIREMENTENTRY._serialized_end=4866
  _SCOPES._serialized_start=4868
  _SCOPES._serialized_end=4978
  _SCOPES_SCOPEENTRY._serialized_start=4934
  _SCOPES_SCOPEENTRY._serialized_end=4978
# @@protoc_insertion_point(module_scope)
