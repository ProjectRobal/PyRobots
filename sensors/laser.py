'''A class that emulate distance sensor'''
from base.sensor import Sensor
from pymunk.vec2d import Vec2d
import pymunk
import math

import pyglet
from pyglet import shapes


class Laser(Sensor):
    '''pos - position of the sensor relative to the body, direction a wersor that point the direction of where the sensor is pointing, distance max sensor distance, radius of the sensor''' 
    def __init__(self,name,space,obj,pos,direction,distance,radius):
        super().__init__(name,space,obj)
        self._distance = distance
        self._pos = Vec2d(pos[0],pos[1])
        self._direction = Vec2d(direction[0],direction[1])
        self._radius = radius
        self._mesaurment=0
        self.start=Vec2d(0,0)
        self.end=Vec2d(0,0)

    def visualize(self,batch):
        self.line=shapes.Line(self.start[0],self.start[1],self.end[0],self.end[1],color=(255,0,0),batch=batch)

    def getDistance(self):
        return self._mesaurment

    def pre_solve(self,dt):
        pass

    def post_solve(self,dt):
        rotation=self._obj.Body().angle

        #transform sensor position

        self.start=self._pos

        self.start=self.start.rotated(rotation)

        self.start=self._obj.Body().position+self.start

        dir=self._direction.rotated(rotation)

        self.end=(self.start+dir*self._distance)

        info=self._space.segment_query(self.start,self.end,self._radius,pymunk.ShapeFilter())

        for i in info:
            if i.shape is not None:
                self._mesaurment=i.alpha*self._distance
                self.end=i.point
                break
            else:
                self._mesaurment=8160

        #print(self._mesaurment)