from .viobject import ViObject



class PhyObject(ViObject):
    ''' name - a name of the object, id - a id of the object ,
     body - pymug physic body
     fig - a shape representation of the body in pymug
     '''
    def __init__(self,name,id,shape,body,fig):
        super().__init__(name,id,shape)
        self._body = body
        self._fig = fig

    def setPosition(self,pos):
        self._body.position = pos

    def setAnchor(self,anchor):
        self._body.center_of_gravity=anchor

    def setRotation(self,rot):
        self._body.angle = rot

    def move(self,vec=None):
        if vec is None:
            return self._body.position
        self._body.position[0]+=vec[0]
        self._body.position[1]+=vec[1]
    
    def rotate(self,rot=None):
        if rot is None:
            return self._body.angle
        self._body.angle+=rot

    def anchor(self,anchor=None):
        if anchor is None:
            return self._body.center_of_gravity
        self._body.center_of_gravity[0]+=anchor[0]
        self._body.center_of_gravity[1]+=anchor[1]


    def getShape(self):
        return self._shape

    def getBody(self):
        return self._body

    def getFigure(self):
        return self._fig
    
    ''' a function that return collison class id'''
    def CollisionClass(self):
        raise NotImplementedError()

    '''
        a function called after pymunk cycle
    '''
    def update(self,space):
        
        self._shape.anchor_x = self._body.center_of_gravity[0]
        self._shape.anchor_y = self._body.center_of_gravity[1]
        self._shape.position = self._body.position
        self._shape.rotation = self._body.angle