from ControlTimer import ControlTimer 

class AlarmFloodTimer(ControlTimer):
    
    def __init__(self):
        
     super().__init__(tps = 10000)
     print("알람홍수모드")