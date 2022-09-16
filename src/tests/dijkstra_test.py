import unittest
from algorithms.dijkstra import Dijkstra


class TestDijkstra(unittest.TestCase):
    """This class tests dijkstra's algorithm
    """
    def setUp(self):
        self.correct_route = [['start', 'x', 'x', 'x', 4, 5, 6, 7, 8, 9],
                              ['@', '@', '@', 'x', 5, 6, 7, 8, 9, 10],
                              [10, 9, '@', 'x', 6, 7, 8, '@', '@', '@'],
                              [9, 8, 7, 'x', 7, 8, 9, '@', 15, 16],
                              [10, 9, 8, 'x', 'x', 'x', 10, '@', 14, 15],
                              ['@', '@', '@', '@', '@', 'x', 11, 12, 13, 14],
                              [16, 15, 14, 13, 12, 'x', 'x', 'x', 'x', 15],
                              [17, 16, 15, 14, '@', '@', '@', '@', 'x', 16],
                              [18, 17, 16, 15, '@', 19, 18, 17, 'x', 17],
                              [19, 18, 17, 16, 17, 18, 19, 18, 'x', 'end']]

    def test_dijkstra_finds_route(self):
        """Tests if the algorithm finds the correct route
        """

        distance_matrix = Dijkstra().find_route(start="(0,0)", end="(9,9)")

        self.assertEqual(self.correct_route, distance_matrix)
