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

from hud.label import Label

import pyaudio

#To do:
# Microphone
# Sound source
# HUD:
# Background to label
# speedometer
# progress bars

space=pymunk.Space(True)
'''use 4 threads'''
space.threads=4

scene=Scene(space)

wall_up=Rect("wall_up",space,(750,25),(25,575),space.static_body)
wall_up.Color((255,0,0))

wall_down=Rect("wall_down",space,(750,25),(25,0),space.static_body)
wall_down.Color((0,255,0))

wall_left=Rect("wall_left",space,(25,800),(0,0),space.static_body)
wall_left.Color((0,0,255))

wall_right=Rect("wall_right",space,(25,800),(775,0),space.static_body)
wall_right.Color((0,0,0))

f_zone=FrictionZone("floor",space,[(0,0),(800,0),(800,600),(0,600)],0.4,[2])
f_zone.Color((250, 209, 95))

hole_pos=(300,400)

h_zone=Hole("hole",space,[(hole_pos[0],hole_pos[1]),(100+hole_pos[0],hole_pos[1]),
(100+hole_pos[0],100+hole_pos[1]),(hole_pos[0],100+hole_pos[1])])

scene.add_object(f_zone)
scene.add_object(wall_up)
scene.add_object(wall_down)
scene.add_object(wall_left)
scene.add_object(wall_right)
scene.add_object(h_zone)

rob=Robot(scene,(0,0))

#HUD

#hello=Label("hello",rob.getPosition,(0,100))

#scene.add_hud(hello)

#obstacle.Body().position=(200,200)

rob.setPosition((200,150))

rob.run()

scene.run()
