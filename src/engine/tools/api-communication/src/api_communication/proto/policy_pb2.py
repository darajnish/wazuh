# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: policy.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import api_communication.proto.engine_pb2 as _engine_pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cpolicy.proto\x12\x1b\x63om.wazuh.api.engine.policy\x1a\x0c\x65ngine.proto\"3\n\x11StorePost_Request\x12\x13\n\x06policy\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_policy\"5\n\x13StoreDelete_Request\x12\x13\n\x06policy\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_policy\"F\n\x10StoreGet_Request\x12\x13\n\x06policy\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\nnamespaces\x18\x02 \x03(\tB\t\n\x07_policy\"\x81\x01\n\x11StoreGet_Response\x12\x32\n\x06status\x18\x01 \x01(\x0e\x32\".com.wazuh.api.engine.ReturnStatus\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x11\n\x04\x64\x61ta\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_errorB\x07\n\x05_data\"w\n\x11\x41ssetPost_Request\x12\x13\n\x06policy\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05\x61sset\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x16\n\tnamespace\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\t\n\x07_policyB\x08\n\x06_assetB\x0c\n\n_namespace\"y\n\x13\x41ssetDelete_Request\x12\x13\n\x06policy\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05\x61sset\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x16\n\tnamespace\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\t\n\x07_policyB\x08\n\x06_assetB\x0c\n\n_namespace\"X\n\x10\x41ssetGet_Request\x12\x13\n\x06policy\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tnamespace\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\t\n\x07_policyB\x0c\n\n_namespace\"s\n\x11\x41ssetGet_Response\x12\x32\n\x06status\x18\x01 \x01(\x0e\x32\".com.wazuh.api.engine.ReturnStatus\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x0c\n\x04\x64\x61ta\x18\x03 \x03(\tB\x08\n\x06_error\"`\n\x18\x44\x65\x66\x61ultParentGet_Request\x12\x13\n\x06policy\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tnamespace\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\t\n\x07_policyB\x0c\n\n_namespace\"{\n\x19\x44\x65\x66\x61ultParentGet_Response\x12\x32\n\x06status\x18\x01 \x01(\x0e\x32\".com.wazuh.api.engine.ReturnStatus\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x0c\n\x04\x64\x61ta\x18\x03 \x03(\tB\x08\n\x06_error\"\x81\x01\n\x19\x44\x65\x66\x61ultParentPost_Request\x12\x13\n\x06policy\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tnamespace\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x06parent\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\t\n\x07_policyB\x0c\n\n_namespaceB\t\n\x07_parent\"\x83\x01\n\x1b\x44\x65\x66\x61ultParentDelete_Request\x12\x13\n\x06policy\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tnamespace\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x06parent\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\t\n\x07_policyB\x0c\n\n_namespaceB\t\n\x07_parent\"\x15\n\x13PoliciesGet_Request\"v\n\x14PoliciesGet_Response\x12\x32\n\x06status\x18\x01 \x01(\x0e\x32\".com.wazuh.api.engine.ReturnStatus\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x0c\n\x04\x64\x61ta\x18\x03 \x03(\tB\x08\n\x06_error\"7\n\x15NamespacesGet_Request\x12\x13\n\x06policy\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_policy\"x\n\x16NamespacesGet_Response\x12\x32\n\x06status\x18\x01 \x01(\x0e\x32\".com.wazuh.api.engine.ReturnStatus\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x0c\n\x04\x64\x61ta\x18\x03 \x03(\tB\x08\n\x06_errorb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'policy_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STOREPOST_REQUEST._serialized_start=59
  _STOREPOST_REQUEST._serialized_end=110
  _STOREDELETE_REQUEST._serialized_start=112
  _STOREDELETE_REQUEST._serialized_end=165
  _STOREGET_REQUEST._serialized_start=167
  _STOREGET_REQUEST._serialized_end=237
  _STOREGET_RESPONSE._serialized_start=240
  _STOREGET_RESPONSE._serialized_end=369
  _ASSETPOST_REQUEST._serialized_start=371
  _ASSETPOST_REQUEST._serialized_end=490
  _ASSETDELETE_REQUEST._serialized_start=492
  _ASSETDELETE_REQUEST._serialized_end=613
  _ASSETGET_REQUEST._serialized_start=615
  _ASSETGET_REQUEST._serialized_end=703
  _ASSETGET_RESPONSE._serialized_start=705
  _ASSETGET_RESPONSE._serialized_end=820
  _DEFAULTPARENTGET_REQUEST._serialized_start=822
  _DEFAULTPARENTGET_REQUEST._serialized_end=918
  _DEFAULTPARENTGET_RESPONSE._serialized_start=920
  _DEFAULTPARENTGET_RESPONSE._serialized_end=1043
  _DEFAULTPARENTPOST_REQUEST._serialized_start=1046
  _DEFAULTPARENTPOST_REQUEST._serialized_end=1175
  _DEFAULTPARENTDELETE_REQUEST._serialized_start=1178
  _DEFAULTPARENTDELETE_REQUEST._serialized_end=1309
  _POLICIESGET_REQUEST._serialized_start=1311
  _POLICIESGET_REQUEST._serialized_end=1332
  _POLICIESGET_RESPONSE._serialized_start=1334
  _POLICIESGET_RESPONSE._serialized_end=1452
  _NAMESPACESGET_REQUEST._serialized_start=1454
  _NAMESPACESGET_REQUEST._serialized_end=1509
  _NAMESPACESGET_RESPONSE._serialized_start=1511
  _NAMESPACESGET_RESPONSE._serialized_end=1631
# @@protoc_insertion_point(module_scope)
