from base.hud import HUD
import pyglet
import math

class GaugeDesign:
    def __init__(self,arrow_color=(255,0,0),background_color=(255,255,255),outline_color=(0,0,0),radius:int=10) -> None:
        self.arrow_color=arrow_color
        self.background_color=background_color
        self.outline_color=outline_color
        self.radius=radius

class Gauge(HUD):
    def __init__(self, name: str, value,x:int,y:int,min:float,max:float,min_angel:float=0,max_angel:float=360,design:GaugeDesign=GaugeDesign()):
        super().__init__(name, value)
        self.min=min
        self.max=max
        self.design=design
        self.x=x
        self.y=y
        self.min_angel=min_angel
        self.max_angel=max_angel

    def draw(self,batch):
        value=self.value()

        self.background=pyglet.shapes.Circle(self.x,self.y,self.design.radius,color=self.design.background_color,batch=batch)
        self.outline=pyglet.shapes.Arc(self.x,self.y,self.design.radius,color=self.design.outline_color,batch=batch)

        angel=(((value-self.min)/(self.max-self.min))*(self.max_angel-self.min_angel)) + self.min_angel

        angel=angel*(math.pi/180.0)

        self.x_1=self.x+self.design.radius*math.cos(angel)
        self.y_1=self.y+self.design.radius*math.sin(angel)

        self.arrow=pyglet.shapes.Line(self.x,self.y,self.x_1,self.y_1,4,self.design.arrow_color,batch=batch)
    


