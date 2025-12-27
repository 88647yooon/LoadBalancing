from SimuManager import SimulationManager

if __name__ == "__main__":
    # 1. 매니저(공장장)를 생성합니다.
    manager = SimulationManager()
    
    # 2. 시뮬레이션 시작 (테스트를 위해 우선 1,000개만 먼저 해보세요)
    # 잘 돌아가는지 확인 후 1,000,000으로 늘리는 것을 추천합니다.
    manager.start(total_count=100000)
    
    # 3. 서버별 통계 출력 (LoadBalancer에 display_stats 함수를 만드셨다면)
    manager.load_balancer.display_stats()