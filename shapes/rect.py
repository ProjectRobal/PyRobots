from base.object import Object
from typing import Tuple
import pymunk

class Rect(Object):
    def __init__(self,name,space,size:Tuple[int,int]):
        super().__init__(name,space)
        
        self.body=pymunk.Body(1,10)
        self.shape=pymunk.Poly(self.body,[(-size[0]/2,-size[1]/2), (size[0]/2,-size[1]/2), (size[0]/2,size[1]/2), (-size[0]/2,size[1]/2)])

        space.space().add(self.body,self.shape)

    def Body(self):
        return self.body
    
    def Shape(self):
        return self.shape