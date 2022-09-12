'''A sensor that act like gyroscope + accelerometer'''
from base.sensor import Sensor
from pymunk.vec2d import Vec2d


class Gyro(Sensor):
    '''pos a position of the gyroscope respect to the obj ( a tuple (x,y))''' 
    def __init__(self,space,obj):
        super().__init__(space,obj)
        self._acceleration=Vec2d(0,0)
        self._angular_velocity = Vec2d(0,0)
        self._velocity1=Vec2d(0,0)
        self._velocity2=Vec2d(0,0)
        self._dt=0

    def get_accel(self):
        return self._acceleration

    def get_angular_velocity(self):
        return self._angular_velocity

    def pre_solve(self,dt):
        self._acceleration=Vec2d(0,0)
        self._angular_velocity = Vec2d(0,0)
        self._velocity1 = self._obj.getBody().velocity
        self._dt=dt



    def post_solve(self,dt):
        self._velocity2 = self._obj.getBody().velocity
        self._dt+=dt
        if self._dt==0:
            return
        dv=self._velocity2-self._velocity1
        self._acceleration=dv/self._dt
        self._angular_velocity=Vec2d(0,self._obj.getBody().angular_velocity)



