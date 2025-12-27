import time
from DataProvider import DataProvider
class ControlTimer:
    def __init__(self, tps):
        self.tps = tps

    def get_interval(self):
        
        return 1.0 / self.tps

    def wait(self):

        time.sleep(self.get_interval())
        
