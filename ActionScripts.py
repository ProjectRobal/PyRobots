'''A class to handle user inputs or others scripts that are going to run in the background'''
import threading


class ActionScripts:
    '''loop - main loop function, scene - reference to Scene objects'''
    def __init__(self,scene,loop=None,_start=True):
        self._loop = loop
        self._scene = scene
        self._thread = threading.Thread(None,self.main_loop,"action1")
        self._run=False
        if _start:
            self.start()
        self._press=None
        self._release=None
        self._mouse_drag=None
        self._mouse_motion=None
        self._mouse_release=None
        self._mouse_press=None

    def alter_main_loop(self,loop):
        self._run=False
        self._thread.join()
        self._loop=loop

    def add_press_keyboard(self,press):
        self._press = press
    
    def add_release_keyboard(self,release):
        self._release = release

    def add_mouse_motion(self,motion):
        self._mouse_motion = motion
    
    def add_mouse_press(self,press):
        self._mouse_press = press

    def add_mouse_release(self,release):
        self._mouse_release = release

    def add_mouse_drag(self,drag):
        self._mouse_drag = drag



    def run_press_key(self,symbol,modifiers):
        if self._press is not None:
            self._press(self._scene,symbol,modifiers)
    
    def run_release_key(self,symbol,modifiers):
        if self._release is not None:
            self._release(self._scene,symbol,modifiers)

    def run_mouse_move(self,x,y,dx,dy):
        if self._mouse_motion is not None:
            self._mouse_motion(self._scene,x,y,dx,dy)
    
    def run_mouse_press(self,x,y,button,modifiers):
        if self._mouse_press is not None:
            self._mouse_press(self._scene,x,y,button,modifiers)

    def run_mouse_release(self,x,y,button,modifiers):
        if self._mouse_release is not None:
            self._mouse_release(self._scene,x,y,button,modifiers)

    def run_mouse_drag(self,x,y,dx,dy,button,modifiers):
        if self._mouse_drag is not None:
            self._mouse_drag(self._scene,x,y,dx,dy,y,button,modifiers)
        
    def start(self):
        self._run=True
        self._thread.start()
        print("Thread started")
    
    def main_loop(self):
        if self._loop is None:
            return
        while self._run:
            self._loop(self._scene)

    def stop(self):
        self._run = False
        self._thread.join()
