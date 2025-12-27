import time
from DataProvider import DataProvider
class ControlTimer:
    def __init__(self, tps):
        self.tps = tps

    def get_interval(self):
        """초당 전송량(TPS)을 바탕으로 간격을 계산합니다."""
        return 1.0 / self.tps

    def wait(self):
        """계산된 간격만큼 대기합니다."""
        time.sleep(self.get_interval())
        
        #로드밸런서가 무너지는 지점을 찾으려면 TPS를 아주 높게 잡아야 합니다. 
        # 예: 초당 1,000개, 5,000개, 10,000개 식으로 올려보며 어느 지점에서 응답 속도가 느려지는지 확인합니다.