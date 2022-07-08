import pymunk
import pyglet

from Scene import Scene
from ActionScripts import ActionScripts
from solids.square import Square
from solids.terrain import Terrain

scene=Scene((0,0))

window = pyglet.window.Window()

sqr=Square("sqr1",1,10,(255,0,0),(40,40))
sqr1=Square("sqr2",2,10,(255,255,0),(10,10))

sqr.setPosition((200,100))
sqr1.setPosition((200,300))
sqr.getFigure().friction=1
sqr1.getFigure().friction=1
sqr.getFigure().elasticity=1
sqr1.getFigure().elasticity=1

terr1=Terrain("terr1",3,0,0,500,500,1,(0,255,0))

scene.add_object(terr1)
scene.add_object(sqr1)
scene.add_object(sqr)

scene.add_begin(terr1,sqr,terr1.onBegin)
scene.add_begin(terr1,sqr1,lambda x,y,z : False)

scene.add_pre_solve(terr1,sqr,terr1.onPreSolve)


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