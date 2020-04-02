# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: computational_resource_description.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='computational_resource_description.proto',
  package='sgci.computeresourcedescription',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n(computational_resource_description.proto\x12\x1fsgci.computeresourcedescription\"\xa0\x08\n\x1a\x43omputeResourceDescription\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12O\n\x05hosts\x18\x04 \x03(\x0b\x32@.sgci.computeresourcedescription.ComputeResourceDescription.Host\x12[\n\x0b\x63onnections\x18\x05 \x03(\x0b\x32\x46.sgci.computeresourcedescription.ComputeResourceDescription.Connection\x12V\n\x04type\x18\x06 \x01(\x0e\x32H.sgci.computeresourcedescription.ComputeResourceDescription.ResourceType\x12i\n\x12storage_attributes\x18\x07 \x01(\x0b\x32M.sgci.computeresourcedescription.ComputeResourceDescription.StorageAttributes\x1a\x36\n\x04Host\x12\x10\n\x08hostname\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x10\n\x08priority\x18\x03 \x01(\x05\x1a\x80\x01\n\nConnection\x12\x0c\n\x04port\x18\x01 \x01(\x05\x12\x1c\n\x14\x63onnection_protocols\x18\x02 \x03(\t\x12\x1a\n\x12security_protocols\x18\x03 \x03(\t\x12\x16\n\x0eproxy_hostname\x18\x04 \x01(\t\x12\x12\n\nproxy_port\x18\x05 \x01(\x05\x1a\xea\x02\n\x11StorageAttributes\x12Z\n\nconnection\x18\x01 \x01(\x0b\x32\x46.sgci.computeresourcedescription.ComputeResourceDescription.Connection\x12n\n\x0b\x66ilesystems\x18\x02 \x01(\x0b\x32Y.sgci.computeresourcedescription.ComputeResourceDescription.StorageAttributes.FileSystems\x12\x14\n\x0cstorage_type\x18\x03 \x01(\t\x1as\n\x0b\x46ileSystems\x12\x16\n\x0ehome_directory\x18\x01 \x01(\t\x12\x19\n\x11scratch_directory\x18\x02 \x01(\t\x12\x16\n\x0ework_directory\x18\x03 \x01(\t\x12\x19\n\x11\x61rchive_directory\x18\x04 \x01(\t\":\n\x0cResourceType\x12\x14\n\x10\x43OMPUTE_RESOURCE\x10\x00\x12\x14\n\x10STORAGE_RESOURCE\x10\x01\x62\x06proto3'
)



_COMPUTERESOURCEDESCRIPTION_RESOURCETYPE = _descriptor.EnumDescriptor(
  name='ResourceType',
  full_name='sgci.computeresourcedescription.ComputeResourceDescription.ResourceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COMPUTE_RESOURCE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STORAGE_RESOURCE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1076,
  serialized_end=1134,
)
_sym_db.RegisterEnumDescriptor(_COMPUTERESOURCEDESCRIPTION_RESOURCETYPE)


_COMPUTERESOURCEDESCRIPTION_HOST = _descriptor.Descriptor(
  name='Host',
  full_name='sgci.computeresourcedescription.ComputeResourceDescription.Host',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hostname', full_name='sgci.computeresourcedescription.ComputeResourceDescription.Host.hostname', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='sgci.computeresourcedescription.ComputeResourceDescription.Host.ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='priority', full_name='sgci.computeresourcedescription.ComputeResourceDescription.Host.priority', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=524,
  serialized_end=578,
)

_COMPUTERESOURCEDESCRIPTION_CONNECTION = _descriptor.Descriptor(
  name='Connection',
  full_name='sgci.computeresourcedescription.ComputeResourceDescription.Connection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='port', full_name='sgci.computeresourcedescription.ComputeResourceDescription.Connection.port', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connection_protocols', full_name='sgci.computeresourcedescription.ComputeResourceDescription.Connection.connection_protocols', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='security_protocols', full_name='sgci.computeresourcedescription.ComputeResourceDescription.Connection.security_protocols', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proxy_hostname', full_name='sgci.computeresourcedescription.ComputeResourceDescription.Connection.proxy_hostname', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proxy_port', full_name='sgci.computeresourcedescription.ComputeResourceDescription.Connection.proxy_port', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=581,
  serialized_end=709,
)

_COMPUTERESOURCEDESCRIPTION_STORAGEATTRIBUTES_FILESYSTEMS = _descriptor.Descriptor(
  name='FileSystems',
  full_name='sgci.computeresourcedescription.ComputeResourceDescription.StorageAttributes.FileSystems',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='home_directory', full_name='sgci.computeresourcedescription.ComputeResourceDescription.StorageAttributes.FileSystems.home_directory', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scratch_directory', full_name='sgci.computeresourcedescription.ComputeResourceDescription.StorageAttributes.FileSystems.scratch_directory', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='work_directory', full_name='sgci.computeresourcedescription.ComputeResourceDescription.StorageAttributes.FileSystems.work_directory', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='archive_directory', full_name='sgci.computeresourcedescription.ComputeResourceDescription.StorageAttributes.FileSystems.archive_directory', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=959,
  serialized_end=1074,
)

_COMPUTERESOURCEDESCRIPTION_STORAGEATTRIBUTES = _descriptor.Descriptor(
  name='StorageAttributes',
  full_name='sgci.computeresourcedescription.ComputeResourceDescription.StorageAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connection', full_name='sgci.computeresourcedescription.ComputeResourceDescription.StorageAttributes.connection', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filesystems', full_name='sgci.computeresourcedescription.ComputeResourceDescription.StorageAttributes.filesystems', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='storage_type', full_name='sgci.computeresourcedescription.ComputeResourceDescription.StorageAttributes.storage_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COMPUTERESOURCEDESCRIPTION_STORAGEATTRIBUTES_FILESYSTEMS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=712,
  serialized_end=1074,
)

