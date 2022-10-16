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
                    # Neighbour list for every node
                    self.neighbours[x_coordinate, y_coordinate] = []
                    # Mark every node as unvisited
                    self.unvisited_nodes.append((x_coordinate, y_coordinate))
                    # Handle left neighbour
                    if x_coordinate != 0 and self.map[y_coordinate][x_coordinate-1] != "@":
                        self.neighbours[x_coordinate, y_coordinate].append(
                            (x_coordinate-1, y_coordinate))
                    # Handle right neighour
                    if x_coordinate != map_size - 1 and self.map[y_coordinate][x_coordinate+1] != "@":
                        self.neighbours[x_coordinate, y_coordinate].append(
                            (x_coordinate+1, y_coordinate))
                    # Handle upper neighbour
                    if y_coordinate != 0 and self.map[y_coordinate-1][x_coordinate] != "@":
                        self.neighbours[x_coordinate, y_coordinate].append(
                            (x_coordinate, y_coordinate-1))
                    # Handle lower neighbour
                    if y_coordinate != map_size - 1 and self.map[y_coordinate+1][x_coordinate] != "@":
                        self.neighbours[x_coordinate, y_coordinate].append(
                            (x_coordinate, y_coordinate+1))
                # If coordinate is a wall, mark it
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
        # Get current time to count performance
        start_time = datetime.datetime.now()
        # Initialize matrix and neighbours
        self._initialize()
        # Distance to start node is 0
        self.distance_matrix[start_y][start_x] = 0
        # Add start node to the heap with weight (again 0)
        self.heap.push([0, (start_x, start_y)])
        # Loop until heap is empty
        while self.heap.get_heap_len() != 0:
            # Remove smallest node by weight
            node_tuple = self.heap.pop_smallest()
            node = (node_tuple[1][0], node_tuple[1][1])
            # If node is already visited, continue
            if node in self.visited_nodes:
                continue
            # Mark current node as visited
            self.visited_nodes.append(node)
            # Go through node's neighbours
            for neighbour in self.neighbours[node]:
                # If neighbour has been already visited, continue
                if neighbour in self.visited_nodes:
                    continue
                x_neighbour = neighbour[0]
                y_neighbour = neighbour[1]
                x_node = node[0]
                y_node = node[1]
                # Current distance
                now = self.distance_matrix[y_neighbour][x_neighbour]
                # New distance
                new = self.distance_matrix[y_node][x_node] + 1
                # If new distance is lower than old, update it
                if new < now:
                    self.distance_matrix[y_neighbour][x_neighbour] = new
                    # Add the neighbour to previous nodes to get the shortest path later
                    self.previous_node[neighbour] = node
                    # Add neighbour with updated weight to the heap
                    self.heap.push([new, neighbour])
        # Fetching the travelled path
        previous = self.previous_node[(end_x, end_y)]
        # Counting the length
        distance = 1
        while previous != (start_x, start_y):
            self.distance_matrix[previous[1]][previous[0]] = "x"
            distance += 1
            previous = self.previous_node[previous]
        # Update the distance matrix for ui
        self.distance_matrix[start_y][start_x] = "start"
        self.distance_matrix[end_y][end_x] = "end"
        # Print the length
        print(f"Shorest path length is {distance}")
        # Get current time to "stop the clock" and save time spent getting route
        finish_time = datetime.datetime.now()
        print(f"Dijkstra found route in {finish_time-start_time}")
        # Return tuple with distance matrix and shortest path length
        return (self.distance_matrix, distance)
