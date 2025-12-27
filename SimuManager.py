from DataProvider import DataProvider
from NormalTimer import NormalTimer
from AlarmFloodTimer import AlarmFloodTimer
from LoadBalancer import LoadBalancer
import time
class SimulationManager:
    def __init__(self):
      
        self.provider = DataProvider(num_machines=1000)
        self.load_balancer = LoadBalancer()
        self.timer1 = NormalTimer()
        self.timer2 = AlarmFloodTimer()
        
    def start(self, total_count):
        print(f"시뮬레이션 시작 (목표: {total_count}개)")
        self.start_time = time.time()
        
        for packet in self.provider.stream_data(total_count):
            
            self.load_balancer.receive(packet)
            self.timer2.wait()

        self.end_time = time.time()
        
        print("[최종 실험 결과]")
        self.calculate_latency(total_count)
        
        
    def calculate_latency(self, total_count):
        duration_sec = self.end_time - self.start_time
        duration_ms = duration_sec * 1000
        avg_latency = duration_ms / total_count if total_count > 0 else 0
        
        print("\n"+ "="*20 + " 실험 결과 분석 " + "="*20)
        print(f"✔️ 총 처리 패킷: {total_count:,} 개")
        print(f"⏱️ 총 소요 시간: {duration_ms:,.2f} ms")
        print(f"⏱️ 패킷당 평균 시간: {avg_latency:.4f} ms")
        print("="*55 + "\n")
        
        return duration_ms
        