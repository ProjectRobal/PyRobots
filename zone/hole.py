from base.object import Object

import pymunk
from pyglet import shapes

import utils

from config import *

class Hole(Object):
    def __init__(self,name,space,coordinates:list[pymunk.Vec2d],id=5):
        super().__init__(name,space)

        self.body=pymunk.Body(0,0,body_type=pymunk.Body.STATIC)

        self.shape=pymunk.Poly(self.body,coordinates)
        self.shape.sensor=True
        self.shape.collision_type=id

        self._color=(0,0,0)

        self.pos=utils.get_anchor(self.shape)

        space.add(self.body,self.shape)

    def Color(self,color=None):
        if color is None:
            return self._color
        self._color=color

    def draw(self,batch):
        self.rec=shapes.Polygon(*self.shape.get_vertices(),color=self._color,batch=batch)
        self.rec.anchor_position=self.pos

    def Body(self):
        return self.body

    def Shape(self):
        return self.shape


