
class Object:
    '''name a name of the object,
    id a id of the object,
    scene a reference to the scene object'''
    def __init__(self,name,id,scene):
        self._name = name
        self._id = id
        self._scene = scene
    
    def name(self):
        return self._name
    
    def id(self):
        return self._id

    def Scene(self):
        return self._scene

    def onAdd(self,scene):
        pass

    
