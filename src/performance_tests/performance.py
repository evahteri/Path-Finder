from performance_tests import ida_star_performance_test
from performance_tests.dijkstra_performance_test import Dijkstra_Performance
from performance_tests.ida_star_performance_test import IdaStar_Performance

class PerformanceTest():
    """This class tests performance of both algorithms
    """

    def __init__(self):
        pass

    def test_performance_small_map(self):
        """Tests 100 random routes through 10x10 map with walls.
        After testing, the time difference is counted.
        """
        dijkstra_time = Dijkstra_Performance().test_dijkstra_100_times_small_map()
        ida_star_time = IdaStar_Performance().test_ida_star_100_times_small_map()
        print(f"Dijkstra found 100 routes in 10x10 map in {dijkstra_time} seconds")
        print(f"IDA* found 100 routes in 10x10 map in {ida_star_time} seconds")
        difference = abs(dijkstra_time - ida_star_time)
        if dijkstra_time > ida_star_time:
            print(f"IDA* star was faster by {difference}")
            return ("IDA*", difference)
        else:
            print(f"Dijkstra star was faster by {difference}")
            return ("Dijkstra", difference)
