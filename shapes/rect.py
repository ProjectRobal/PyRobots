from base.object import Object
from typing import Tuple
import pymunk
from pymunk import Vec2d


def MakeRect(size:Vec2d,position:Vec2d,body)->pymunk.Poly:

    return pymunk.Poly(body,[(-size[0]/2 + position[0],-size[1]/2 + position[1]), (size[0]/2 +position[0],-size[1]/2 + position[1]), (size[0]/2+position[0],size[1]/2+ position[1]), (-size[0]/2+ position[0],size[1]/2 + position[1])])

class Rect(Object):
    def __init__(self,name,space,size:Vec2d,mass=1,inertia=10):
        super().__init__(name,space)
        self.body=pymunk.Body(mass,inertia)
        self.shape=MakeRect(size,(0,0),self.body)
        space.space().add(self.body,self.shape)

    def Body(self):
        return self.body
    
    def Shape(self):
        return self.shape