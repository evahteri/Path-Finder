import datetime


class IdaStar():
    """Class that includes all functions for ida star algorithm
    """

    def __init__(self, map):
        """Constructor that creates all needed data structures and local values
        """
        self.map = map
        self.graph = {}
        self.distance_matrix = None
        self.distance = 0
        self.path = []

    def _map_size(self):
        """Function to get size of current map

        Returns:
            int: Size of current map
        """
        size = 0
        with open(f"src/static/maps/{self.map}") as current_map:
            for i in current_map:
                size += 1
        return size

    def _initialize(self):
        """Creates the graph for the algorithm
        """
        map_size = self._map_size()
        # Create matrix, first with max distances to every node
        self.distance_matrix = [[999]*map_size for _ in range(map_size)]
        current_map = open(f"src/static/maps/{self.map}", "r")
        self.map = current_map.read().splitlines()
        # Create a graph. The graph is a python dictionary with coordinates as keys and neighbours in a list
        for y in range(map_size):
            for x in range(map_size):
                self.graph[(x, y)] = []
        # Next add every neighbour to the graph
        y_coordinate = 0
        for y in self.map:
            x_coordinate = 0
            for x in y:
                if x != "@":
                    # Handle left neighbour
                    if x_coordinate != 0 and self.map[y_coordinate][x_coordinate-1] != "@":
                        self.graph[(x_coordinate, y_coordinate)].append(
                            (x_coordinate-1, y_coordinate))
                    # Handle right neighbour
                    if x_coordinate != map_size - 1 and self.map[y_coordinate][x_coordinate+1] != "@":
                        self.graph[(x_coordinate, y_coordinate)].append(
                            (x_coordinate+1, y_coordinate))
                    # Handle upper neighbour
                    if y_coordinate != 0 and self.map[y_coordinate-1][x_coordinate] != "@":
                        self.graph[(x_coordinate, y_coordinate)].append(
                            (x_coordinate, y_coordinate-1))
                    # Handle lower neighbour
                    if y_coordinate != map_size - 1 and self.map[y_coordinate+1][x_coordinate] != "@":
                        self.graph[(x_coordinate, y_coordinate)].append(
                            (x_coordinate, y_coordinate+1))
                if x == "@":
                    # Mark walls to the distance matrix
                    self.distance_matrix[y_coordinate][x_coordinate] = "@"
                x_coordinate += 1
            y_coordinate += 1

    def find_route(self, start_x, start_y, end_x, end_y):
        """Main function that uses infinite loop which calls search function to find fastest route

        Args: Four integers as a coordinates for start and goal nodes

        Returns:
            Matrix: distance matrix that has the fastest route and visited nodes marked
        """
        # Save current time for counting time spent
        start_time = datetime.datetime.now()
        # Add start node to current path
        self.path = [(start_x, start_y)]
        # Initialize graph
        self._initialize()
        start_coordinate = (start_x, start_y)
        goal_coordinate = (end_x, end_y)
        # Count threshold a.k.a. f score. Call heuristic function to get manhattan distance
        threshold = self._heuristic(start_coordinate, goal_coordinate)
        while True:
            # Call search function, g score is 0
            new_threshold = self._search(
                node=start_coordinate, g=0, threshold=threshold, goal=goal_coordinate)
            # If path is found,
            if new_threshold == "found":
                # Mark start and end nodes to the distance matrix
                self.distance_matrix[start_coordinate[1]
                                     ][start_coordinate[0]] = "start"
                self.distance_matrix[goal_coordinate[1]
                                     ][goal_coordinate[0]] = "end"
                print(f"Shortest path length is {self.distance}")
                # "Stop the clock" to get time spent fetching path
                finish_time = datetime.datetime.now()
                print(f" IDA* found route found in {finish_time-start_time}")
                # Return tuple with distance matrix and shortest path length
                return (self.distance_matrix, self.distance, finish_time)
            # If search function returns max int, any path isn't found
            if new_threshold == float("inf"):
                return False
            # Update threshold
            threshold = new_threshold

    def _search(self, node, g, threshold, goal):
        """Iterative search function

        Args:
            node (tuple): current node that the main function is handling
            g (int): g score is the current cost
            threshold (int): threshold for maximum distance
            goal (tuple): goal node

        Returns:
            if path is found: "found" string, if not found: minimum value for the fastest route
        """
        # New f score is g score plus heuristic to the goal node from current node
        f = g + self._heuristic(node, goal)
        # If f score is bigger than threshold, return f score
        if f > threshold:
            return f
        # If node is goal, the path is found
        if node == goal:
            return "found"
        # Set min value to maximum integer
        min_value = float("inf")
        # Go trough node's neighbours
        for neighbour in self.graph[node]:
            # If the neighbour is not in current path, add it there
            if neighbour not in self.path:
                self.path.append(neighbour)
                # Mark neighbour as "visited" for ui
                self.distance_matrix[neighbour[1]][neighbour[0]] = 1
                # Recursive call for nodes neighbours, g+1 is the cost to travel to that node
                search_result = self._search(neighbour, g+1, threshold, goal)
                # If call returns found, shortest path is found
                if search_result == "found":
                    # Mark current node to correct route
                    self.distance_matrix[node[1]][node[0]] = "x"
                    # Update shortest distance counter
                    self.distance += 1
                    return "found"
                # Update minimun value to improve estimate
                if search_result < min_value:
                    min_value = search_result
                # Remove node from current path
                self.path.pop()
        return min_value

    def _heuristic(self, start, goal):
        """Heuristic function for the algorithm

        Args:
            start (tuple): start node
            goal (tuple): goal node

        Returns:
            int: Manhattan distance between start and goal node
        """

        x_distance = abs(start[0] - goal[0])
        y_distance = abs(start[1] - goal[1])
        return x_distance + y_distance
