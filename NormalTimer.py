from ControlTimer import ControlTimer
 
class NormalTimer(ControlTimer):
   
    def __init__(self):

     super().__init__(tps = 10)
     print("일반모드")