# a main class to maintain the GUI and physic engine
import pymunk
import pyglet
import pymunk.pyglet_util

from base.object import Object
from base.sensor import Sensor
from base.eventobject import EventObject
from base.hud import HUD

class Scene:
    # win - a reference to the window object to draw on
    def __init__(self):
        self._window = pyglet.window.Window()
        self._objects={}
        self._sensors={}
        self._hud={}
        self._space=pymunk.Space()
        self._space.gravity =(0,0)
        self._options=pymunk.pyglet_util.DrawOptions()
        self._space.debug_draw(self._options)
        self.init_events()
        pyglet.clock.schedule_interval(self.update,0.01)

    def on_key_press(self,symbol, modifiers):
        for obj in self._objects.values():
            if isinstance(obj,EventObject):
                obj.run_press_key(symbol, modifiers)

    def on_key_release(self,symbol, modifiers):
        for obj in self._objects.values():
            if isinstance(obj,EventObject):
                obj.run_release_key(symbol, modifiers)

    def on_mouse_motion(self,x,y,dx,dy):
        for obj in self._objects.values():
            if isinstance(obj,EventObject):
                obj.run_mouse_move(x,y,dx,dy)

    def on_mouse_press(self,x, y, button, modifiers):
        for obj in self._objects.values():
            if isinstance(obj,EventObject):
                obj.run_mouse_press(x,y,button, modifiers)

    def on_mouse_release(self,x, y, button, modifiers):
        for obj in self._objects.values():
            if isinstance(obj,EventObject):
                obj.run_mouse_release(x,y,button, modifiers)

    def on_mouse_drag(self,x, y, dx, dy, buttons, modifiers):
        for obj in self._objects.values():
            if isinstance(obj,EventObject):
                obj.run_mouse_drag(x,y,dx,dy,buttons,modifiers)
    

    def init_events(self):
        window=self._window
        window.on_key_press=self.on_key_press
        window.on_key_release=self.on_key_release
        window.on_mouse_motion=self.on_mouse_motion
        window.on_mouse_press=self.on_mouse_press
        window.on_mouse_release=self.on_mouse_release
        window.on_mouse_drag=self.on_mouse_drag
        window.on_draw=self.on_draw

    def main_loop(self,dt):
        for obj in self._objects.values():
            obj.Loop(dt)
    
    def space(self):
        return self._space

    def run(self):
        pyglet.app.run()

    def on_draw(self):
        batch=pyglet.graphics.Batch()
        pyglet.gl.glClearColor(255, 255, 255, 255)
        self._window.clear()

        for obj in self._objects.values():
            obj.draw(batch)

        for sensor in self._sensors.values():
            if sensor.Show():
                sensor.visualize(batch)

        # draw the HUD 
        for hud in self._hud.values():
            hud.draw(batch)

        batch.draw()

    def update(self,dt):
        
        self.main_loop(dt)

        for sensor in self._sensors.values():
            sensor.pre_solve(dt)

        self._space.step(dt)

        for sensor in self._sensors.values():
            sensor.post_solve(dt)
    
    def get_obj_list(self):
        return self._objects

    def add_hud(self,hud:HUD):
        
        self._hud[hud.name()]=hud

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
            self._objects[obj.Name()]=obj

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
    
    
