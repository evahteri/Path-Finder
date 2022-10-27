
import unittest
from services.input_check import InputCheck
from services.map_helper import MapHelper


class TestServices(unittest.TestCase):
    """Tests services classes
    """

    def setUp(self):
        pass

    def test_map_size(self):
        """Tests get_map_size function
        """
        size = MapHelper(current_map="map_1.txt").get_map_size()
        self.assertEqual(size, 10)

    def test_check_input_too_big_start_x(self):
        """Tests inputcheck if start x-coordinate is too big
        """
        result = InputCheck().check_input(current_map="map_1.txt",
                                          x_start=10, y_start=0, x_end=9, y_end=9)

        self.assertEqual(False, result)

    def test_check_input_too_big_start_y(self):
        """Tests inputcheck if start y-coordinate is too big
        """
        result = InputCheck().check_input(current_map="map_1.txt",
                                          x_start=0, y_start=10, x_end=9, y_end=9)

        self.assertEqual(False, result)

    def test_check_input_too_big_end_x(self):
        """Tests inputcheck if end x-coordinate is too big
        """
        result = InputCheck().check_input(current_map="map_1.txt",
                                          x_start=0, y_start=0, x_end=10, y_end=9)

        self.assertEqual(False, result)

    def test_check_input_too_big_end_y(self):
        """Tests inputcheck if end y-coordinate is too big
        """
        result = InputCheck().check_input(current_map="map_1.txt",
                                          x_start=0, y_start=0, x_end=9, y_end=10)

        self.assertEqual(False, result)

    def test_check_input_negative_start_x(self):
        """Tests inputcheck if negative value is given
        """
        result = InputCheck().check_input(current_map="map_1.txt",
                                          x_start=-1, y_start=0, x_end=9, y_end=9)

        self.assertEqual(False, result)

    def test_check_input_negative_start_y(self):
        """Tests inputcheck if negative value is given
        """
        result = InputCheck().check_input(current_map="map_1.txt",
                                          x_start=0, y_start=-1, x_end=9, y_end=9)

        self.assertEqual(False, result)

    def test_check_input_negative_end_x(self):
        """Tests inputcheck if negative value is given
        """
        result = InputCheck().check_input(current_map="map_1.txt",
                                          x_start=0, y_start=0, x_end=-1, y_end=9)

        self.assertEqual(False, result)

    def test_check_input_negative_end_y(self):
        """Tests inputcheck if negative value is given
        """
        result = InputCheck().check_input(current_map="map_1.txt",
                                          x_start=0, y_start=0, x_end=9, y_end=-1)

        self.assertEqual(False, result)

    def test_check_input_with_string(self):
        """Tests inputcheck if input is string format and not integer
        """
        result = InputCheck().check_input(current_map="map_1.txt",
                                          x_start="a", y_start=0, x_end=9, y_end=0)

        self.assertEqual(False, result)

    def test_check_input_with_same_coordinate(self):
        """Tests inputcheck if start and end coordinate is the same
        """
        result = InputCheck().check_input(current_map="map_1.txt",
                                          x_start=0, y_start=0, x_end=0, y_end=0)

        self.assertEqual(False, result)

    def test_check_input_start_is_wall(self):
        """Tests inputcheck if start coordinate is a wall
        """
        result = InputCheck().check_input(current_map="map_1.txt",
                                          x_start=0, y_start=1, x_end=0, y_end=0)

        self.assertEqual(False, result)

    def test_check_input_end_is_wall(self):
        """Tests inputcheck if end coordinate is a wall
        """
        result = InputCheck().check_input(current_map="map_1.txt",
                                          x_start=0, y_start=0, x_end=0, y_end=1)

        self.assertEqual(False, result)
