
import unittest
from services.input_check import InputCheck
from services.map_helper import MapHelper


class TestServices(unittest.TestCase):

    def setUp(self):
        pass

    def test_map_size(self):
        size = MapHelper(map="map_1.txt").get_map_size()
        self.assertEqual(size, 10)

    def test_check_input_too_big_start_x(self):
        result = InputCheck().check_input(current_map="map_1.txt",
                                          x_start=10, y_start=0, x_end=9, y_end=9)

        self.assertEqual(False, result)

    def test_check_input_too_big_start_y(self):
        result = InputCheck().check_input(current_map="map_1.txt",
                                          x_start=0, y_start=10, x_end=9, y_end=9)

        self.assertEqual(False, result)

    def test_check_input_too_big_end_x(self):
        result = InputCheck().check_input(current_map="map_1.txt",
                                          x_start=0, y_start=0, x_end=10, y_end=9)

        self.assertEqual(False, result)

    def test_check_input_too_big_end_y(self):
        result = InputCheck().check_input(current_map="map_1.txt",
                                          x_start=0, y_start=0, x_end=9, y_end=10)

        self.assertEqual(False, result)

    def test_check_input_negative_start_x(self):
        result = InputCheck().check_input(current_map="map_1.txt",
                                          x_start=-1, y_start=0, x_end=9, y_end=9)

        self.assertEqual(False, result)

    def test_check_input_negative_start_y(self):
        result = InputCheck().check_input(current_map="map_1.txt",
                                          x_start=0, y_start=-1, x_end=9, y_end=9)

        self.assertEqual(False, result)

    def test_check_input_negative_end_x(self):
        result = InputCheck().check_input(current_map="map_1.txt",
                                          x_start=0, y_start=0, x_end=-1, y_end=9)

        self.assertEqual(False, result)

    def test_check_input_negative_end_y(self):
        result = InputCheck().check_input(current_map="map_1.txt",
                                          x_start=0, y_start=0, x_end=9, y_end=-1)

        self.assertEqual(False, result)

    def test_check_input_with_string(self):
        result = InputCheck().check_input(current_map="map_1.txt",
                                          x_start="a", y_start=0, x_end=9, y_end=0)

        self.assertEqual(False, result)

    def test_check_input_with_same_coordinate(self):
        result = InputCheck().check_input(current_map="map_1.txt",
                                          x_start=0, y_start=0, x_end=0, y_end=0)

        self.assertEqual(False, result)

    def test_check_input_start_is_wall(self):
        result = InputCheck().check_input(current_map="map_1.txt",
                                          x_start=0, y_start=1, x_end=0, y_end=0)

        self.assertEqual(False, result)

    def test_check_input_end_is_wall(self):
        result = InputCheck().check_input(current_map="map_1.txt",
                                          x_start=0, y_start=0, x_end=0, y_end=1)

        self.assertEqual(False, result)
