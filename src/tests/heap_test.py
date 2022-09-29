
import unittest
from data_structures.heap import Heap


class TestHeap(unittest.TestCase):

    def setUp(self):
        self.heap = Heap()

    def test_push(self):
        self.heap.push([0, (1, 1)])
        heap_size = self.heap.get_heap_len()
        self.assertEqual(heap_size, 1)

    def test_pop_returns_smallest(self):
        self.heap.push([0, (1, 1)])
        self.heap.push([2, (2, 3)])
        smallest = self.heap.pop_smallest()
        self.assertEqual(smallest, [0, (1, 1)])

    def test_pop_removes_element(self):
        self.heap.push([0, (1, 1)])
        self.heap.push([2, (2, 3)])
        self.heap.pop_smallest()
        heap_size = self.heap.get_heap_len()
        self.assertEqual(heap_size, 1)
