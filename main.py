from SimuManager import SimulationManager

if __name__ == "__main__":

    manager = SimulationManager()
    manager.start(total_count=100000)
    manager.load_balancer.display_stats()