# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/type/postal_address.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n google/type/postal_address.proto\x12\x0bgoogle.type\"\xfd\x01\n\rPostalAddress\x12\x10\n\x08revision\x18\x01 \x01(\x05\x12\x13\n\x0bregion_code\x18\x02 \x01(\t\x12\x15\n\rlanguage_code\x18\x03 \x01(\t\x12\x13\n\x0bpostal_code\x18\x04 \x01(\t\x12\x14\n\x0csorting_code\x18\x05 \x01(\t\x12\x1b\n\x13\x61\x64ministrative_area\x18\x06 \x01(\t\x12\x10\n\x08locality\x18\x07 \x01(\t\x12\x13\n\x0bsublocality\x18\x08 \x01(\t\x12\x15\n\raddress_lines\x18\t \x03(\t\x12\x12\n\nrecipients\x18\n \x03(\t\x12\x14\n\x0corganization\x18\x0b \x01(\tBx\n\x0f\x63om.google.typeB\x12PostalAddressProtoP\x01ZFgoogle.golang.org/genproto/googleapis/type/postaladdress;postaladdress\xf8\x01\x01\xa2\x02\x03GTPb\x06proto3')



_POSTALADDRESS = DESCRIPTOR.message_types_by_name['PostalAddress']
PostalAddress = _reflection.GeneratedProtocolMessageType('PostalAddress', (_message.Message,), {
  'DESCRIPTOR' : _POSTALADDRESS,
  '__module__' : 'google.type.postal_address_pb2'
  # @@protoc_insertion_point(class_scope:google.type.PostalAddress)
  })
_sym_db.RegisterMessage(PostalAddress)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017com.google.typeB\022PostalAddressProtoP\001ZFgoogle.golang.org/genproto/googleapis/type/postaladdress;postaladdress\370\001\001\242\002\003GTP'
  _POSTALADDRESS._serialized_start=50
  _POSTALADDRESS._serialized_end=303
# @@protoc_insertion_point(module_scope)
