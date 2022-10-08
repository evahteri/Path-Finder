class FloydWarshall():
    """Class that includes all functions for Floyd Warshall algorithm
    """

    def __init__(self):
        """Constructor that creates all needed data structures and local values
        """
        self.map = None
        self.size = 0
        self.distance_matrix = {}
        self.distances = []

    def _initialize(self):
        """Function to establish the distance matrix as a correct size
        """
        current_map = open("../Path_Finder/src/static/maps/map_1.txt", "r")
        self.map = current_map.read().splitlines()
        for row in self.map: 
            self.size += 1
        y_coordinate = 0
        for y in self.map:
            x_coordinate = 0
            for x in y:
                if x != "@":
                    if x_coordinate != 0:
                        # Handle left neighbour
                        # (a,b,x) a= start node, b = end node x = distance
                        self.distances.append(((x_coordinate, y_coordinate)(x_coordinate-1, y_coordinate), 1))
                        self.distances.append(((x_coordinate-1, y_coordinate)(x_coordinate, y_coordinate), 1))
                    if x_coordinate != 9:
                        self.distances.append(((x_coordinate, y_coordinate)(x_coordinate+1, y_coordinate), 1))
                        self.distances.append(((x_coordinate+1, y_coordinate)(x_coordinate, y_coordinate), 1))
                        # Handle right neighbour
                    if y_coordinate != 0:
                        self.distances.append(((x_coordinate, y_coordinate)(x_coordinate, y_coordinate-1), 1))
                        self.distances.append(((x_coordinate, y_coordinate-1)(x_coordinate, y_coordinate), 1))
                        # Handle north neighbour
                    if y_coordinate != 9:
                        self.distances.append(((x_coordinate, y_coordinate)(x_coordinate, y_coordinate+1), 1))
                        self.distances.append(((x_coordinate, y_coordinate+1)(x_coordinate, y_coordinate), 1))
                        # Handle south neughbour
                x_coordinate += 1
            y_coordinate += 1
        for x in range(self.size):
            for y in range(self.size):
                for x_2 in range(self.size):
                    for y_2 in range(self.size):
                        self.distance_matrix[(x,y)(x_2,y_2)] = -1
                        if (x,y) == (x_2,y_2):
                            self.distance_matrix[(x,y)(x_2,y_2)] = 0

    def find_routes(self):
        for node in self.distances:
            old_distance = self.distance_matrix[node[0]]

        # Find shortest distances
        for k in range(self.size):
            for i in range(self.size):
                for j in range(self.size):
                    self.distance_matrix[i][j] = min((self.distance_matrix[i][j], self.distance_matrix[i][k] + self.distance_matrix[k][j]))


        

