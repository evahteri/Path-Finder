import datetime
from random import randint
from algorithms.dijkstra import Dijkstra

class Dijkstra_Performance():

    def __init__(self):
        pass

    def _get_map_size(self):
        size = 0
        with open(f"src/static/maps/map_1.txt") as current_map:
            for row in current_map:
                size += 1
        return size

    def _check_input(self, x_start, y_start, x_end, y_end):
        map_size = self._get_map_size()
        current_map = open(f"src/static/maps/map_1.txt", "r")
        map = current_map.read().splitlines()
        try:
            if int(x_start) > map_size-1:
                return False
            if int(y_start) > map_size-1:
                return False
            if int(x_end) > map_size-1:
                return False
            if int(y_end) > map_size-1:
                return False
            if int(x_start) < 0:
                return False
            if int(y_start) < 0:
                return False
            if int(x_end) < 0:
                return False
            if int(y_end) < 0:
                return False
        except ValueError:
            return False
        if (x_start, y_start) == (x_end, y_end):
            return False
        if map[int(y_start)][int(x_start)] == "@":
            return False
        if map[int(y_end)][int(x_end)] == "@":
            return False
        return True

    def test_dijkstra_100_times_small_map(self):
        """Paths are fetched 100 times in 10x10 sized map (map_1.txt)
        """
        start_time = datetime.datetime.now()
        for i in range(100):
            start_x = randint(0,9)
            start_y = randint(0,9)
            goal_x = randint(0,9)
            goal_y = randint(0,9)
            if self._check_input(start_x, start_y, goal_x, goal_y):
                Dijkstra("map_1.txt").find_route(start_x, start_y, goal_x, goal_y)
        finish_time = datetime.datetime.now()
        return finish_time-start_time