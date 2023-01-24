from typing import Tuple

import pymunk
import pymunk.pyglet_util
import pyglet

from base.object import Object
from base.eventobject import EventObject

from sensors.gyrosensor import Gyro

from base.robot import Robot

import pymunk

from Scene import Scene

from shapes.rect import Rect
from zone.friction_zone import FrictionZone
from zone.hole import Hole

#To do:
# Microphone
# Sound source
# HUD

space=pymunk.Space(True)
'''use 4 threads'''
space.threads=4

scene=Scene(space)

obstacle=Rect("obstacle",space,(100,100),(200,200),pymunk.Body(0,0,body_type=pymunk.Body.STATIC))
obstacle.Color((255,0,0))

f_zone=FrictionZone("floor",space,[(-200,-200),(200,-200),(200,200),(-200,200)],0.4,[2])
f_zone.Color((250, 209, 95))

h_zone=Hole("hole",space,[(200,-200),(600,-200),(600,200),(200,200)])

scene.add_object(h_zone)
scene.add_object(f_zone)
scene.add_object(obstacle)

rob=Robot(scene,(0,0))

#obstacle.Body().position=(200,200)

rob.setPosition((50,175))

scene.run()