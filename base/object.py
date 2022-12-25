

class Object:
    '''space - reference to a pymunk space to initialize the object'''
    def __init__(self,name,space):
        self._space=space
        self._name=name

    def Loop(self,dt):
        pass

    def Name(self):
        return self._name

    def Scene(self):
        return self._space

    def Body(self):
        return None

    def Shape(self):
        return None

    def draw(self,batch):
        pass

    def __del__(self):
        if self.Shape() is not None:
            self.Scene().space().remove(self.Shape()) 
        if self.Body() is not None:
            self.Scene().space().remove(self.Body()) 
    
