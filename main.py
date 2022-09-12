from typing import Tuple

import pymunk
import pymunk.pyglet_util
import pyglet

from base.object import Object
from base.eventobject import EventObject

from sensors.frictionsensor import FrictionSensor
from sensors.gyrosensor import Gyro
from sensors.distancesensor import DistanceSensor

window = pyglet.window.Window()

space=pymunk.Space()

space.gravity=(0,0)

options=pymunk.pyglet_util.DrawOptions()

space.debug_draw(options)

class Rect(Object):
    def __init__(self,name,space,size:Tuple[int,int]):
        super().__init__(name,space)
        
        self.body=pymunk.Body(1,10)
        self.shape=pymunk.Poly(self.body,[(0,0),(size[0],0),size,(0,size[1])])

        space.add(self.body,self.shape)

    def Body(self):
        return self.body
    
    def Shape(self):
        return self.shape
        

rect1=Rect("rect1",space,(50,50))



rect1.body.position=(100,100)

sensors=[]

sensors.append(FrictionSensor("gric",space,rect1,0.5))

# a list with pymunk objects
objects=[]


def main_loop():
    pass

@window.event()
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.UP:
        rect1.Body().apply_force_at_local_point((0,400),(0,0))

    for obj in objects:
        if isinstance(obj,EventObject):
            obj.run_press_key(symbol, modifiers)

@window.event()
def on_key_release(symbol, modifiers):
    global apply_force
    if symbol == pyglet.window.key.UP:
        apply_force = False

    for obj in objects:
        if isinstance(obj,EventObject):
            obj.run_release_key(symbol, modifiers)

@window.event()
def on_mouse_motion(x,y,dx,dy):
    for obj in objects:
        if isinstance(obj,EventObject):
            obj.run_mouse_move(x,y,dx,dy)

@window.event()
def on_mouse_press(x, y, button, modifiers):
    for obj in objects:
        if isinstance(obj,EventObject):
            obj.run_mouse_press(x,y,button, modifiers)

@window.event()
def on_mouse_release(x, y, button, modifiers):
    for obj in objects:
        if isinstance(obj,EventObject):
            obj.run_mouse_release(x,y,button, modifiers)

@window.event()
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    for obj in objects:
        if isinstance(obj,EventObject):
            obj.run_mouse_drag(x,y,dx,dy,buttons,modifiers)

@window.event()
def on_draw():
    pyglet.gl.glClearColor(255, 255, 255, 255)
    window.clear()
    space.debug_draw(options)
    

def update(dt):

    main_loop()
    
    for s in sensors:
        s.pre_solve(dt)

    space.step(dt)

    for s in sensors:
        s.post_solve(dt)

pyglet.clock.schedule_interval(update,0.01)
pyglet.app.run()

