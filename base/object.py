


class Object:
    '''space - reference to a pymunk space to initialize the object'''
    def __init__(self,name,space):
        self._space=space
        self._name=name

    def Name(self):
        return self._name

    def Scene(self):
        return self._space

    def Body(self):
        raise NotImplementedError()

    def Shape(self):
        raise NotImplementedError()

    
