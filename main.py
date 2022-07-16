import pymunk
import pyglet

from Scene import Scene
from ActionScripts import ActionScripts
from solids.square import Square
from sensors.frictionsensor import FrictionSensor
from sensors.gyrosensor import Gyro
from sensors.distancesensor import DistanceSensor

scene=Scene((0,0))

window = pyglet.window.Window()

sqr=Square("sqr1",1,scene,10,(255,0,0),(40,40))
sqr1=Square("sqr2",2,scene,10,(255,255,0),(10,10))

sqr.setPosition((200,100))
sqr1.setPosition((200,300))


fric=FrictionSensor("fric",1,scene,sqr,0.5)
gyro=Gyro("gyro",2,scene,sqr)

#sensor=DistanceSensor("distance",3,sqr,scene,(0,0,),(0,1,),30,0.5)

scene.add_object(sqr1)
scene.add_object(sqr)

scene.add_sensor(fric)
scene.add_sensor(gyro)

apply_force=False

def main_loop(scene):
    global sqr
    if apply_force:
        sqr.getBody().apply_force_at_local_point((0,0.01),(0,0))

script=ActionScripts(scene,main_loop)


@window.event()
def on_key_press(symbol, modifiers):
    global apply_force
    if symbol == pyglet.window.key.UP:
        apply_force=True
    script.run_press_key(symbol, modifiers)

@window.event()
def on_key_release(symbol, modifiers):
    global apply_force
    if symbol == pyglet.window.key.UP:
        apply_force = False
    script.run_release_key(symbol, modifiers)

@window.event()
def on_mouse_motion(x,y,dx,dy):
    script.run_mouse_move(x,y,dx,dy)

@window.event()
def on_mouse_press(x, y, button, modifiers):
    script.run_mouse_press(x,y,button, modifiers)

@window.event()
def on_mouse_release(x, y, button, modifiers):
    script.run_mouse_release(x,y,button, modifiers)

@window.event()
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    script.run_mouse_drag(x,y,dx,dy,buttons,modifiers)


@window.event()
def on_draw():
    window.clear()
    scene.draw_all()
    

def update(dt):
    scene.update(dt)


pyglet.clock.schedule(update)
pyglet.app.run()

script.stop()