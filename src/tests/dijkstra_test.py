import unittest
from algorithms.dijkstra import Dijkstra


class TestDijkstra(unittest.TestCase):
    """This class tests dijkstra's algorithm
    """

    def setUp(self):
        self.shortest_route = 18

    def test_dijkstra_finds_route(self):
        """Tests if the algorithm finds the correct route
        """

        distance = Dijkstra().find_route(start="(0,0)", end="(9,9)")[1]

        self.assertEqual(self.shortest_route, distance)

    def test_dijkstra_incorrect_start_input_out_or_range(self):

        distance_matrix = Dijkstra().find_route(start="(0,10)", end="(9,9)")

        self.assertEqual("incorrect input", distance_matrix)

    def test_dijkstra_incorrect_end_input_out_or_range(self):

        distance_matrix = Dijkstra().find_route(start="(0,0)", end="(9,10)")

        self.assertEqual("incorrect input", distance_matrix)

    def test_dijkstra_incorrect_start_input_negative(self):

        distance_matrix = Dijkstra().find_route(start="(-1,0)", end="(9,9)")

        self.assertEqual("incorrect input", distance_matrix)

    def test_dijkstra_incorrect_end_input_negative(self):

        distance_matrix = Dijkstra().find_route(start="(0,0)", end="(9,-2)")

        self.assertEqual("incorrect input", distance_matrix)

    def test_dijkstra_incorrect_start_input_in_wall(self):

        distance_matrix = Dijkstra().find_route(start="(1,0)", end="(9,9)")

        self.assertEqual("incorrect input", distance_matrix)

    def test_dijkstra_incorrect_end_input_in_wall(self):

        distance_matrix = Dijkstra().find_route(start="(0,0)", end="(1,0)")

        self.assertEqual("incorrect input", distance_matrix)
