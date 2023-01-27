
# A base class for controls of HUD.
from copy import copy

class HUD:
    '''value - a value which will be shown in the HUD'''
    def __init__(self,name:str,value):
        self._value = value
        self._name = name

    def name(self):
        return self._name

    '''retrive a value from the HUD'''
    def value(self):
        if callable(self._value):
            return self._value()

        return self._value

    '''How to display the value'''
    def draw(self,batch):
        raise NotImplementedError()