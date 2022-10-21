from services.map_helper import MapHelper
from services.input_check import InputCheck
from algorithms.ida_star import IdaStar
from algorithms.dijkstra import Dijkstra
from performance_tests.heap_performance_test import Heap_Performance
from performance_tests.ida_star_performance_test import IdaStar_Performance
from performance_tests.dijkstra_performance_test import Dijkstra_Performance
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")


class PerformanceTest():
    """This class tests performance of both algorithms
    """

    def __init__(self):
        pass

    def test_performance_plot(self, current_map):
        """Plots performace results 
        """
        # Clear current canvas if exists
        plt.clf()
        results = {}
        results["dijkstra"] = []
        results["ida_star"] = []
        d_handled_distances = []
        i_handled_distances = []
        map_length = MapHelper(current_map).get_map_size()
        # Start coordinate will be (0,0). End coordinate is changing in range of the map size.
        for y in range(map_length):
            for x in range(map_length):
                if InputCheck().check_input(current_map=current_map, x_start=0, y_start=0, x_end=x, y_end=y):
                    dijkstra_result = Dijkstra(current_map).find_route(
                        start_x=0, start_y=0, end_x=x, end_y=y)
                    ida_star_result = IdaStar(current_map).find_route(
                        start_x=0, start_y=0, end_x=x, end_y=y)
                    # If path is found, the distance is added to handled distances and to the algorithm's results
                    if dijkstra_result:
                        if dijkstra_result[1] not in d_handled_distances:
                            results["dijkstra"].append(
                                (dijkstra_result[1], dijkstra_result[2].microsecond))
                            d_handled_distances.append(dijkstra_result[1])
                    if ida_star_result:
                        if ida_star_result[1] not in i_handled_distances:
                            i_handled_distances.append(ida_star_result[1])
                            results["ida_star"].append(
                                (ida_star_result[1], ida_star_result[2].microsecond))
        # Sort the results based on the distance for the pyplot function to work correctly
        results_dijkstra = sorted(
            results["dijkstra"], key=lambda value: value[0])
        results_ida_star = sorted(
            results["ida_star"], key=lambda value: value[0])
        x = []
        y = []
        for result in results_dijkstra:
            x.append(result[0])
            y.append(result[1])
        plt.plot(x, y, label="Dijkstra")
        x_2 = []
        y_2 = []
        for result in results_ida_star:
            x_2.append(result[0])
            y_2.append(result[1])

        plt.plot(x_2, y_2, label="IDA*")

        plt.ylabel("Time took (microseconds)")

        plt.xlabel("Path length")

        plt.title(
            f"Time effiency in {map_length}x{map_length} map (Higher is worse)")

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
        print(
            f"IDA* found 100 routes in 10x10 map in {ida_star_time.microseconds} microseconds")
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
        """Tests 100 random routes through 15x15 map with walls.
        After testing, the time difference is counted.
        """
        dijkstra_time = Dijkstra_Performance().test_dijkstra_100_times_15x15_map()
        ida_star_time = IdaStar_Performance().test_ida_star_100_times_15x15_map()
        print(
            f"Dijkstra found 100 routes in 15x15 map in {dijkstra_time.microseconds} microseconds")
        print(
            f"IDA* found 100 routes in 15x15 map in {ida_star_time.microseconds} microseconds")
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
        """Tests 100 random routes through 30x30 map with walls.
        After testing, the time difference is counted.
        """
        dijkstra_time = Dijkstra_Performance().test_dijkstra_100_times_30x30_map()
        ida_star_time = IdaStar_Performance().test_ida_star_100_times_30x30_map()
        print(
            f"Dijkstra found 100 routes in 30x30 map in {dijkstra_time.microseconds} microseconds")
        print(
            f"IDA* found 100 routes in 30x30 map in {ida_star_time.microseconds} microseconds")
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
        """Tests 10 random routes through 50x50 map with walls.
        After testing, the time difference is counted.
        """
        dijkstra_time = Dijkstra_Performance().test_dijkstra_10_times_50x50_map()
        ida_star_time = IdaStar_Performance().test_ida_star_10_times_50x50_map()
        print(
            f"Dijkstra found 100 routes in 50x50 map in {dijkstra_time.microseconds} microseconds")
        print(
            f"IDA* found 100 routes in 50x50 map in {ida_star_time.microseconds} microseconds")
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
