from typing import Tuple

import pymunk
import pymunk.pyglet_util
import pyglet

from base.object import Object
from base.eventobject import EventObject

from sensors.frictionsensor import FrictionSensor
from sensors.gyrosensor import Gyro

from base.robot import Robot

import pymunk

from Scene import Scene

from shapes.rect import Rect

space=pymunk.Space(True)
'''use 4 threads'''
space.threads=4

scene=Scene(space)

rob=Robot(scene,(0,0))

obstacle=Rect("obstacle",space,(100,100),(300,200),pymunk.Body(0,0,body_type=pymunk.Body.STATIC))
obstacle.setColor((255,0,0))
scene.add_object(obstacle)

rob.setPosition((200,200))

scene.run()