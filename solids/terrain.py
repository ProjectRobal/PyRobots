from base.phyobject import PhyObject
import pymunk
import pyglet
import math

class Terrain(PhyObject):
    def __init__(self,name,id,x,y,width,height,friction,color=(0,0,0,0)):
        body=pymunk.Body(0,0,pymunk.Body.STATIC)
        coordinates=((0,0),(width,0),(width,height),(0,height),)
        poly=pymunk.Poly(body,coordinates)
        shape=pyglet.shapes.Rectangle(0,0,width,height,color=color)
        body.sensor=True
        body.friction=friction
        poly.collision_type=id
        super().__init__(name,id,shape,body,poly)
        self.setPosition((x,y))

    def CollisionClass(self):
        return self.id()

    def onBegin(self,arbiter,space,data):
        return True

    def onPreSolve(self,arbiter,space,data):
        shape1=arbiter.shapes[1]
        vel=math.sqrt((shape1.body.velocity[0]**2) + (shape1.body.velocity[1]**2))
        if vel==0:
            return False
        direction=(shape1.body.velocity[0]/vel,shape1.body.velocity[1]/vel)

        firc=arbiter.friction
        
        gforce=9.81*shape1.body.mass
        
        shape1.body.apply_force_at_local_point((-direction[0]*gforce,-direction[1]*gforce),(0,0))
        return False

