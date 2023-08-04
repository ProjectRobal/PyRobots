from base.object import Object
import pymunk
import math

'''A class for dc motor simulation'''

class DCMotor(Object):

    '''torque - a max engine torque, vmax - max engine speed, body - target body, origin - a point where to apply force'''
    def __init__(self,name,scene,body,origin,torque,max_power,vmax):
        super().__init__(name,scene)
        self._torque = torque
        self._vmax = vmax
        self._a=self._torque/self._vmax
        self._power=0 #0-100
        self._max_power=max_power
        self._body=body
        self._origin = pymunk.Vec2d(*origin)
        self._k=2.0
        self._direction=1


    def set_power(self,power):
        if power<0:
            power=0
        if power>100:
            power=100
        self._power = power

    def set_direction(self,direction):


        if direction==0:
            self._direction=1
        elif direction==1:
            self._direction=-1
        else:
            self._direction=0


    def Loop(self,dt):
        # it should also depends on angular velocity

        vel=abs(self.Body().velocity + self.Body().angular_velocity*pymunk.Vec2d.rotated(self._origin,self.Body().angle))/self._k

        force=((self._torque-(self._a*vel))*self._direction)*(self._power/100.0)
        
        force_vec=(force*math.cos(self.Body().angle),force*math.sin(self.Body().angle))

        self.Body().apply_force_at_local_point(force_vec,pymunk.Vec2d.rotated(self._origin,self.Body().angle))
      
    def Body(self):
        return self._body

    def Shape(self):
        return None
        