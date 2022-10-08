

class Object:
    '''space - reference to a pymunk space to initialize the object'''
    def __init__(self,name,space):
        self._space=space
        self._name=name

    def Loop(self):
        pass

    def Name(self):
        return self._name

    def Scene(self):
        return self._space

    def Body(self):
        raise NotImplementedError()

    def Shape(self):
        raise NotImplementedError()

    def __del__(self):
        self.Scene().space().remove(self.Body(),self.Shape()) 
    
