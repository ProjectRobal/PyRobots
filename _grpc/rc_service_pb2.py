# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rc_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10rc_service.proto\"\x07\n\x05_None\")\n\x05Motor\x12\x11\n\tdirection\x18\x01 \x01(\r\x12\r\n\x05speed\x18\x02 \x01(\r\"\"\n\x0e\x44istanceSensor\x12\x10\n\x08\x64istance\x18\x01 \x01(\x01\"]\n\tGyroscope\x12\x14\n\x0c\x61\x63\x63\x65leration\x18\x03 \x03(\x01\x12\x11\n\tgyroscope\x18\x06 \x03(\x01\x12\x13\n\x0b\x61\x63\x63\x65l_range\x18\x07 \x03(\x01\x12\x12\n\ngyro_range\x18\x08 \x03(\x01\"\x16\n\x05Servo\x12\r\n\x05\x61ngle\x18\x01 \x01(\r\"\x1c\n\nAudioChunk\x12\x0e\n\x04\x64\x61ta\x18\xc4\xd8\x02 \x03(\r\"]\n\x07\x43ommand\x12\x12\n\x02mA\x18\x01 \x01(\x0b\x32\x06.Motor\x12\x12\n\x02mB\x18\x02 \x01(\x0b\x32\x06.Motor\x12\x14\n\x04\x65\x61r1\x18\x03 \x01(\x0b\x32\x06.Servo\x12\x14\n\x04\x65\x61r2\x18\x04 \x01(\x0b\x32\x06.Servo\"\xc0\x01\n\x07Message\x12\x1e\n\x05\x66ront\x18\x01 \x01(\x0b\x32\x0f.DistanceSensor\x12\x1e\n\x05\x66loor\x18\x02 \x01(\x0b\x32\x0f.DistanceSensor\x12\x1d\n\tgyroscope\x18\x03 \x01(\x0b\x32\n.Gyroscope\x12\x19\n\x04left\x18\x04 \x01(\x0b\x32\x0b.AudioChunk\x12\x1a\n\x05right\x18\x05 \x01(\x0b\x32\x0b.AudioChunk\x12\x0e\n\x06status\x18\x06 \x01(\x05\x12\x0f\n\x07message\x18\x07 \x01(\t2M\n\x07RCRobot\x12\x1f\n\x07Process\x12\x08.Command\x1a\x08.Message\"\x00\x12!\n\x0bSendCommand\x12\x08.Command\x1a\x06._None\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'rc_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  __NONE._serialized_start=20
  __NONE._serialized_end=27
  _MOTOR._serialized_start=29
  _MOTOR._serialized_end=70
  _DISTANCESENSOR._serialized_start=72
  _DISTANCESENSOR._serialized_end=106
  _GYROSCOPE._serialized_start=108
  _GYROSCOPE._serialized_end=201
  _SERVO._serialized_start=203
  _SERVO._serialized_end=225
  _AUDIOCHUNK._serialized_start=227
  _AUDIOCHUNK._serialized_end=255
  _COMMAND._serialized_start=257
  _COMMAND._serialized_end=350
  _MESSAGE._serialized_start=353
  _MESSAGE._serialized_end=545
  _RCROBOT._serialized_start=547
  _RCROBOT._serialized_end=624
# @@protoc_insertion_point(module_scope)
