'''A sensor that emulate friction on object'''

from base.sensor import Sensor
from pymunk import Vec2d

class FrictionSensor(Sensor):
    '''u a friction ratio'''
    def __init__(self,name,scene,obj,u):
        super().__init__(name,scene,obj)
        self._fric_u=u

    def pre_solve(self,dt):
        pass

    def post_solve(self,dt):
        mass=self._obj.Body().mass
        velocity=self._obj.Body().velocity
        # we are going to act against velocity
        velocity=-velocity
        vel_mod=abs(velocity)

        if vel_mod ==0:
            return
        # the wersor of the velocity
        direction=velocity/vel_mod

        force=9.81*self._fric_u

        v_after=vel_mod-(force*dt)

        if v_after > 0:

            self._obj.Body().apply_force_at_local_point(direction*force*mass,(0,0))
        else:
            self._obj.Body().velocity=(0,0)