from DataProvider import DataProvider
from NormalTimer import NormalTimer
from AlarmFloodTimer import AlarmFloodTimer
from LoadBalancer import LoadBalancer
import time
class SimulationManager:
    def __init__(self):
        # 1. 필요한 부품들을 여기서 다 만듭니다.
        self.provider = DataProvider(num_machines=1000)
        self.load_balancer = LoadBalancer() # (곧 만드실 클래스)
        
        # 2. 처음에는 일반 타이머로 시작합니다.
        self.timer1 = NormalTimer()
        self.timer2 = AlarmFloodTimer()
        
    def start(self, total_count):
        print(f"시뮬레이션 시작 (목표: {total_count}개)")
        self.start_time = time.time()
        
        # 데이터를 하나씩 생성해서 로드밸런서로 보냅니다.
        for packet in self.provider.stream_data(total_count):
            
            self.load_balancer.receive(packet)
            self.timer2.wait()

        self.end_time = time.time()
        
        print("[최종 실험 결과]")
        self.calculate_latency(total_count)
        
        
    def calculate_latency(self, total_count):
        duration_sec = self.end_time - self.start_time
        duration_ms = duration_sec * 1000
        
        # 0으로 나누기 방지
        avg_latency = duration_ms / total_count if total_count > 0 else 0
        
        print("\n"+ "="*20 + " 실험 결과 분석 " + "="*20)
        print(f"✔️ 총 처리 패킷: {total_count:,} 개")
        print(f"⏱️ 총 소요 시간: {duration_ms:,.2f} ms")
        print(f"⏱️ 패킷당 평균 시간: {avg_latency:.4f} ms")
        print("="*55 + "\n")
        
        return duration_ms
        