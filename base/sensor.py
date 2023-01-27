'''A base class for sensor they would have the reference for object ( obj in constructor ) and would activate before and 
after pymunk update ( function pre_solve and post_solve )'''

class Sensor:
    def __init__(self,name,space,obj):
        self._obj = obj
        self._name = name
        self._space= space
        self._show=False

    def Show(self,s=None):
        if s is None:
            return self._show

        self._show = s

    def Name(self):
        return self._name

    def Space(self):
        return self._space

    def getObject(self):
        return self._obj

    def pre_solve(self,dt):
        pass

    def post_solve(self,dt):
        pass

    def visualize(self,batch):
        pass