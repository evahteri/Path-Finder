import datetime
import heapq
from random import randint
from data_structures.heap import Heap


class Heap_Performance():
    """Class responsible for testing Heap's performance
    """

    def __init__(self):
        self.heap = Heap()
        self.python_heap = []

    def test_own_heap_push_and_pop_1000_times(self):
        start_time = datetime.datetime.now()
        for i in range(1000):
            tuple = (randint(0, 100), (randint(0, 1000), randint(0, 1000)))
            self.heap.push(tuple)
        for i in range(1000):
            self.heap.pop_smallest()
        finish_time = datetime.datetime.now()
        return finish_time-start_time

    def test_python_heap_push_and_pop_1000_times(self):
        heapq.heapify(self.python_heap)
        start_time = datetime.datetime.now()
        for i in range(1000):
            tuple = (randint(0, 100), (randint(0, 1000), randint(0, 1000)))
            heapq.heappush(self.python_heap, tuple)
        for i in range(1000):
            heapq.heappop(self.python_heap)
        finish_time = datetime.datetime.now()
        return finish_time-start_time
