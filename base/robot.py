from base.object import Object
from robots.dcmotor import DCMotor
from sensors.laser import Laser
from sensors.gyrosensor import Gyro
from sensors.frictionsensor import FrictionSensor

from shapes.rect import Rect

from Scene import Scene

import pymunk

class Robot:

    def __init__(self,scene:Scene,position=(0,0)):
        self._scene = scene
        self._base = Rect("base",scene.Space(),(50,50),(0,0),pymunk.Body(10,1))
        self._base.setColor((231, 255, 13,255))

        self._m1=DCMotor("m1",scene.Space(),self._base.Body(),(0.0,50.0),5,500)
        self._m2=DCMotor("m2",scene.Space(),self._base.Body(),(0.0,-50.0),5,500)

        self._front=Laser("front",scene.Space(),self._base,(26,0),(1,0),100,1)

        self._gyro=Gyro("gyro",scene.Space(),self._base)
        self._friction=FrictionSensor("friction",scene.Space(),self._base,1)

        self._front.Show(True)

        scene.add_object(self._base)
        scene.add_object(self._m1)
        scene.add_object(self._m2)

        scene.add_sensor(self._front)

        self._m1.set_power(65)
        self._m2.set_power(65)

        self.setPosition(position)

    def getPosition(self):
        return self._base.Body().position

    def setPosition(self,position):
        self._base.Body().position = position
        self._scene.Space().reindex_shapes_for_body(self._base.Body())
        

