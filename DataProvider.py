import random
import time
import uuid
# 트래픽을 생성만 하는 책임을 가지는 클래스
class DataProvider():
    def __init__(self, num_machines = 1000):
        
        self.machine_ids = [f"MCH-{i:04d}" for i in range(num_machines)]
        self.severities = ["INFO", "WARNING", "CRITICAL"]
        self.is_storm_mode = False
        self.total_count=100
        
    def create_packet(self, machine_id, sequence):
     
     event_type = "ALARM" if self.is_storm_mode else random.choice(["NORMAL", "NORMAL", "ALARM"])
    
     return {
        "header": {
            "machine_id": machine_id,
            "packet_id": str(uuid.uuid4())[:8],
            "timestamp": time.time(),
            "sequence": sequence
        },
        "status": {
            "event_type": event_type,
            "severity": random.choice(self.severities) if event_type == "ALARM" else "INFO"
        },
        "payload": {
            "value": round(random.uniform(20.0, 80.0), 2),
            "unit": "Celsius"
        }
        # 산업용 알람과 비슷하게 생긴 딕셔너리
    }
     
    def make_data(self):

        transactions = []
        
        for i in range(self.total_count):
            m_id = self.machine_ids[i % len(self.machine_ids)]
            
            transactions.append(self.create_packet(m_id, i))
            
            
        return transactions #리스트로 한번에 쏨
        
    def stream_data(self):
        for i in range(self.total_count):
            m_id = self.machine_ids[i % len(self.machine_ids)]
            yield self.create_packet(m_id,i) # 하나씩 만들때마다 쏨