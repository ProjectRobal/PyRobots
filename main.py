import pymunk
import pyglet

from Scene import Scene
from solids.square import Square

scene=Scene((0,-100))

window = pyglet.window.Window()

sqr=Square("sqr1",1,10,(255,0,0),(40,40))
sqr1=Square("sqr2",2,10,(255,255,0),(10,10))

sqr.setPosition((50,100))
sqr1.setPosition((50,300))
sqr.getFigure().friction=1
sqr1.getFigure().friction=1
sqr.getFigure().elasticity=1
sqr1.getFigure().elasticity=1

scene.add_object(sqr1)
scene.add_object(sqr)

seg=pymunk.Segment(scene.getStaticBody(),(0,0),(200,0),2)
seg.friction=1

seg1=pymunk.Segment(scene.getStaticBody(),(0,0),(0,800),2)
seg1.friction=1

scene._space.add(seg)
scene._space.add(seg1)


@window.event()
def on_draw():
    window.clear()
    scene.draw_all()
    

def update(dt):
    scene.update(dt)


pyglet.clock.schedule(update)
pyglet.app.run()