'''A sensor that act like gyroscope + accelerometer'''
from base.sensor import Sensor
from pymunk.vec2d import Vec2d

import numpy as np
from config import PIXEL_TO_MM

G=9.81

GYRO_DIM=2000.0

ACCEL_RANGE=float(2**16 -1)
GYRO_RANGE=float(2**16 -1)

class Gyro(Sensor):
    '''pos a position of the gyroscope respect to the obj ( a tuple (x,y))''' 
    '''Now it will pass information about change of rotations and change of movement'''
    def __init__(self,name,scene,obj):
        super().__init__(name,scene,obj)
        self._acceleration=np.array([0,0,0],dtype=np.int32)
        self._angular_velocity = np.array([0,0,0],dtype=np.int32)
        self._velocity1=Vec2d(0,0)
        self._velocity2=Vec2d(0,0)
        self._dt=0

    def get_accel(self):
        return self._acceleration*PIXEL_TO_MM

    def get_angular_velocity(self):
        return self._angular_velocity*PIXEL_TO_MM
    
    def get_rotation(self):
        return [0,0,np.round(self._obj.Body().angle,1)]

    def pre_solve(self,dt):
        self._velocity1 = self._obj.Body().velocity*PIXEL_TO_MM
        self._dt=dt

    def post_solve(self,dt):
        self._velocity2 = self._obj.Body().velocity*PIXEL_TO_MM
        self._dt+=dt
        if self._dt==0:
            return
        dv=(self._velocity2-self._velocity1)/1000.0
        #print(dv)
        #print(dt)
        #self._acceleration=np.array((0,self._velocity2[0]*dt ,self._velocity2[1]*dt),dtype=np.int32)
        self._acceleration=np.array((0,(dv[0]/self._dt)*32767/2 ,(dv[1]/self._dt)*32767/2),dtype=np.int32)
        self._angular_velocity=np.array([0,0,self._obj.Body().angular_velocity*dt],dtype=np.int32)
        #print(self._acceleration)
        #print(self._angular_velocity)

