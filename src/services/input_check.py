from services.map_helper import MapHelper

class InputCheck():

    def check_input(self, current_map, x_start, y_start, x_end, y_end):
            map_size = MapHelper(current_map).get_map_size()
            current_map = open(f"src/static/maps/{current_map}", "r")
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
