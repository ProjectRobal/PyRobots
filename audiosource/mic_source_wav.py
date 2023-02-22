from base.object import Object
from sensors.microphone import Microphone

import pymunk
import pyglet

import pyaudio
import wave

import math

import numpy as np

CHUNK=32000
RATE=16000
CHANNELS=1

class MicSourceWAV(Object):

    SYMBOL_SIZE=10

    '''Audio source from microphone
    recivers - a microphones that will recive audio data
    damping - a dumping force applied to audio signal
    '''
    def __init__(self, name, space,filename:str,x:int,y:int,recivers,damping=1):
        super().__init__(name, space)

        self._recivers=recivers
        self._damping=damping
        self.m_pos=pymunk.Vec2d(x,y)

        self.source=wave.open(filename,"rb")

        # audio source

        #self.audio=pyaudio.PyAudio()

        #self.source=self.audio.open(RATE,CHANNELS,pyaudio.paInt16,input=True,frames_per_buffer=CHUNK,input_device_index=3)

    def Loop(self,dt):

        data=np.fromstring(self.source.readframes(CHUNK),dtype=np.int16)

        if data.size==0:
            self.source.rewind()
            return

        for rec in self._recivers:
            if isinstance(rec,Microphone):
                _pos=rec.getPosition()

                distance=abs(_pos-self.m_pos)

                output=np.array([],dtype=np.int32)

                for d in data:
                    output=np.append(output,int(d*math.exp(-self._damping*float(distance))))

                input=rec.Buffer()

                rec.Buffer(np.add(input,output,np.int32))

    def draw(self,batch):
        self._mic=pyglet.shapes.Triangle(self.m_pos.x-self.SYMBOL_SIZE,self.m_pos.y-self.SYMBOL_SIZE,self.m_pos.x+self.SYMBOL_SIZE,self.m_pos.y-self.SYMBOL_SIZE,
                                         self.m_pos.x,self.m_pos.y+self.SYMBOL_SIZE,color=(168,52,235,255),batch=batch)
