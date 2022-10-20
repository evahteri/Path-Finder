import matplotlib.pyplot as plt
from performance_tests import ida_star_performance_test
from performance_tests.dijkstra_performance_test import Dijkstra_Performance
from performance_tests.ida_star_performance_test import IdaStar_Performance
from performance_tests.heap_performance_test import Heap_Performance
from algorithms.dijkstra import Dijkstra
from algorithms.ida_star import IdaStar
from services.input_check import InputCheck

class PerformanceTest():
    """This class tests performance of both algorithms
    """

    def __init__(self):
        pass

    def test_gradual_performance(self):
        """Plots performace results from 15x15 map
        """
        results = {}
        results["dijkstra"] = []
        results["ida_star"] = []
        for y in range(14):
            for x in range(14):
                if InputCheck().check_input(current_map="map_2.txt", x_start=0, y_start=0, x_end=x, y_end=y):
                    dijkstra_result = Dijkstra("map_2.txt").find_route(start_x=0, start_y=0, end_x=x, end_y=y)
                    ida_star_result = IdaStar("map_2.txt").find_route(start_x=0, start_y=0, end_x=x, end_y=y)
                    if dijkstra_result:
                        results["dijkstra"].append((dijkstra_result[1], dijkstra_result[2].microsecond))
                    if ida_star_result:
                        results["ida_star"].append((ida_star_result[1], ida_star_result[2].microsecond))
        for result in results["dijkstra"]:
            plt.plot(result[0],result[1], label="Dijkstra")
        
        for result in results["ida_star"]:
            plt.plot(result[0],result[1], label="IDA*")
        
        plt.xlabel("Time took (microseconds)")

        plt.ylabel("Path length")

        plt.title("Time effiency in 30x30 map")

        plt.legend()

        plt.show()


    def test_heap_performance(self):
        """Tests heap with 1000 push and pop calls, comparing results to Python's own heapq heap.
        """
        own_heap_time = Heap_Performance().test_own_heap_push_and_pop_1000_times()
        python_heap_time = Heap_Performance().test_python_heap_push_and_pop_1000_times()
        print(f"My heap did 1000 push and pop functions in {own_heap_time.microseconds} microseconds. \
            Python's heapq did the same in {python_heap_time.microseconds} microseconds.")
        difference_time = abs(own_heap_time - python_heap_time)
        if own_heap_time > python_heap_time:
            difference_percentage = round(
                (difference_time / own_heap_time * 100), 2)
            return (own_heap_time, python_heap_time, difference_percentage)
        else:
            difference_percentage = round(
                (difference_time / python_heap_time * 100), 2)
            return (own_heap_time, python_heap_time, difference_percentage)

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

    def test_performance_50x50_map(self):
        dijkstra_time = Dijkstra_Performance().test_dijkstra_10_times_50x50_map()
        ida_star_time = IdaStar_Performance().test_ida_star_10_times_50x50_map()
        print(
            f"Dijkstra found 100 routes in 50x50 map in {dijkstra_time.microseconds} microseconds")
        print(f"IDA* found 100 routes in 50x50 map in {ida_star_time.microseconds} microseconds")
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

