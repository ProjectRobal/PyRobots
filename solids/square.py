from base.phyobject import PhyObject
import pymunk
import pyglet

class Square(PhyObject):
    def __init__(self,name,id,scene,mass=10,color=(255,255,255),size=(25,25)):
        moment=pymunk.moment_for_box(mass,size)
        body=pymunk.Body(mass,moment)
        coordinates=((0,0),(size[0],0),(size[0],size[1]),(0,size[1]))
        poly=pymunk.Poly(body,coordinates)
        shape=pyglet.shapes.Rectangle(0,0,size[0],size[1],color=color)
        poly.collision_type=id
        super().__init__(name,id,scene,shape,body,poly)

    def CollisionClass(self):
        return self.id()