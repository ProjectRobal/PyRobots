'''A class that emulate distance sensor'''
from base.sensor import Sensor
from pymunk.vec2d import Vec2d
from pymunk import PointQueryInfo


class DistanceSensor(Sensor):
    '''pos - position of the sensor relative to the body, direction a wersor that point the direction of where the sensor is pointing, distance max sensor distance, radius of the sensor''' 
    def __init__(self,name,id,scene,obj,pos,direction,distance,radius):
        super().__init__(name,id,scene,obj)
        self._distance = distance
        self._pos = Vec2d(pos[0],pos[1])
        self._direction = Vec2d(direction[0],direction[1])
        self._radius = radius
        self._mesaurment=0

    def getDistance(self):
        return self._mesaurment

    def pre_solve(self,scene,dt):
        pass

    def post_solve(self,scene,dt):
        start=self._obj.getBody().position+self._pos

        start=start.rotated(self._obj.getBody().angle)

        dir=self._direction.rotated(self._obj.getBody().angle)

        end=(start+dir*self._distance)

        info=self._obj.getShape().segment_query(start,end,self._radius)

        if info.shape is not None:
            self._mesaurment=info.alpha*self._distance
        else:
            self._mesaurment=8160
