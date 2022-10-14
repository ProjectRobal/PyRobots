'''A class that emulate distance sensor'''
from base.sensor import Sensor
from pymunk.vec2d import Vec2d
import pymunk


class Laser(Sensor):
    '''pos - position of the sensor relative to the body, direction a wersor that point the direction of where the sensor is pointing, distance max sensor distance, radius of the sensor''' 
    def __init__(self,name,space,obj,pos,direction,distance,radius):
        super().__init__(name,space,obj)
        self._distance = distance
        self._pos = Vec2d(pos[0],pos[1])
        self._direction = Vec2d(direction[0],direction[1])
        self._radius = radius
        self._mesaurment=0

    def getDistance(self):
        return self._mesaurment

    def pre_solve(self,dt):
        pass

    def post_solve(self,dt):
        rotation=self._obj.Body().angle

        #transform sensor position
        start=self._obj.Body().position+self._pos

        start=start.rotated(rotation)

        dir=self._direction.rotated(rotation)

        end=(start+dir*self._distance)

        info=self.getSpace().space().segment_query(start,end,self._radius,pymunk.ShapeFilter())

        for i in info:
            if i.shape is not None:
                self._mesaurment=i.alpha*self._distance
            else:
                self._mesaurment=8160

        print(self._mesaurment)
