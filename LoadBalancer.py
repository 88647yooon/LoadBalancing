import threading
import random
from Server import Server
class LoadBalancer:
    def __init__(self, num_servers=3):
        self.servers = [Server(f"Server-{i}") for i in range(num_servers)]

    def receive(self, packet):
        
        target_server = self.get_least_connection_server()
        thread = threading.Thread(target=target_server.handle, args=(packet,))
        thread.start()

    def get_least_connection_server(self):

     min_load = min(s.current_load for s in self.servers)
     least_loaded_servers = [s for s in self.servers if s.current_load == min_load]
    
     return random.choice(least_loaded_servers)
    
    def display_stats(self):

        print("\n" + "="*50)
        print(f"{'Server Name':^15} | {'Total Processed':^15} | {'Current Load':^12}")
        print("-" * 50)
        
        for server in self.servers:
            print(f"{server.server_id:^15} | {server.total_processed:^15,} | {server.current_load:^12}")
        print("="*50 + "\n")