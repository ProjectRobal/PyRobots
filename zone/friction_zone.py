from base.object import Object

import pymunk
from pyglet import shapes

import utils

class FrictionZone(Object):
    '''
    An area object when proper object interact with it , it 
    adds a friction force opposed to object's movement.
    '''
    def __init__(self, name, space,coordinates:list[tuple[float,float]],friction:float):
        '''
        coordinates - a list of tuples of (x,y)
        friction - a coefficient of friction
        '''
        super().__init__(name, space)

        self._body=pymunk.Body(0,0,body_type=pymunk.Body.STATIC)

        self._shape=pymunk.Poly(self._body,coordinates)
        self._shape.sensor=True
        self._coords=coordinates
        self._color=(0,0,0)
        self._friction=friction

        self.anchor=utils.get_anchor(self._shape)

        space.add(self._body,self._shape)

    def Color(self,color=None):
        if color is None:
            return self._color
        
        self._color=color

    def draw(self,batch):
        self.poly=shapes.Polygon(self._coords,self._color,batch=batch)

        utils._to_pyglet_coords(self.anchor,self._shape,self.poly)

    
    def Body(self):
        return self._body

    def Shape(self):
        return self._shape

    