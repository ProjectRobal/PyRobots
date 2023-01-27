from base.sensor import Sensor

import pyglet

class Microphone(Sensor):
    def __init__(self, name, space, obj,pos):
        super().__init__(name, space, obj)
        self._pos=pos
        self._start=pos

    def post_solve(self, dt):
        
        self._start=self.getObject().Body().local_to_world(self._pos)


    def getPosition(self):
        return self._start


    def visualize(self, batch):
        self.point=pyglet.shapes.Circle(self._start[0],self._start[1],4,
        color=(229, 70, 250,255),batch=batch)