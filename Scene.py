# a main class to maintain the GUI and physic engine
import pymunk
import pyglet
from base.viobject import ViObject
from base.phyobject import PhyObject

def always_collide(arbiter,space,data):
        return True

def do_nothing(arbiter,space,data):
        return None

class Scene:
    # win - a reference to the window object to draw on
    def __init__(self,g=(0,-981)):
        self._objects=[]
        self._physic_objects=[]
        self._draw_objects=[]
        self._space=pymunk.Space()
        self._space.gravity =g

    def add_object(self,obj):
        if isinstance(obj,PhyObject):
            self._space.add(obj.getBody(),obj.getFigure())
            self._physic_objects.append(obj)
            self._draw_objects.append(obj)
            self._objects.append(obj)
        elif isinstance(obj,ViObject):
            self._objects.append(obj)
            self._draw_objects.append(obj)

    def remove_object(self,obj):

        if type(obj) is str:
            obj=next((x for x in self._objects if x.name()==obj),None)
        elif type(obj) is int:
            obj=next((x for x in self._objects if x.id()==obj),None)
        
        if obj is None:
            return

        if isinstance(obj,PhyObject):
            self._space.remove(obj.getBody(),obj.getFigure())
            self._physic_objects.remove(obj)
            self._objects.remove(obj)
        elif isinstance(obj,ViObject):
            self._objects.remove(obj)
            self._draw_objects.remove(obj)

    def add_begin(self,obj1,obj2,func=always_collide):
        h=self._space.add_collision_handler(obj1.CollisionClass(),obj2.CollisionClass())

        h.begin=func

    def add_pre_solve(self,obj1,obj2,func=always_collide):
        h=self._space.add_collision_handler(obj1.CollisionClass(),obj2.CollisionClass())

        h.pre_solve=func

    def add_post_solve(self,obj1,obj2,func=do_nothing):
        h=self._space.add_collision_handler(obj1.CollisionClass(),obj2.CollisionClass())

        h.post_solve=func

    def add_separate(self,obj1,obj2,func=do_nothing):
        h=self._space.add_collision_handler(obj1.CollisionClass(),obj2.CollisionClass())

        h.separate=func

    def getStaticBody(self):
        return self._space.static_body

    def draw_all(self):
        for draw in self._draw_objects:
            draw.draw()
    
    def update(self,dt):
        
        self._space.step(dt)

        for phy in self._physic_objects:
            phy.update(self)