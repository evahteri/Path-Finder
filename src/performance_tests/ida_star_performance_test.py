import datetime
from random import randint
from algorithms.ida_star import IdaStar
from services.input_check import InputCheck

class IdaStar_Performance():
    """Class responsible for testing IDA*'s performance
    """

    def __init__(self):
        pass

    def test_ida_star_100_times_small_map(self):
        """Paths are fetched 100 times in 10x10 sized map (map_1.txt)
        """
        start_time = datetime.datetime.now()
        for i in range(100):
            start_x = randint(0,9)
            start_y = randint(0,9)
            goal_x = randint(0,9)
            goal_y = randint(0,9)
            if InputCheck().check_input(current_map="map_1.txt", x_start=start_x, y_start=start_y, x_end=goal_x, y_end=goal_y):
                IdaStar("map_1.txt").find_route(start_x, start_y, goal_x, goal_y)
        finish_time = datetime.datetime.now()
        return finish_time-start_time