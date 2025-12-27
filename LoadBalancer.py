import threading
import random
from Server import Server
class LoadBalancer:
    def __init__(self, num_servers=3):
        # 1. 로드밸런서가 관리할 서버들을 만듭니다.
        self.servers = [Server(f"Server-{i}") for i in range(num_servers)]

    def receive(self, packet):
        """TransactionGenerator로부터 패킷을 받는 입구"""
        # 2. 알고리즘을 통해 최적의 서버를 고릅니다.
        target_server = self.get_least_connection_server()
        
        thread = threading.Thread(target=target_server.handle, args=(packet,))
        thread.start()

    def get_least_connection_server(self):
     # 1. 현재 최소 부하가 얼마인지 찾습니다.
     min_load = min(s.current_load for s in self.servers)
    
     # 2. 최소 부하를 가진 서버들을 '모두' 리스트에 담습니다.
     least_loaded_servers = [s for s in self.servers if s.current_load == min_load]
    
     # 3. 최소 부하 서버가 여러 대라면 그중 하나를 랜덤하게 골라 반환합니다.
     return random.choice(least_loaded_servers)
    
    def display_stats(self):
        """현재 모든 서버의 누적 처리량과 부하 상태를 출력합니다."""
        print("\n" + "="*50)
        print(f"{'Server Name':^15} | {'Total Processed':^15} | {'Current Load':^12}")
        print("-" * 50)
        
        for server in self.servers:
            print(f"{server.server_id:^15} | {server.total_processed:^15,} | {server.current_load:^12}")
        print("="*50 + "\n")