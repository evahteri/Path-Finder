class MapHelper():
    """Class responsible for common map related functions
    """

    def __init__(self, current_map):
        self.map = current_map

    def get_map_size(self):
        """Function to get current map's size

        Returns:
            int: Size of current map
        """
        size = 0
        with open(f"src/static/maps/{self.map}") as current_map:
            for row in current_map:
                size += 1
        return size
