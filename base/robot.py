from base.object import Object
from robots.dcmotor import DCMotor
from sensors.laser import Laser
from sensors.gyrosensor import Gyro
from sensors.frictionsensor import FrictionSensor

from shapes.rect import Rect

class Robot:

    def __init__(self,space):
        self._space = space
        self._base = Rect("base",space,(50,50))
        self._m1=DCMotor("m1",space,self._base.Body(),(0.0,50.0),1,500)
        self._m2=DCMotor("m2",space,self._base.Body(),(0.0,-50.0),1,500)
        self._front=Laser("front",space,self._base,(26,0),(1,0),100,1)

        self._gyro=Gyro("gyro",space,self._base)
        self._friction=FrictionSensor("friction",space,self._base,1)

        self._front.Show(True)

        space.add_object(self._base)
        space.add_object(self._m1)
        space.add_object(self._m2)

        space.add_sensor(self._front)

        self._m1.set_power(20)
        self._m2.set_power(20)

    def getPosition(self):
        return self._base.Body().position

    def setPosition(self,position):
        self._base.Body().position = position
        self._space.space().reindex_shapes_for_body(self._base.Body())
        

