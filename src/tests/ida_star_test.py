
import unittest
from algorithms.ida_star import IdaStar
from algorithms.dijkstra import Dijkstra


class TestIdaStar(unittest.TestCase):

    def setUp(self):
        pass

    def test_ida_star_finds_route(self):
        """Here the correct distances are fetched with Dijkstra
        """
        correct_distance_1 = Dijkstra("map_1.txt").find_route(start_x=0, start_y=0, end_x=9, end_y=9)[1]
        correct_distance_2 = Dijkstra("map_1.txt").find_route(start_x=3, start_y=2, end_x=9, end_y=9)[1]
        correct_distance_3 = Dijkstra("map_1.txt").find_route(start_x=0, start_y=9, end_x=9, end_y=0)[1]
        correct_distance_4 = Dijkstra("map_1.txt").find_route(start_x=0, start_y=4, end_x=9, end_y=3)[1]

        distance_1 = IdaStar("map_1.txt").find_route(start_x=0, start_y=0, end_x=9, end_y=9)[1]
        distance_2 = IdaStar("map_1.txt").find_route(start_x=3, start_y=2, end_x=9, end_y=9)[1]
        distance_3 = IdaStar("map_1.txt").find_route(start_x=0, start_y=9, end_x=9, end_y=0)[1]
        distance_4 = IdaStar("map_1.txt").find_route(start_x=0, start_y=4, end_x=9, end_y=3)[1]

        self.assertEqual((correct_distance_1, correct_distance_2, correct_distance_3, correct_distance_4), (distance_1, distance_2, distance_3, distance_4))
    
    def test_ida_star_impossible_route(self):
        """Test if algorithm returns False when no route can be found
        """
        path = IdaStar("map_4.txt").find_route(start_x=0, start_y=0, end_x=4, end_y=4)

        self.assertEqual(False, path)