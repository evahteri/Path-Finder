import heapq
import datetime


class Dijkstra():
    """Class responsible for the Djikstra algorithm to find shortest path
    """

    def __init__(self):
        """Constructor that creates the distance matrix for the shortest distances and
        establishes all of the dictionaries and lists that the algorithm uses
        """
        self.distance_matrix = [[999]*10 for _ in range(10)]
        self.unvisited_nodes = []
        self.visited_nodes = []
        self.heap = []
        self.map = None
        self.neighbours = {}
        self.previous_node = {}
    
    def _check_input(self, start, end):
        try:
            if len(start) > 5:
                return False
            if len(end) > 5:
                return False
            if int(start[3]) > len(self.map) or int(start[3]) < 0:
                return False
            if int(start[1]) > len(self.map) or int(start[1]) < 0:
                return False 
            if int(end[3]) > len(self.map) or int(end[3]) < 0:
                return False
            if int(end[1]) > len(self.map) or int(end[1]) < 0:
                return False
            if self.map[int(start[1])][int(start[3])] == "@":
                return False
            if self.map[int(end[1])][int(end[3])] == "@":
                return False
        except IndexError:
            return False
        return True
        


    def _initialize(self):
        """Initializes neighbours for all nodes
        """

        current_map = open("../Path_Finder/src/static/maps/map_1.txt", "r")
        self.map = current_map.read().splitlines()
        y_coordinate = 0
        for y in self.map:
            x_coordinate = 0
            for x in y:
                if x != "@":
                    self.distance_matrix[y_coordinate][x_coordinate] = 999
                    self.neighbours[x_coordinate, y_coordinate] = []
                    self.unvisited_nodes.append((x_coordinate, y_coordinate))
                    if x_coordinate != 0:
                        self.neighbours[x_coordinate, y_coordinate].append(
                            (x_coordinate-1, y_coordinate))
                    if x_coordinate != 9:
                        self.neighbours[x_coordinate, y_coordinate].append(
                            (x_coordinate+1, y_coordinate))
                        # Handle right neighbour
                    if y_coordinate != 0:
                        self.neighbours[x_coordinate, y_coordinate].append(
                            (x_coordinate, y_coordinate-1))
                        # Handle north neighbour
                    if y_coordinate != 9:
                        self.neighbours[x_coordinate, y_coordinate].append(
                            (x_coordinate, y_coordinate+1))
                        # Handle south neughbour
                if x == "@":
                    self.distance_matrix[y_coordinate][x_coordinate] = "@"
                x_coordinate += 1
            y_coordinate += 1

    def find_route(self, start, end):
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
        if not self._check_input(start, end):
            return "incorrect input"
        start_x = int(start[3])
        start_y = int(start[1])
        end_x = int(end[3])
        end_y = int(end[1])
        self.distance_matrix[start_y][start_x] = 0
        heapq.heappush(self.heap, [0, (start_x, start_y)])
        while len(self.heap) != 0:
            node_tuple = heapq.heappop(self.heap)
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
                    heapq.heappush(self.heap, (new, neighbour))
        previous = self.previous_node[(end_x, end_y)]
        while previous != (start_x, start_y):
            self.distance_matrix[previous[1]][previous[0]] = "x"
            previous = self.previous_node[previous]
        self.distance_matrix[start_y][start_x] = "start"
        self.distance_matrix[end_y][end_x] = "end"
        finish_time = datetime.datetime.now()
        print(f"Route found in {finish_time-start_time}")
        return self.distance_matrix