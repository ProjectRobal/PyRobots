from base.sensor import Sensor
from pymunk.vec2d import Vec2d
import pymunk
from pyglet import shapes

class HoleSensor(Sensor):
    def __init__(self,name,space,obj,pos,id=5):
        super().__init__(name,space,obj)
        self._pos=pos
        self._start=pos
        self._touch=False
        self.color=(255,0,0)
        self._id=id
        self._distance=10

    def visualize(self, batch):
        self.point=shapes.Circle(self._start[0],self._start[1],5,color=self.color,batch=batch)        

    def isTouchingHole(self):
        return self._distance>10

    def Distance(self):
        return self._distance

    def pre_solve(self, dt):
        pass

    def post_solve(self, dt):
        self._start=self._obj.Body().local_to_world(self._pos)

        info=self._space.point_query(self._start,10,pymunk.ShapeFilter())

        for i in info:
            if i.shape is not None:
                if i.shape.collision_type == self._id:
                    self._distance=8160
                    self.color=(0,255,0)
                    return
                break
        
        self._distance=10
        self.color=(255,0,0)
        
