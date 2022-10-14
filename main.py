from typing import Tuple

import pymunk
import pymunk.pyglet_util
import pyglet

from base.object import Object
from base.eventobject import EventObject

from sensors.frictionsensor import FrictionSensor
from sensors.gyrosensor import Gyro

from base.robot import Robot

from Scene import Scene

from shapes.rect import Rect


scene=Scene()

rob=Robot(scene)

obstacle=Rect("obstacle",scene,(40,40))


rob.setPosition((200,200))

obstacle.Body().position=(300,200)

scene.run()