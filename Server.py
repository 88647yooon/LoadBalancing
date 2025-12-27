import time
import random
class Server:
     def __init__(self, server_id):
        self.server_id = server_id
        self.current_load = 0  # 현재 처리 중인 연결(트랜잭션) 수
        self.total_processed = 0 # 총 처리한 패킷 수
        self.total_latency = 0   # 총 지연 시간 합계

     def handle(self, packet):
        # 1. 처리 시작 (부하 증가)
        start_time = time.time()
        self.current_load += 1
        
        # 2. 작업 처리 시뮬레이션 
        # 성능이 같으므로 모든 서버가 동일한 범위(예: 0.001~0.003초) 내에서 랜덤하게 처리한다고 가정합니다.
        processing_time = random.uniform(0.001, 0.003)
        time.sleep(processing_time) # 실제 실험 시 1,00만 개를 하려면 이 부분을 조정해야 합니다.
        
        # 3. 처리 완료 (부하 감소)
        self.current_load -= 1
        self.total_processed += 1
        
        # 4. 성능 측정
        end_time = time.time()
        latency = end_time - start_time
        self.total_latency += latency
        
        return latency