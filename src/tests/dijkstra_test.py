from asyncio import start_unix_server
import unittest
from algorithms.dijkstra import Dijkstra


class TestDijkstra(unittest.TestCase):
    """This class tests dijkstra's algorithm
    """

    def setUp(self):
        pass

    def test_dijkstra_finds_route(self):
        """Tests if the algorithm finds the correct route with manually counted distances.

        """
        correct_distance_1 = 18 # From (0,0) to (9,9)
        correct_distance_2 = 12 # From (0,0) to (6,6)
        correct_distance_3 = 10 # From (2,3) to (9,4)
        distance_1 = Dijkstra("map_1.txt").find_route(start_x=0, start_y=0, end_x=9, end_y=9)[1]
        distance_2 = Dijkstra("map_1.txt").find_route(start_x=0, start_y=0, end_x=6, end_y=6)[1]
        distance_3 = Dijkstra("map_1.txt").find_route(start_x=2, start_y=3, end_x=9, end_y=4)[1]

        self.assertEqual((correct_distance_1, correct_distance_2, correct_distance_3), (distance_1, distance_2, distance_3))
    