import datetime
from data_structures.heap import Heap


class Dijkstra():
    """Class responsible for the Djikstra algorithm to find shortest path
    """

    def __init__(self, map):
        """Constructor that creates the distance matrix for the shortest distances and
        establishes all of the dictionaries and lists that the algorithm uses
        """
        self.distance_matrix = None
        self.unvisited_nodes = []
        self.visited_nodes = []
        self.heap = Heap()
        self.map = map
        self.neighbours = {}
        self.previous_node = {}

    def _map_size(self):
        size = 0
        with open(f"src/static/maps/{self.map}") as current_map:
            for i in current_map:
                size += 1
        return size

    def _initialize(self):
        """Initializes neighbours for all nodes
        """
        map_size = self._map_size()
        self.distance_matrix = [[999]*map_size for _ in range(map_size)]
        current_map = open(f"src/static/maps/{self.map}", "r")
        self.map = current_map.read().splitlines()
        y_coordinate = 0
        for y in self.map:
            x_coordinate = 0
            for x in y:
                if x != "@":
                    self.neighbours[x_coordinate, y_coordinate] = []
                    self.unvisited_nodes.append((x_coordinate, y_coordinate))
                    if x_coordinate != 0:
                        self.neighbours[x_coordinate, y_coordinate].append(
                            (x_coordinate-1, y_coordinate))
                    if x_coordinate != map_size - 1:
                        self.neighbours[x_coordinate, y_coordinate].append(
                            (x_coordinate+1, y_coordinate))
                        # Handle right neighbour
                    if y_coordinate != 0:
                        self.neighbours[x_coordinate, y_coordinate].append(
                            (x_coordinate, y_coordinate-1))
                        # Handle north neighbour
                    if y_coordinate != map_size - 1:
                        self.neighbours[x_coordinate, y_coordinate].append(
                            (x_coordinate, y_coordinate+1))
                        # Handle south neughbour
                if x == "@":
                    self.distance_matrix[y_coordinate][x_coordinate] = "@"
                x_coordinate += 1
            y_coordinate += 1

    def find_route(self, start_x, start_y, end_x, end_y):
        """The actual algorithm to find the fastest route between start and end node

        Args:
            start (tuple): Coordinate for the start node
            end (tuple): Coordinate for the end node

        Returns:
            Distance matrix that has the fastest route nodes marked as "x", and fastest route
            to each node
        """
        start_time = datetime.datetime.now()
        self._initialize()
        self.distance_matrix[start_y][start_x] = 0
        self.heap.push([0, (start_x, start_y)])
        while self.heap.get_heap_len() != 0:
            node_tuple = self.heap.pop_smallest()
            node = (node_tuple[1][0], node_tuple[1][1])
            if node in self.visited_nodes:
                continue
            self.visited_nodes.append(node)
            for neighbour in self.neighbours[node]:
                if neighbour in self.visited_nodes:
                    continue
                x_neighbour = neighbour[0]
                y_neighbour = neighbour[1]
                x_node = node[0]
                y_node = node[1]
                now = self.distance_matrix[y_neighbour][x_neighbour]
                new = self.distance_matrix[y_node][x_node] + 1
                if now == "@":
                    continue
                if new < now:
                    self.distance_matrix[y_neighbour][x_neighbour] = new
                    self.previous_node[neighbour] = node
                    self.heap.push([new, neighbour])
        previous = self.previous_node[(end_x, end_y)]
        distance = 1
        while previous != (start_x, start_y):
            self.distance_matrix[previous[1]][previous[0]] = "x"
            distance += 1
            previous = self.previous_node[previous]
        self.distance_matrix[start_y][start_x] = "start"
        self.distance_matrix[end_y][end_x] = "end"
        print(f"Shorest path length is {distance}")
        finish_time = datetime.datetime.now()
        print(f"Dijkstra found route in {finish_time-start_time}")
        return (self.distance_matrix, distance)
