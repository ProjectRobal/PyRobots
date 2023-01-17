from base.object import Object

import pymunk
from pyglet import shapes

import utils

class FrictionZone(Object):
    '''
    An area object when proper object interact with it , it 
    adds a friction force opposed to object's movement.
    '''
    def __init__(self, name, space,coordinates:list[tuple[float,float]],friction:float,iteraction_list:list[int]):
        '''
        coordinates - a list of tuples of (x,y)
        friction - a coefficient of friction
        '''
        super().__init__(name, space)

        self.body=pymunk.Body(0,0,body_type=pymunk.Body.STATIC)

        self.shape=pymunk.Poly(self.body,coordinates)
        self.shape.sensor=True

        self._color=(0,0,0)
        self._friction=friction

        self.anchor=utils.get_anchor(self.shape)

        for i in iteraction_list:
            handle=space.add_collision_handler(1,i)
            handle.pre_solve=self._pre_solve

        space.add(self.body,self.shape)

    def _pre_solve(self,arbiter,data):
        on_floor:pymunk.Shape=arbiter.shapes()[1]
        
        velocity:pymunk.Vec2d=on_floor.body.velocity

        if abs(velocity) <= 0:
            return

        mass=on_floor.body.mass

        friction=mass*10*self._friction

        f_force=friction*-velocity.normalized()

        on_floor.body.apply_force_at_local_point(f_force)
        

    def Color(self,color=None):
        if color is None:
            return self._color
        
        self._color=color

    def draw(self,batch):
        self.poly=shapes.Polygon(*self.shape.get_vertices(),self._color,batch=batch)

        utils._to_pyglet_coords(self.anchor,self.shape,self.poly)

    
    def Body(self):
        return self.body

    def Shape(self):
        return self.shape

    