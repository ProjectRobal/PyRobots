from base.eventobject import EventObject
from sensors.microphone import Microphone

import pymunk
import pyglet

import pyaudio

import math

import numpy as np

CHUNK=32000
RATE=16000
CHANNELS=1

class MicSource(EventObject):

    '''Audio source from microphone
    recivers - a microphones that will recive audio data
    '''
    def __init__(self, name, space,recivers,damping=1):
        super().__init__(name, space)

        self._recivers=recivers
        self._damping=damping

        # audio source

        self.audio=pyaudio.PyAudio()

        self.source=self.audio.open(RATE,CHANNELS,pyaudio.paInt16,input=True,frames_per_buffer=CHUNK,input_device_index=3)

    def run_mouse_press(self,x,y,button,modifiers):
        
        if button==pyglet.window.mouse.LEFT:
            m_pos=pymunk.Vec2d(x,y)

            data=np.fromstring(self.source.read(CHUNK),dtype=np.int16)

            for rec in self._recivers:
                if isinstance(rec,Microphone):
                    _pos=rec.getPosition()

                    distance=abs(_pos-m_pos)

                    output=np.array([],dtype=np.int16)

                    for d in data:
                        output=np.append(output,d*math.exp(-self._damping*float(distance)))

                    rec.Buffer(output)

                    

