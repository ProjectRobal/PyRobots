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
    def __init__(self, name, space,coordinates:list[pymunk.Vec2d],friction:float,iteraction_list:list[int],id=1):
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

        self.pos=utils.get_anchor_static(self.shape)

        for i in iteraction_list:
            handle=space.add_collision_handler(id,i)
            handle.pre_solve=self._pre_solve

        space.add(self.body,self.shape)

    def _pre_solve(self,arbiter:pymunk.Arbiter,space,data):
        on_floor:pymunk.Shape=arbiter.shapes[1]
        
        velocity:pymunk.Vec2d=on_floor.body.velocity


        mass=on_floor.body.mass

        friction=mass*10*self._friction

        if abs(on_floor.body.angular_velocity)>0:

            area=on_floor.area

            radius=math.sqrt(area/math.pi)

            anti_torque=friction*radius

            if abs(on_floor.body.angular_velocity)-abs(anti_torque*STEP_TIME/mass)<=0:
                on_floor.body.angular_velocity=0
            else:
                on_floor.body.apply_force_at_local_point(force=pymunk.Vec2d((-on_floor.body.angular_velocity/abs(on_floor.body.angular_velocity))*anti_torque/radius,0),point=pymunk.Vec2d(0,radius))
        
        print(on_floor.body.angular_velocity)

        if abs(velocity) <= 0:
            return True

        #print(velocity)

        f_force=friction*(-velocity.normalized())

        #print(on_floor.body.angular_velocity)

        if abs(velocity)-abs(f_force/mass)*STEP_TIME<=0:
            on_floor.body.velocity=(0,0)
            return True
        
        center=on_floor.bb.center()

        on_floor.body.apply_force_at_world_point(f_force,center)


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

    