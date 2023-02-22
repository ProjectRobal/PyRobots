from base.sensor import Sensor
import numpy as np

import pyglet
import pymunk


class Microphone(Sensor):
    def __init__(self, name, space, obj,pos:pymunk.Vec2d):
        super().__init__(name, space, obj)
        self._pos=pos
        self._start=pos
        self._buffer=np.zeros(32000,dtype=np.int32)

    def post_solve(self, dt):
        self._start=self.getObject().Body().local_to_world(self._pos)

    def getPosition(self):
        return self._start

    def visualize(self, batch):
        self.point=pyglet.shapes.Circle(self._start[0],self._start[1],5,
        color=(229, 70, 250,255),batch=batch)

    def Buffer(self,buffer=None):
        if buffer is None:
            return self._buffer
        
        self._buffer=np.array(buffer,dtype=np.int32)
