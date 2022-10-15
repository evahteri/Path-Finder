from performance_tests.dijkstra_performance_test import Dijkstra_Performance

class PerformanceTest():

    def __init__(self):
        pass

    def test_performance(self):
        dijkstra_time = Dijkstra_Performance().test_dijkstra_100_times_small_map()
        print(f"Dijkstra found 100 routes in 10x10 map in {dijkstra_time} seconds")
