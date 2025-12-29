import time
import random
class Server:
     def __init__(self, server_id):
        self.server_id = server_id
        self.current_load = 0  # 현재 처리 중인 연결(트랜잭션) 수
        self.total_processed = 0 
        self.total_latency = 0  

     def handle(self, packet):

        start_time = time.time()
        self.current_load += 1
        processing_time = random.uniform(0.001, 0.003)
        time.sleep(processing_time) 
        
        self.current_load -= 1
        self.total_processed += 1
        
        end_time = time.time()
        latency = end_time - start_time
        self.total_latency += latency
        
        return latency