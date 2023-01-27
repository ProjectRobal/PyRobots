from base.hud import HUD
from pymunk import Vec2d
import pyglet

class Label(HUD):
    def __init__(self,name:str,value,pos:Vec2d):
        super().__init__(name,value)
        self._pos=pos
        self._size=36
        self._color=(0,0,0,255)
        self._background=(255,255,255,255)

    def draw(self,batch):
        self.text=pyglet.text.Label(str(self.value()),font_size=self._size,x=self._pos[0],y=self._pos[1],batch=batch)
        self.text.color=self._color

    def size(self,size=None|int):
        if size is None:
            return self._size

        self._size=size

    def background(self,color=None):
        if color is None:
            return self._background

        self._background=color

    def color(self,color=None):
        if color is None:
            return self._color

        self._color=color