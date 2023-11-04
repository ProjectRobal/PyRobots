from concurrent import futures
import grpc
import _grpc.rc_service_pb2 as rc_service_pb2
from _grpc.rc_service_pb2 import Message,_None,Gyroscope,DistanceSensor,AudioChunk
import _grpc.rc_service_pb2_grpc as rc_service_pb2_grpc

class RCRobotServicer(rc_service_pb2_grpc.RCRobotServicer):
    def __init__(self,manager):
        self._manager = manager
        self._status=0
        self._message=""
    
    def UpdateParams(self,params):
        self._manager.UpdateParams("Motors",{"speedA":params.mA.speed,"directionA":params.mA.direction,"speedB":params.mB.speed,"directionB":params.mB.direction})

        self._manager.UpdateParams("Servos",{"pwm0":params.ear1.angle,"pwm1":params.ear2.angle})      

    def PackageData(self):
        self._message=str(self._message)
        data=self._manager.getParamsList("Gyroscope")
        gyro=Gyroscope()
        try:
            gyro=Gyroscope()
            gyro.acceleration[:]=data["acceleration"]
            gyro.gyroscope[:]=data["gyroscope"]
            gyro.accel_range=data["accel_range"]
            gyro.gyro_range=data["gyro_range"]
        except:
            self._status=-1
            self._message+=" No device Gyroscope"    
        data=self._manager.getParamsList("Distance_Front")
        front=DistanceSensor()

        try:
                front=DistanceSensor(distance=data["distance"])
        except:
            self._status=-1
            self._message+=" No front Sensor"  

        data=self._manager.getParamsList("Distance_Floor")
        floor=DistanceSensor()

        front1=DistanceSensor()

        try:
                front1=DistanceSensor(distance=data["distance1"])
        except:
            self._status=-1
            self._message+=" No front Sensor"  

        data=self._manager.getParamsList("Distance_Floor")
        floor=DistanceSensor()

        try:
                floor=DistanceSensor(distance=data["distance"])
        except:
            self._status=-1
            self._message=" No floor Sensor"  
        
        data=self._manager.getParamsList("Ears")
        left=AudioChunk()
        right=AudioChunk()

        try:
            left=AudioChunk()
            left.data[:]=data["channel1"]
            right=AudioChunk()
            right.data[:]=data["channel2"]
        except:
            self._status=-1
            self._message=" No audio device"
        
        msg=Message(front=front,front1=front1,floor=floor, left=left, right=right,gyroscope=gyro,status=self._status,message=self._message)

        print(msg)
        return msg


    def Process(self,request, context):
        
        try:

            self.UpdateParams(request)

            self._manager.loop()

        except errors.DeviceCriticalError as e:
            print(e)
            self._message=str(e)
            self._code=e.code
            self._manager.EmergencyDetach(e.name)
        except errors.GeneralDeviceError as e:
            print(e)
            self._message=str(e)
            self._code=e.code
        except Exception as e:
            self._message=e
            self._code=-98
        except:
            self._message="Some errors"
            self._code=-99
        finally:

            return self.PackageData()



    def SendCommand(self,request,context):
        try:
        
            self.UpdateParams(request)

            self._manager.loop()
        except errors.DeviceCriticalError as e:
            print(e)
            self._message=e
            self._code=e.code
            self._manager.EmergencyDetach(e.name)
        except errors.GeneralDeviceError as e:
            print(e)
            self._message=e
            self._code=e.code
        except Exception as e:
            self._message=e
            self._code=-98
        except:
            self._message="Some errors"
            self._code=-99

        return _None()
    
    def ReadData(self, request, context):

        return self.PackageData()



def run(manager):
    server= grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    rc_service_pb2_grpc.add_RCRobotServicer_to_server(
        RCRobotServicer(manager),server
    )
    server.add_insecure_port('172.0.0.1:5051')
    server.start()
    server.wait_for_termination()