from typing import Tuple

import pymunk
import pymunk.pyglet_util
import pyglet

from base.object import Object
from base.eventobject import EventObject

from sensors.frictionsensor import FrictionSensor
from sensors.gyrosensor import Gyro
from sensors.distancesensor import DistanceSensor

from robots.dcmotor import DCMotor

from Scene import Scene

class Rect(Object):
    def __init__(self,name,space:Scene,size:Tuple[int,int]):
        super().__init__(name,space)
        
        self.body=pymunk.Body(1,10)
        self.shape=pymunk.Poly(self.body,[(-size[0]/2,-size[1]/2), (size[0]/2,-size[1]/2), (size[0]/2,size[1]/2), (-size[0]/2,size[1]/2)])

        space.space().add(self.body,self.shape)

    def Body(self):
        return self.body
    
    def Shape(self):
        return self.shape
        

scene=Scene()

rect1=Rect("rect1",scene,(50,50))


rect1.body.position=(100,100)


motor=DCMotor("m1",rect1.body,pymunk.Circle(rect1.body,4,(25,25)),scene,100,50)

motor1=DCMotor("m2",rect1.body,pymunk.Circle(rect1.body,4,(-25,-25)),scene,100,50)



motor.set_power(40)

motor1.set_power(40)

#scene.add_sensor(FrictionSensor("gric",scene,rect1,0.5))

# a list with pymunk objects
scene.add_object(rect1)

scene.add_object(motor)

scene.add_object(motor1)


scene.run()