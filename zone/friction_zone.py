from base.object import Object

import pymunk
from pyglet import shapes
import math

import utils

from config import *

class FrictionZone(Object):
    '''
    An area object when proper object interact with it , it 
    adds a friction force opposed to object's movement.
    '''
    def __init__(self, name, space,coordinates:list[pymunk.Vec2d],friction:float,damping:float,iteraction_list:list[int],id=1):
        '''
        coordinates - a list of Vec2ds
        friction - a coefficient of friction
        iteraction_list - a list of collsion types object will iteract with
        id - a collision type of zone, allow to use multiple zone in one simulation
        '''
        super().__init__(name, space)

        self.body=pymunk.Body(0,0,body_type=pymunk.Body.STATIC)

        self.shape=pymunk.Poly(self.body,coordinates)
        self.shape.filter=pymunk.ShapeFilter(group=1)
        self.shape.sensor=True
        self.shape.collision_type=id

        self._color=(0,0,0)
        self._friction=friction
        self._damping=damping

        self.pos=utils.get_anchor_static(self.shape)

        for i in iteraction_list:
            handle=space.add_collision_handler(id,i)
            handle.pre_solve=self._pre_solve

        space.add(self.body,self.shape)

    def _pre_solve(self,arbiter:pymunk.Arbiter,space,data):
        on_floor:pymunk.Shape=arbiter.shapes[1]

        on_floor.body.velocity=on_floor.body.velocity*self._friction
       
        on_floor.body.angular_velocity=self._damping*on_floor.body.angular_velocity

        return True
        

    def Color(self,color=None):
        if color is None:
            return self._color
        
        self._color=color

    def draw(self,batch):
        self.poly=shapes.Polygon(*self.shape.get_vertices(),color=self._color,batch=batch)
        self.poly.position=self.pos
        #utils._to_pyglet_coords(self.pos,self.shape,self.poly)

    
    def Body(self):
        return self.body

    def Shape(self):
        return self.shape

    