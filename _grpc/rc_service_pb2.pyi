from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class _None(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Motor(_message.Message):
    __slots__ = ["direction", "speed"]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    direction: int
    speed: int
    def __init__(self, direction: _Optional[int] = ..., speed: _Optional[int] = ...) -> None: ...

class DistanceSensor(_message.Message):
    __slots__ = ["distance"]
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    distance: float
    def __init__(self, distance: _Optional[float] = ...) -> None: ...

class Gyroscope(_message.Message):
    __slots__ = ["acceleration", "gyroscope", "accel_range", "gyro_range"]
    ACCELERATION_FIELD_NUMBER: _ClassVar[int]
    GYROSCOPE_FIELD_NUMBER: _ClassVar[int]
    ACCEL_RANGE_FIELD_NUMBER: _ClassVar[int]
    GYRO_RANGE_FIELD_NUMBER: _ClassVar[int]
    acceleration: _containers.RepeatedScalarFieldContainer[float]
    gyroscope: _containers.RepeatedScalarFieldContainer[float]
    accel_range: int
    gyro_range: int
    def __init__(self, acceleration: _Optional[_Iterable[float]] = ..., gyroscope: _Optional[_Iterable[float]] = ..., accel_range: _Optional[int] = ..., gyro_range: _Optional[int] = ...) -> None: ...

class Servo(_message.Message):
    __slots__ = ["angle"]
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    angle: int
    def __init__(self, angle: _Optional[int] = ...) -> None: ...

class AudioChunk(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, data: _Optional[_Iterable[int]] = ...) -> None: ...

class Command(_message.Message):
    __slots__ = ["mA", "mB", "ear1", "ear2"]
    MA_FIELD_NUMBER: _ClassVar[int]
    MB_FIELD_NUMBER: _ClassVar[int]
    EAR1_FIELD_NUMBER: _ClassVar[int]
    EAR2_FIELD_NUMBER: _ClassVar[int]
    mA: Motor
    mB: Motor
    ear1: Servo
    ear2: Servo
    def __init__(self, mA: _Optional[_Union[Motor, _Mapping]] = ..., mB: _Optional[_Union[Motor, _Mapping]] = ..., ear1: _Optional[_Union[Servo, _Mapping]] = ..., ear2: _Optional[_Union[Servo, _Mapping]] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ["front", "front1", "floor", "gyroscope", "left", "right", "status", "message"]
    FRONT_FIELD_NUMBER: _ClassVar[int]
    FRONT1_FIELD_NUMBER: _ClassVar[int]
    FLOOR_FIELD_NUMBER: _ClassVar[int]
    GYROSCOPE_FIELD_NUMBER: _ClassVar[int]
    LEFT_FIELD_NUMBER: _ClassVar[int]
    RIGHT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    front: DistanceSensor
    front1: DistanceSensor
    floor: DistanceSensor
    gyroscope: Gyroscope
    left: AudioChunk
    right: AudioChunk
    status: int
    message: str
    def __init__(self, front: _Optional[_Union[DistanceSensor, _Mapping]] = ..., front1: _Optional[_Union[DistanceSensor, _Mapping]] = ..., floor: _Optional[_Union[DistanceSensor, _Mapping]] = ..., gyroscope: _Optional[_Union[Gyroscope, _Mapping]] = ..., left: _Optional[_Union[AudioChunk, _Mapping]] = ..., right: _Optional[_Union[AudioChunk, _Mapping]] = ..., status: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...
