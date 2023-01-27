from base.object import Object
from robots.dcmotor import DCMotor
from sensors.laser import Laser
from sensors.gyrosensor import Gyro
from sensors.holesensor import HoleSensor
from sensors.microphone import Microphone
from audiosource.mic_source import MicSource

from shapes.rect import Rect

from Scene import Scene

import pymunk

class Robot:

    def __init__(self,scene:Scene,position=(0,0)):
        self._scene = scene
        self._base = Rect("base",scene.Space(),(50,50),(-25,-25),pymunk.Body(10,1))
        self._base.Color((231, 255, 13,255))
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

    def applySound(self,pos,buffer):
        '''In this function sound in a buffer will be applied to microphones
        pos - a position of a sound source
        buffer - a sound sample'''
        
        for micro in self._microphones:
            m_pos=micro.getPosition()


        

