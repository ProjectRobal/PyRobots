'''A class that have set of event function so object can react to them '''
from .object import Object


class EventObject(Object):
    def __init__(self,name,id):
        super().__init__(name,id)

    def run_press_key(self,symbol,modifiers):
        pass
    
    def run_release_key(self,symbol,modifiers):
        pass

    def run_mouse_move(self,x,y,dx,dy):
        pass
    
    def run_mouse_press(self,x,y,button,modifiers):
        pass

    def run_mouse_release(self,x,y,button,modifiers):
        pass

    def run_mouse_drag(self,x,y,dx,dy,button,modifiers):
        pass
        
