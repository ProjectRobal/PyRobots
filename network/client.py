import grpc
import _grpc.rc_service_pb2_grpc as pb2_grpc
from _grpc.rc_service_pb2 import _None,Motor,DistanceSensor,Gyroscope,Servo,AudioChunk,Command,Message
import json

def send_message(stub:pb2_grpc.RCRobotStub,speedA,directionA,speedB,directionB,angel1,angel2):

    msg=Command(mA=Motor(direction=int(directionA),speed=int(speedA)),mB=Motor(direction=int(directionB),speed=int(speedB)),ear1=Servo(angle=int(angel1)),ear2=Servo(angle=int(angel2)))

    return stub.SendCommand(msg)    

def send_message_data(stub:pb2_grpc.RCRobotStub,data):

    return send_message(stub=stub,speedA=data["Motors"]["speedA"],directionA=data["Motors"]["directionA"],speedB=data["Motors"]["speedB"],directionB=data["Motors"]["directionB"],angel1=data["Servos"]["pwm1"],angel2=data["Servos"]["pwm2"])

def process(stub:pb2_grpc.RCRobotStub,speedA,directionA,speedB,directionB,angel1,angel2):

    msg=Command(mA=Motor(direction=int(directionA),speed=int(speedA)),mB=Motor(direction=int(directionB),speed=int(speedB)),ear1=Servo(angle=int(angel1)),ear2=Servo(angle=int(angel2)))
    
    return stub.Process(msg)

def process_data(stub:pb2_grpc.RCRobotStub,data):

    return process(stub,speedA=data["Motors"]["speedA"],directionA=data["Motors"]["directionA"],speedB=data["Motors"]["speedB"],directionB=data["Motors"]["directionB"],angel1=data["Servos"]["pwm1"],angel2=data["Servos"]["pwm2"])

def read_data(stub:pb2_grpc.RCRobotStub):

    return stub.ReadData(_None)

def get_stub(channel)->pb2_grpc.RCRobotStub:
    return pb2_grpc.RCRobotStub(channel)

def connect(address):
    return grpc.insecure_channel(address)