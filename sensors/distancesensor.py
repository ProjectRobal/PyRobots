'''A class that emulate distance sensor'''
from base.sensor import Sensor
from pymunk.vec2d import Vec2d
import pymunk


class DistanceSensor(Sensor):
    '''pos - position of the sensor relative to the body, direction a wersor that point the direction of where the sensor is pointing, distance max sensor distance, radius of the sensor''' 
    def __init__(self,space,obj,pos,direction,distance,radius):
        super().__init__(space,obj)
        self._distance = distance
        self._pos = Vec2d(pos[0],pos[1])
        self._direction = Vec2d(direction[0],direction[1])
        self._radius = radius
        self._mesaurment=0
        body=pymunk.Body(0,0)
        self._point=pymunk.Circle(body,0)
        self._point.position=self._pos+obj.getBody().position
        self._point.sensor=True
        self._joints=pymunk.constraints.PinJoint(obj.getBody(),self._point.body,self._pos)
        space.add(body,self._point)
        space.add(self._joints)

    def getDistance(self):
        return self._mesaurment

    def pre_solve(self,dt):
        pass

    def post_solve(self,dt):
        start=self._obj.getBody().position+self._pos

        start=start.rotated(self._obj.getBody().angle)

        dir=self._direction.rotated(self._obj.getBody().angle)

        end=(start+dir*self._distance)

        info=self.getScene().Space().segment_query(start,end,self._radius,pymunk.ShapeFilter())

        for i in info:
            if i.shape is not None:
                self._mesaurment=i.alpha*self._distance
            else:
                self._mesaurment=8160

        print(self._mesaurment)
