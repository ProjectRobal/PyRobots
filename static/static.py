from base.object import Object
from typing import Tuple
from pymunk import Vec2d
import pymunk

'''A class that take shape from object and create a static object'''

class Static(Object):
    '''shape is a pointer to a function that create shape, kwargs are the arguments for the function'''
    def __init__(self,name,space,shape,kwargs):
        super().__init__(name,space)
                
        self.body=space.getStaticBody()

        self.shape=shape(*kwargs,self.body)
        
        space.space().add(self.shape)

    def Body(self):
        return None
    
    def Shape(self):
        return self.shape