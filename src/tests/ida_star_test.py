
import unittest
from algorithms.ida_star import IdaStar


class TestIdaStar(unittest.TestCase):

    def setUp(self):
        self.shortest_route = 18

    def test_ida_star_finds_route(self):
        distance = IdaStar().find_route(start="(0,0)", goal="(9,9)")[1]

        self.assertEqual(self.shortest_route, distance)
