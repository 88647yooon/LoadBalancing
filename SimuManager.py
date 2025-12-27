from DataProvider import DataProvider
from NormalTimer import NormalTimer
from AlarmFloodTimer import AlarmFloodTimer
from LoadBalancer import LoadBalancer
class SimulationManager:
    def __init__(self):
        # 1. 필요한 부품들을 여기서 다 만듭니다.
        self.provider = DataProvider(num_machines=1000)
        self.load_balancer = LoadBalancer() # (곧 만드실 클래스)
        
        # 2. 처음에는 일반 타이머로 시작합니다.
        self.timer1 = NormalTimer()
        self.timer2 = AlarmFloodTimer()
        
    def start(self, total_count=1000000):
        print(f"시뮬레이션 시작 (목표: {total_count}개)")
        
        # 데이터를 하나씩 생성해서 로드밸런서로 보냅니다.
        for packet in self.provider.stream_data():
            
            # [연결 지점] 로드밸런서에게 데이터를 던져줍니다.
            self.load_balancer.receive(packet)
            
            # 타이머 박자에 맞춰 쉽니다.
            self.timer.wait()
            
            # (선택 사항) 특정 조건에서 타이머를 교체하는 로직도 여기 넣을 수 있습니다.
            # if 상황 == "위급": self.timer = AlarmFloodTimer()

        print("시뮬레이션 완료")