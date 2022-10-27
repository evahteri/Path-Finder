import datetime
import heapq
from random import randint
from data_structures.heap import Heap


class HeapPerformance():
    """Class responsible for testing Heap's performance
    """

    def __init__(self):
        self.heap = Heap()
        self.python_heap = []

    def test_own_heap_push_and_pop_1000_times(self):
        """Tests self made heap 1000 times with push and pop functions

        Returns:
            datetime object: run time of the performance test
        """
        start_time = datetime.datetime.now()
        for i in range(1000):
            rand_tuple = (randint(0, 100),
                          (randint(0, 1000), randint(0, 1000)))
            self.heap.push(rand_tuple)
        for i in range(1000):
            self.heap.pop_smallest()
        finish_time = datetime.datetime.now()
        return finish_time-start_time

    def test_python_heap_push_and_pop_1000_times(self):
        """Tests heapq's heap 1000 times with push and pop functions

        Returns:
            datetime object: run time of the performance test
        """
        heapq.heapify(self.python_heap)
        start_time = datetime.datetime.now()
        for i in range(1000):
            rand_tuple = (randint(0, 100),
                          (randint(0, 1000), randint(0, 1000)))
            heapq.heappush(self.python_heap, rand_tuple)
        for i in range(1000):
            heapq.heappop(self.python_heap)
        finish_time = datetime.datetime.now()
        return finish_time-start_time
