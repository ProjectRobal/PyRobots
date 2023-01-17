from base.object import Object
from typing import Tuple
import pymunk
from pymunk import Vec2d
import pyglet
from pyglet import shapes
import math
import utils


def MakeRect(size:Vec2d,position:Vec2d,body)->pymunk.Poly:

    return pymunk.Poly(body,[(-size[0]/2 + position[0],-size[1]/2 + position[1]), (size[0]/2 +position[0],-size[1]/2 + position[1]), (size[0]/2+position[0],size[1]/2+ position[1]), (-size[0]/2+ position[0],size[1]/2 + position[1])])

class Rect(Object):
    def __init__(self,name,space,size:Vec2d,pos:Vec2d,body:pymunk.Body):
        super().__init__(name,space)
        self.body=body
        self.shape=MakeRect(size,pos,self.body)
        if body.space is None:
            space.add(self.body,self.shape)
        self.color=(0,0,0)
        self.anchor=utils.get_anchor(self.shape)

    def setColor(self,color):
        self.color=color

    def draw(self,batch):
        self.rec=shapes.Polygon(*self.shape.get_vertices(),color=self.color,batch=batch)
        utils._to_pyglet_coords(self.anchor,self.shape,self.rec)

    def Body(self):
        return self.body
    
    def Shape(self):
        return self.shape