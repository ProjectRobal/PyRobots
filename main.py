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

from base.hud import HUD
from hud.label import Label
from hud.board import Board,Box
from hud.guage import Gauge,GaugeDesign

import pyaudio

from config import PIXEL_TO_MM

space=pymunk.Space(True)
'''use 4 threads'''
space.threads=4

scene=Scene(space,remote=False)

wall_up=Rect("wall_up",space,(750,25),(25,575),space.static_body)
wall_up.Color((255,0,0))

wall_down=Rect("wall_down",space,(750,25),(25,0),space.static_body)
wall_down.Color((0,255,0))

wall_left=Rect("wall_left",space,(25,800),(0,0),space.static_body)
wall_left.Color((0,0,255))

wall_right=Rect("wall_right",space,(25,800),(775,0),space.static_body)
wall_right.Color((0,0,0))

f_zone=FrictionZone("floor",space,[(0,0),(800,0),(800,600),(0,600)],0.1,[2])
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

#HUD:

def vec2d_to_str(vec:pymunk.Vec2d)->str:
    return str(round(vec.x*PIXEL_TO_MM/10,2))+"cm,"+str(round(vec.y*PIXEL_TO_MM/10,2))+"cm"

def make_label(text:str,fun:callable,x,y,size=10)->list[HUD]:
    label=Label(text,text,(x,y),size)
    info=Label(text+"_info",fun,(x,y-size-10),size)

    return [label,info]

def make_hud():

    labs:list[HUD]=[*make_label("pos:",lambda x=None: vec2d_to_str(rob.getPosition()),100,50),
                    *make_label("rotation:",lambda x=None: str(rob._gyro.get_angular_velocity()),250,75),
                    *make_label("movement:",lambda x=None: str(rob._gyro.get_accel()),250,25),
                    *make_label("front:",lambda x=None: str(rob._front.getDistance())+" mm",400,70),
                    *make_label("floor:",lambda x=None: str(rob._hole.Distance())+" mm",400,30),
                    ]

    info_b=Board("board_bottom",Box(0,100,25,25,color=(255,255,0)),Box(0,0,800,100,color=(255,255,255)),labs)
    info_b_label=Label("board_b_label","Sensors",(0,125),10)

    scene.add_hud(info_b)

    for l in labs:
        scene.add_hud(l)
    
    scene.add_hud(info_b_label)

    labs1:list[HUD]=[
        *make_label("motorA:",lambda x=None: "pow: "+str(rob._m1._power)+" dir:"+str(rob._m1._direction),100,70),
        *make_label("motorB:",lambda x=None: "pow: "+str(rob._m2._power)+" dir:"+str(rob._m2._direction),100,30),
        Gauge("servo1",lambda x=None: rob.getServo()[0],250,50,0,180,0,180,design=GaugeDesign(radius=30)),
        Label("servo1_label","angel",(225,0),10),
        Gauge("servo2",lambda x=None: rob.getServo()[1],350,50,0,180,0,180,design=GaugeDesign(radius=30)),
        Label("servo2_label","angel",(325,0),10)
    ]

    info_a=Board("board_top",Box(0,300,25,25,color=(255,0,255)),Box(0,0,800,100,color=(255,255,255)),labs1)
    info_a_label=Label("board_a_label","Outputs",(0,325),10)

    scene.add_hud(info_a)

    for l in labs1:
        scene.add_hud(l)

    scene.add_hud(info_a_label)


make_hud()

rob.setPosition((600,450))

rob.run()

scene.run()

rob.stop()