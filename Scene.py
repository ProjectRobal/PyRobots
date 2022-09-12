# a main class to maintain the GUI and physic engine
import pymunk
import pyglet
import pymunk.pyglet_util

from base.object import Object
from base.sensor import Sensor

def always_collide(arbiter,space,data):
        return True

def do_nothing(arbiter,space,data):
        return None

class Scene:
    # win - a reference to the window object to draw on
    def __init__(self,window):
        self._window = window
        self._objects={}
        self._sensors={}
        self._space=pymunk.Space()
        self._space.gravity =(0,0)
        self._options=pymunk.pyglet_util.DrawOptions()
        pyglet.clock.schedule_interval(self.update,0.01)

    def run(self):
        pyglet.app.run()

    def on_draw(self):
        pyglet.gl.glClearColor(255, 255, 255, 255)
        self._window.clear()
        self._space.debug_draw(self._options)


    def update(self,dt):
        
        for sensor in self._sensors:
            sensor.pre_solve(self,dt)

        self._space.step(dt)

        for sensor in self._sensors:
            sensor.post_solve(self,dt)
    
    def get_obj_list(self):
        return self._objects

    def add_sensor(self,sensor):
        
        if isinstance(sensor,Sensor):
            self._sensors[sensor.Name()]=sensor

    def remove_sensor(self,sensor):

        if type(sensor) is str:
            if sensor in self._objects.keys():
                del self._sensors[sensor]

        self._sensors.remove(sensor)

    def add_object(self,obj):

        if isinstance(obj,Object):
            self._objects[obj.Name]=obj

    def remove_object(self,obj):

        if type(obj) is str:
            if obj in self._objects.keys():
                del self._objects[obj]
        if isinstance(obj,Object):
            self._objects.remove(obj)


    def getStaticBody(self):
        return self._space.static_body

    def Space(self):
        return self._space
    
    
