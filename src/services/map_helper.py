class MapHelper():

    def __init__(self, map):
        self.map = map

    def get_map_size(self):
        size = 0
        with open(f"src/static/maps/{self.map}") as current_map:
            for row in current_map:
                size += 1
        return size
