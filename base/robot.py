from base.object import Object
from robots.dcmotor import DCMotor
from sensors.laser import Laser
from sensors.gyrosensor import Gyro
from sensors.holesensor import HoleSensor
from sensors.microphone import Microphone
from audiosource.mic_source import MicSource
from audiosource.mic_source_static import MicSourceStatic
from audiosource.mic_source_noise import MicSourceNoise

from concurrent import futures
import grpc
from _grpc.rc_service_pb2 import Message,_None,Gyroscope,DistanceSensor,AudioChunk
import _grpc.rc_service_pb2_grpc as rc_service_pb2_grpc

from shapes.rect import Rect

from Scene import Scene


import pymunk
import threading
import numpy as np
from config import *


from scipy import signal
import numpy as np

SAMPLE_RATE=16000

class Robot(rc_service_pb2_grpc.RCRobotServicer):

    def __init__(self,scene:Scene,position=(0,0)):
        self._scene = scene
        self._base = Rect("base",scene.Space(),(58,50),(-29,-25),pymunk.Body(30,200))
        self._base.Color((231, 255, 13,255))
        self._base.Shape().filter=pymunk.ShapeFilter(group=1)

        self._servo=[0,0]
        #self._base.Shape().collision_type=2

        self._motor1=Rect("motor1",scene.Space(),(58,15),(-29,25),self._base.Body())
        self._motor2=Rect("motor2",scene.Space(),(58,15),(-29,-40),self._base.Body())
        self._motor1.Shape().collision_type=2
        self._motor2.Shape().collision_type=2

        self._m1=DCMotor("m1",scene.Space(),self._base.Body(),(0.0,50.0),300,100,100)
        self._m2=DCMotor("m2",scene.Space(),self._base.Body(),(0.0,-50.0),300,100,100)

        self._hole=HoleSensor("floor",scene.Space(),self._base,(50,0))

        self._front1=Laser("front_left",scene.Space(),self._base,(26,12),(1,0),2000,1)
        self._front2=Laser("front_right",scene.Space(),self._base,(26,-12),(1,0),2000,1)

        self._gyro=Gyro("gyro",scene.Space(),self._base)

        # a list of microphones ( audio recivers )
        self._microphones=[
            Microphone("mic1",scene.Space(),self._base,(28,12)),
            Microphone("mic2",scene.Space(),self._base,(28,-12))
        ]

        #self._a_source=MicSource("mic",scene.Space(),self._microphones,1.0)
        #self._a_source=MicSourceStatic("mic",scene.Space(),600,500,self._microphones,0.001)
        self._a_source=MicSourceNoise("mic",scene.Space(),200,500,self._microphones,0.01)

        self._front1.Show(True)
        self._front2.Show(True)
        self._hole.Show(True)
        
        scene.add_object(self._base)
        scene.add_object(self._motor1)
        scene.add_object(self._motor2)
        scene.add_object(self._m1)
        scene.add_object(self._m2)
        scene.add_object(self._a_source)

        scene.add_sensor(self._front1)
        scene.add_sensor(self._front2)
        scene.add_sensor(self._hole)
        scene.add_sensor(self._gyro)

        for micro in self._microphones:
            micro.Show(True)
            scene.add_sensor(micro)
            
        self._m1.set_power(50)
        self._m2.set_power(0)

        self._m1.set_direction(0)
        self._m2.set_direction(0)

        self.setPosition(position)
        #self._base.Body().angle=np.pi/2

        self._scene.update(STEP_TIME)

    def getPosition(self):
        return self._base.Body().position

    def setPosition(self,position):
        self._base.Body().position = position
        self._scene.Space().reindex_shapes_for_body(self._base.Body())

    def getServo(self):
        return self._servo       

    def applySound(self,pos,buffer):
        '''In this function sound in a buffer will be applied to microphones
        pos - a position of a sound source
        buffer - a sound sample'''
        
        for micro in self._microphones:
            m_pos=micro.getPosition()

    def UpdateParams(self,params):

        self._m1.set_power(params.mA.speed)
        self._m2.set_power(params.mB.speed)

        self._m1.set_direction(params.mA.direction)
        self._m2.set_direction(params.mB.direction)

    def PackageData(self):
        
        gyro=Gyroscope()

        gyro.acceleration[:]=np.array(self._gyro.get_accel(),dtype=np.float32)
        gyro.gyroscope[:]=np.array(self._gyro.get_rotation(),dtype=np.float32)
        gyro.accel_range=16
        gyro.gyro_range=2000

        front=DistanceSensor(distance=self._front1.getDistance())
        front1=DistanceSensor(distance=self._front2.getDistance())
        floor=DistanceSensor(distance=self._hole.Distance())

        left=AudioChunk()
        right=AudioChunk()

        left.data[:]=np.array(self._microphones[0].Buffer(),dtype=np.int32)
        right.data[:]=np.array(self._microphones[1].Buffer(),dtype=np.int32)

        #print(left.data[-52:])
        #print(right.data[-52:])
        

        msg=Message(front=front,front1=front1,floor=floor,
        left=left,right=right,gyroscope=gyro,status=0,message="")

        return msg

    def Process(self, request, context):

        self.UpdateParams(request)

        self._scene.update(STEP_TIME)
        
        return self.PackageData()

    def SendCommand(self, request, context):

        self.UpdateParams(request)

        return _None()
    
    def ReadData(self, request, context):

        return self.PackageData()
    
    def _run_server(self):
        self.server= grpc.server(futures.ThreadPoolExecutor(max_workers=10))

        rc_service_pb2_grpc.add_RCRobotServicer_to_server(
            self,self.server
        )
        self.server.add_insecure_port('127.0.0.1:5051')
        self.server.start()
        self.server.wait_for_termination()

    def run_local(self):
        server=threading.Thread(target=self._run_model,args=[])
        server.start()

    def run(self):
        server=threading.Thread(target=self._run_server,args=[])
        server.start()

    def stop(self):
        self.server.stop(None)
