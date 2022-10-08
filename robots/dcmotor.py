from base.object import Object
import pymunk
import math

'''A class for dc motor simulation'''

class DCMotor(Object):

    '''torque - a max engine torque, vmax - max engine speed'''
    def __init__(self,name,body,shape,space,torque,vmax):
        super().__init__(name,space)
        self._torque = torque
        self._vmax = vmax
        self._power=0 #0-100
        self._body=body
        self._shape=shape
        space.space().add(self._shape)


    def set_power(self,power):
        if power<0 and power>100:
            return
        self._power = power

    def Loop(self):

        if abs(self.Body().velocity)>=self._vmax:
            return

        vel=abs(self.Body().velocity)

        force=self._torque*math.exp(-vel)*(self._power/100.0)
        
        print(self.Name()," ",force," ",vel)

        force_vec=(force*math.cos(self.Body().angle),force*math.sin(self.Body().angle))

        self.Body().apply_force_at_local_point(force_vec,self._shape.offset)

    def Body(self):
        return self._body

    def Shape(self):
        return self._shape
        