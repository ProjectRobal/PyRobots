'''A base class for sensor they would have the reference for object ( obj in constructor ) and would activate before and 
after pymunk update ( function pre_solve and post_solve )'''

class Sensor:
    def __init__(self,name,id,scene,obj):
        self._name=name
        self._id = id
        self._obj = obj
        self._scene= scene

    def getScene(self):
        return self._scene

    def getName(self):
        return self._name
    
    def getId(self):
        return self._id

    def getObject(self):
        return self._obj

    def pre_solve(self,scene,dt):
        raise NotImplementedError()

    def post_solve(self,scene,dt):
        raise NotImplementedError()