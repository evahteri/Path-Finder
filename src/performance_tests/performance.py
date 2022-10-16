from performance_tests import ida_star_performance_test
from performance_tests.dijkstra_performance_test import Dijkstra_Performance
from performance_tests.ida_star_performance_test import IdaStar_Performance


class PerformanceTest():
    """This class tests performance of both algorithms
    """

    def __init__(self):
        pass

    def test_performance_10x10_map(self):
        """Tests 100 random routes through 10x10 map with walls.
        After testing, the time difference is counted.
        """
        dijkstra_time = Dijkstra_Performance().test_dijkstra_100_times_10x10_map()
        ida_star_time = IdaStar_Performance().test_ida_star_100_times_10x10_map()
        print(
            f"Dijkstra found 100 routes in 10x10 map in {dijkstra_time.microseconds} microseconds")
        print(f"IDA* found 100 routes in 10x10 map in {ida_star_time.microseconds} microseconds")
        difference_time = abs(dijkstra_time - ida_star_time)
        if dijkstra_time > ida_star_time:
            difference_percentage = round(
                (difference_time / dijkstra_time * 100), 2)
            print(
                f"IDA* star was faster by {difference_time.microseconds}microseconds, {difference_percentage} %")
            return ("IDA*", difference_time.microseconds, difference_percentage)
        else:
            difference_percentage = round(
                (difference_time / ida_star_time * 100), 2)
            print(
                f"Dijkstra star was faster by {difference_time.microseconds}microseconds, {difference_percentage}")
            return ("Dijkstra", difference_time.microseconds, difference_percentage)
        
    def test_performance_15x15_map(self):
        dijkstra_time = Dijkstra_Performance().test_dijkstra_100_times_15x15_map()
        ida_star_time = IdaStar_Performance().test_ida_star_100_times_15x15_map()
        print(
            f"Dijkstra found 100 routes in 15x15 map in {dijkstra_time.microseconds} microseconds")
        print(f"IDA* found 100 routes in 15x15 map in {ida_star_time.microseconds} microseconds")
        difference_time = abs(dijkstra_time - ida_star_time)
        if dijkstra_time > ida_star_time:
            difference_percentage = round(
                (difference_time / dijkstra_time * 100), 2)
            print(
                f"IDA* star was faster by {difference_time.microseconds} microseconds, {difference_percentage} %")
            return ("IDA*", difference_time.microseconds, difference_percentage)
        else:
            difference_percentage = round(
                (difference_time / ida_star_time * 100), 2)
            print(
                f"Dijkstra star was faster by {difference_time.microseconds} microseconds, {difference_percentage}")
            return ("Dijkstra", difference_time.microseconds, difference_percentage)
    
    def test_performance_30x30_map(self):
        dijkstra_time = Dijkstra_Performance().test_dijkstra_100_times_30x30_map()
        ida_star_time = IdaStar_Performance().test_ida_star_100_times_30x30_map()
        print(
            f"Dijkstra found 100 routes in 30x30 map in {dijkstra_time.microseconds} microseconds")
        print(f"IDA* found 100 routes in 30x30 map in {ida_star_time.microseconds} microseconds")
        difference_time = abs(dijkstra_time - ida_star_time)
        if dijkstra_time > ida_star_time:
            difference_percentage = round(
                (difference_time / dijkstra_time * 100), 2)
            print(
                f"IDA* star was faster by {difference_time.microseconds} microseconds, {difference_percentage} %")
            return ("IDA*", difference_time.microseconds, difference_percentage)
        else:
            difference_percentage = round(
                (difference_time / ida_star_time * 100), 2)
            print(
                f"Dijkstra star was faster by {difference_time.microseconds} microseconds, {difference_percentage}")
            return ("Dijkstra", difference_time.microseconds, difference_percentage)
