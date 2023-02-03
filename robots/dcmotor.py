from base.object import Object
import pymunk
import math

'''A class for dc motor simulation'''

class DCMotor(Object):

    '''torque - a max engine torque, vmax - max engine speed, body - target body, origin - a point where to apply force'''
    def __init__(self,name,scene,body,origin,torque,vmax):
        super().__init__(name,scene)
        self._torque = torque
        self._vmax = vmax
        self._power=0 #0-100
        self._body=body
        self._origin = origin
        self._k=2.0
        self._direction=1


    def set_power(self,power):
        if power<0 and power>100:
            return
        self._power = power

    def set_direction(self,direction):
        if direction==1:
            self._direction=1
        else:
            self._direction=-1

    def Loop(self,dt):

        vel=abs(self.Body().velocity)/self._k

        force=(self._torque*math.exp(-vel)*(self._power/100.0))*self._direction
        
        force_vec=(force*math.cos(self.Body().angle),force*math.sin(self.Body().angle))

        self.Body().apply_force_at_local_point(force_vec,
        ( self._origin[0]*math.cos(self.Body().angle)-self._origin[1]*math.sin(self.Body().angle)
        ,
        self._origin[1]*math.cos(self.Body().angle)+self._origin[0]*math.sin(self.Body().angle)
        ))
      
    def Body(self):
        return self._body

    def Shape(self):
        return None
        