from services.map_helper import MapHelper


class InputCheck():
    """Class for checking inputs
    """

    def check_input(self, current_map, x_start, y_start, x_end, y_end):
        """Input checker to make sure the coordinates aren't walls or out of bounds

        Args:
            current_map (string): string that describes the current map .txt file
            x_start (int): x coordinate for start
            y_start (int): y coordinate for start
            x_end (int): x coordinate for start
            y_end (int): y coordinate for start

        Returns:
            Boolean: True if input is valid, False else
        """
        map_size = MapHelper(current_map).get_map_size()
        current_map = open(f"src/static/maps/{current_map}", "r")
        current_map = current_map.read().splitlines()
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
        if current_map[int(y_start)][int(x_start)] == "@":
            return False
        if current_map[int(y_end)][int(x_end)] == "@":
            return False
        return True
