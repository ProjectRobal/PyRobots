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
from shapes.rect import MakeRect

from static.static import Static


scene=Scene()

rob=Robot(scene)

obstacle=Static("obstacle",scene,MakeRect,((40,40),(300,200)))


rob.setPosition((200,200))


scene.run()