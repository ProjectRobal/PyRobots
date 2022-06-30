from .object import Object

class ViObject(Object):
    def __init__(self,name,id,shape):
        super().__init__(name,id)
        self._shape = shape

    def setPosition(self,pos):
        self._shape.position = pos

    def setAnchor(self,anchor):
        self._shape.anchor_x = anchor[0]
        self._shape.anchor_y = anchor[1]

    def setRotation(self,rot):
        self._shape.rotation = rot

    def move(self,vec=None):
        if vec is None:
            return self._shape.position
        self._shape.position[0]+=vec[0]
        self._shape.position[1]+=vec[1]

    def rotate(self,rot=None):
        if rot is None:
            return self._shape.rotation
        self._shape.rotation+=rot

    def anchor(self,anchor=None):
        if anchor is None:
            return (self._shape.anchor_x,self._shape.anchor_y)
        self._shape.anchor_x += anchor[0]
        self._shape.anchor_y += anchor[1]

    def getShape(self):
        return self._shape

    # how to draw object
    def draw(self):
        self._shape.draw()