from base.object import Object
from robots.dcmotor import DCMotor
from sensors.laser import Laser
from sensors.gyrosensor import Gyro
from sensors.holesensor import HoleSensor
from sensors.microphone import Microphone
from audiosource.mic_source import MicSource

from concurrent import futures
import grpc
from _grpc.rc_service_pb2 import Message,_None,Gyroscope,DistanceSensor,AudioChunk
import _grpc.rc_service_pb2_grpc as rc_service_pb2_grpc

from shapes.rect import Rect

from Scene import Scene

import pymunk

class Robot(rc_service_pb2_grpc.RCRobotServicer):

    def __init__(self,scene:Scene,position=(0,0)):
        self._scene = scene
        self._base = Rect("base",scene.Space(),(50,50),(-25,-25),pymunk.Body(10,1))
        self._base.Color((231, 255, 13,255))

        self._servo=[0,0]
        #self._base.Shape().collision_type=2

        self._motor1=Rect("motor1",scene.Space(),(50,5),(-25,25),self._base.Body())
        self._motor2=Rect("motor2",scene.Space(),(50,5),(-25,-30),self._base.Body())
        self._motor1.Shape().collision_type=2
        self._motor2.Shape().collision_type=2

        self._m1=DCMotor("m1",scene.Space(),self._base.Body(),(-25.0,50.0),100,500)
        self._m2=DCMotor("m2",scene.Space(),self._base.Body(),(25.0,-50.0),100,500)

        self._hole=HoleSensor("floor",scene.Space(),self._base,(50,0))

        self._front=Laser("front",scene.Space(),self._base,(26,0),(1,0),100,1)

        self._gyro=Gyro("gyro",scene.Space(),self._base)

        # a list of microphones
        self._microphones=[
            Microphone("mic1",scene.Space(),self._base,(20,25)),
            Microphone("mic2",scene.Space(),self._base,(20,-25))
        ]

        self._a_source=MicSource("mic",scene.Space(),self._microphones,1.0)

        self._front.Show(True)
        self._hole.Show(True)
        
        scene.add_object(self._base)
        scene.add_object(self._motor1)
        scene.add_object(self._motor2)
        scene.add_object(self._m1)
        scene.add_object(self._m2)
        scene.add_object(self._a_source)

        scene.add_sensor(self._front)
        scene.add_sensor(self._hole)

        for micro in self._microphones:
            micro.Show(True)
            scene.add_sensor(micro)
            
        self._m1.set_power(90)
        self._m2.set_power(90)

        self.setPosition(position)

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

        self._m1.set_power(params["Motors"]["speedA"])
        self._m2.set_power(params["Motors"]["speedB"])

        self._m1.set_direction(params["Motors"]["directionA"])
        self._m2.set_direction(params["Motors"]["directionB"])

    def PackageData(self):
        
        gyro=Gyroscope()

        gyro.acceleration[:]=self._gyro.get_accel()
        gyro.gyroscope[:]=self._gyro.get_angular_velocity()
        gyro.accel_range=[9.81*16]*3
        gyro.gyro_range=[2000]*3

        front=DistanceSensor(distance=self._front.getDistance())
        floor=DistanceSensor(distance=self._floor.getDistance())

        left=AudioChunk()
        right=AudioChunk()

        left.data[:]=self._microphones[0].Buffer()
        right.data[:]=self._microphones[1].Buffer()

        msg=Message(front=front,floor=floor,
        left=left,right=right,gyroscope=gyro,status=0,message="")

        return msg

    def Process(self, request, context):

        self.UpdateParams(request)
        
        return self.PackageData()

    def SendCommand(self, request, context):

        self.UpdateParams(request)

        return _None()

    def run(self):
        server= grpc.server(futures.ThreadPoolExecutor(max_workers=10))

        rc_service_pb2_grpc.add_RCRobotServicer_to_server(
            self,server
        )
        server.add_insecure_port('127.0.0.1:5051')
        server.start()
        #server.wait_for_termination()
        
