from base.hud import HUD
from pymunk import Vec2d
import pyglet

class Box:
    def __init__(self,x:int,y:int,w:int,h:int,color=(255,0,0)) -> None:
        self.x=x
        self.y=y
        self.width=w
        self.height=h
        self.color=color

    def point_is_box(self,x:int,y:int)->bool:

        return (x>=self.x) and (x<=self.x+self.width) and (y>=self.y) and (y<=self.y+self.height)

class Board(HUD):
    def __init__(self,name:str,icon:Box,board:Box,childs:list[HUD]=[]):
        super().__init__(name,None)
        self.board=board
        self.icon=icon
        self._childs=childs

        self.active=False
        self._hide()

    def _hide(self):
        for hud in self._childs:
            hud._visible=False

    def _show(self):
        for hud in self._childs:
            hud._visible=True

    def draw(self,batch):

        if self.active:
            self._board=pyglet.shapes.Rectangle(self.board.x,self.board.y,self.board.width,self.board.height,color=self.board.color,batch=batch)
        
        self._icon=pyglet.shapes.Rectangle(self.icon.x,self.icon.y,self.icon.width,self.icon.height,color=self.icon.color,batch=batch)

    def on_mouse_press(self,x,y,button,modifiers):
        pass

    def on_mouse_release(self,x,y,button,modifiers):
        pass

    def on_mouse_motion(self,x,y,dx,dy):
        if self.icon.point_is_box(x,y):
            self.active=True
            self._show()
        else:
            self.active=False
            self._hide()