'''

    Kapibara Control Network

'''

from .control import network
from .control import layer
from .control import BreedStrategy

import grpc
from _grpc.rc_service_pb2 import Message,_None,Gyroscope,DistanceSensor,AudioChunk
import _grpc.rc_service_pb2_grpc as rc_service_pb2_grpc

from timeit import default_timer

import numpy as np

class Mind:
    def __init__(self) -> None:
        '''

            Networks inputs:
            32x32 spectogram, 2 audio coefficient, 3 accelerator, 3 gyroscope, 2 front sensors, 
            1 floor sensors, 1 direction of second network, 1 motor power output of second network 
            = 1038

            Output size:
            1 direction of motor. 1 motor power output
        '''

        self.input_buf=np.ndarray(1038,np.float64)
        self.last_output_left=np.ndarray(2,dtype=np.float64)
        self.last_output_right=np.ndarray(2,dtype=np.float64)

        self.eval:float=0.0

        self.left_network=network.Network(1038)
        self.left_network.addLayer(256,16,layer.RecurrentLayer)
        self.left_network.addLayer(2,8,layer.RecurrentLayer)

        self.right_network=network.Network(1038)
        self.right_network.addLayer(256,16,layer.RecurrentLayer)
        self.right_network.addLayer(2,8,layer.RecurrentLayer)

        self.left_network.setTrendFunction(self.trend)
        self.right_network.setTrendFunction(self.trend)

    def step(self,msg:np.ndarray)->float:
        '''

            Returns time step

        '''

        start=default_timer()
        
        self.input_buf[:1035]=msg[:]

        self.input_buf[1036:]=self.last_output_right[:]

        self.last_output_left=self.left_network.step(self.input_buf)

        self.input_buf[:1035]=msg[:]

        self.input_buf[1036:]=self.last_output_left[:]

        self.last_output_right=self.right_network.step(self.input_buf)

        return default_timer()-start

    
    def trend(self,eval:float,network:network.Network)->float:
        
        return self.eval