_COMPUTERESOURCEDESCRIPTION = _descriptor.Descriptor(
  name='ComputeResourceDescription',
  full_name='sgci.computeresourcedescription.ComputeResourceDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='sgci.computeresourcedescription.ComputeResourceDescription.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='sgci.computeresourcedescription.ComputeResourceDescription.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='sgci.computeresourcedescription.ComputeResourceDescription.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hosts', full_name='sgci.computeresourcedescription.ComputeResourceDescription.hosts', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connections', full_name='sgci.computeresourcedescription.ComputeResourceDescription.connections', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='sgci.computeresourcedescription.ComputeResourceDescription.type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='storage_attributes', full_name='sgci.computeresourcedescription.ComputeResourceDescription.storage_attributes', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COMPUTERESOURCEDESCRIPTION_HOST, _COMPUTERESOURCEDESCRIPTION_CONNECTION, _COMPUTERESOURCEDESCRIPTION_STORAGEATTRIBUTES, ],
  enum_types=[
    _COMPUTERESOURCEDESCRIPTION_RESOURCETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=1134,
)

_COMPUTERESOURCEDESCRIPTION_HOST.containing_type = _COMPUTERESOURCEDESCRIPTION
_COMPUTERESOURCEDESCRIPTION_CONNECTION.containing_type = _COMPUTERESOURCEDESCRIPTION
_COMPUTERESOURCEDESCRIPTION_STORAGEATTRIBUTES_FILESYSTEMS.containing_type = _COMPUTERESOURCEDESCRIPTION_STORAGEATTRIBUTES
_COMPUTERESOURCEDESCRIPTION_STORAGEATTRIBUTES.fields_by_name['connection'].message_type = _COMPUTERESOURCEDESCRIPTION_CONNECTION
_COMPUTERESOURCEDESCRIPTION_STORAGEATTRIBUTES.fields_by_name['filesystems'].message_type = _COMPUTERESOURCEDESCRIPTION_STORAGEATTRIBUTES_FILESYSTEMS
_COMPUTERESOURCEDESCRIPTION_STORAGEATTRIBUTES.containing_type = _COMPUTERESOURCEDESCRIPTION
_COMPUTERESOURCEDESCRIPTION.fields_by_name['hosts'].message_type = _COMPUTERESOURCEDESCRIPTION_HOST
_COMPUTERESOURCEDESCRIPTION.fields_by_name['connections'].message_type = _COMPUTERESOURCEDESCRIPTION_CONNECTION
_COMPUTERESOURCEDESCRIPTION.fields_by_name['type'].enum_type = _COMPUTERESOURCEDESCRIPTION_RESOURCETYPE
_COMPUTERESOURCEDESCRIPTION.fields_by_name['storage_attributes'].message_type = _COMPUTERESOURCEDESCRIPTION_STORAGEATTRIBUTES
_COMPUTERESOURCEDESCRIPTION_RESOURCETYPE.containing_type = _COMPUTERESOURCEDESCRIPTION
DESCRIPTOR.message_types_by_name['ComputeResourceDescription'] = _COMPUTERESOURCEDESCRIPTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ComputeResourceDescription = _reflection.GeneratedProtocolMessageType('ComputeResourceDescription', (_message.Message,), {

  'Host' : _reflection.GeneratedProtocolMessageType('Host', (_message.Message,), {
    'DESCRIPTOR' : _COMPUTERESOURCEDESCRIPTION_HOST,
    '__module__' : 'computational_resource_description_pb2'
    # @@protoc_insertion_point(class_scope:sgci.computeresourcedescription.ComputeResourceDescription.Host)
    })
  ,

  'Connection' : _reflection.GeneratedProtocolMessageType('Connection', (_message.Message,), {
    'DESCRIPTOR' : _COMPUTERESOURCEDESCRIPTION_CONNECTION,
    '__module__' : 'computational_resource_description_pb2'
    # @@protoc_insertion_point(class_scope:sgci.computeresourcedescription.ComputeResourceDescription.Connection)
    })
  ,

  'StorageAttributes' : _reflection.GeneratedProtocolMessageType('StorageAttributes', (_message.Message,), {

    'FileSystems' : _reflection.GeneratedProtocolMessageType('FileSystems', (_message.Message,), {
      'DESCRIPTOR' : _COMPUTERESOURCEDESCRIPTION_STORAGEATTRIBUTES_FILESYSTEMS,
      '__module__' : 'computational_resource_description_pb2'
      # @@protoc_insertion_point(class_scope:sgci.computeresourcedescription.ComputeResourceDescription.StorageAttributes.FileSystems)
      })
    ,
    'DESCRIPTOR' : _COMPUTERESOURCEDESCRIPTION_STORAGEATTRIBUTES,
    '__module__' : 'computational_resource_description_pb2'
    # @@protoc_insertion_point(class_scope:sgci.computeresourcedescription.ComputeResourceDescription.StorageAttributes)
    })
  ,
  'DESCRIPTOR' : _COMPUTERESOURCEDESCRIPTION,
  '__module__' : 'computational_resource_description_pb2'
  # @@protoc_insertion_point(class_scope:sgci.computeresourcedescription.ComputeResourceDescription)
  })
_sym_db.RegisterMessage(ComputeResourceDescription)
_sym_db.RegisterMessage(ComputeResourceDescription.Host)
_sym_db.RegisterMessage(ComputeResourceDescription.Connection)
_sym_db.RegisterMessage(ComputeResourceDescription.StorageAttributes)
_sym_db.RegisterMessage(ComputeResourceDescription.StorageAttributes.FileSystems)


# @@protoc_insertion_point(module_scope)
