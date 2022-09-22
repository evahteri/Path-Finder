
import unittest
from algorithms.ida_star import IdaStar

class TestIdaStar(unittest.TestCase):

    def setUp(self):
        self.correct_route = [['start', 'x', 'x', 'x', 'x', 'x', 'x', 1, 1, 1],
         ['@', '@', '@', 999, 999, 1, 'x', 1, 1, 1],
          [999, 999, '@', 999, 999, 1, 'x', '@', '@', '@'],
           [999, 999, 999, 999, 999, 1, 'x', '@', 999, 999],
            [999, 999, 999, 999, 999, 1, 'x', '@', 999, 1],
             ['@', '@', '@', '@', '@', 1, 'x', 'x', 'x', 'x'],
              [999, 999, 999, 999, 999, 999, 999, 999, 1, 'x'],
               [999, 999, 999, 999, '@', '@', '@', '@', 1, 'x'],
                [999, 999, 999, 999, '@', 999, 999, 999, 1, 'x'],
                 [999, 999, 999, 999, 999, 999, 999, 999, 999, 'end']]
    
    def test_ida_star_finds_route(self):
        distance_matrix = IdaStar().find_route(start="(0,0)", goal="(9,9)")

        self.assertEqual(self.correct_route, distance_matrix)
