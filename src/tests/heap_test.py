
import unittest
from data_structures.heap import Heap


class TestHeap(unittest.TestCase):
    """Testing heap data structure with test for every function
    """

    def setUp(self):
        """Initialize heap
        """
        self.heap = Heap()

    def test_push(self):
        """Test push function with one push and use get_heap_len to get it's length
        """
        self.heap.push([0, (1, 1)])
        heap_size = self.heap.get_heap_len()
        self.assertEqual(heap_size, 1)

    def test_pop_returns_smallest(self):
        """Testing pop function (remove smallest)
        First two nodes are pushed to the heap, then one removed.
        Then check if the smaller was removed.
        """
        self.heap.push([0, (1, 1)])
        self.heap.push([2, (2, 3)])
        smallest = self.heap.pop_smallest()
        self.assertEqual(smallest, [0, (1, 1)])

    def test_pop_removes_element(self):
        """Test if pop function removes a node
        First two nodes are pushed to the heap, then one removed.
        Then check if length is updated.
        """
        self.heap.push([0, (1, 1)])
        self.heap.push([2, (2, 3)])
        self.heap.pop_smallest()
        heap_size = self.heap.get_heap_len()
        self.assertEqual(heap_size, 1)

    def test_pop_with_empty_heap(self):
        """Tests if pop with empty heap returns None
        """
        smallest = self.heap.pop_smallest()
        self.assertEqual(None, smallest)
