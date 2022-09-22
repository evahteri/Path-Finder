

class IdaStar():

    def __init__(self):
        self.graph = {}
        self.max_f_value = 25 #maximum cost of shortest path between nodes in the map
        self.threshold = None # f score for the main function
        self.min_value = 999 #cost of shortest path, first a max value

    def _initialize(self):
        current_map = open("../Path_Finder/src/static/maps/map_1.txt", "r")
        self.map = current_map.read().splitlines()
        for y in range(10):
            for x in range(10):
                self.graph[(x,y)] = []

        y_coordinate = 0
        for y in self.map:
            x_coordinate = 0
            for x in y:
                if x != "@":

                    if x_coordinate != 0:
                        self.graph[(x_coordinate,y_coordinate)].append(
                            (x_coordinate-1, y_coordinate))
                    if x_coordinate != 9:
                        self.graph[(x_coordinate,y_coordinate)].append(
                            (x_coordinate+1, y_coordinate))
                        # Handle right neighbour
                    if y_coordinate != 0:
                        self.graph[(x_coordinate,y_coordinate)].append(
                            (x_coordinate, y_coordinate-1))
                        # Handle north neighbour
                    if y_coordinate != 9:
                        self.graph[(x_coordinate,y_coordinate)].append(
                            (x_coordinate, y_coordinate+1))
                        # Handle south neughbour
                if x == "@":
                    self.graph[(x_coordinate,y_coordinate)] = "@"
                x_coordinate += 1
            y_coordinate += 1
    
    def find_route(self, start, goal):
        self._initialize()
        for i in self.graph:
            print(i)
            print(self.graph[i])
        start_coordinate = (int(start[1]),int(start[3]))
        goal_coordinate = (int(goal[1]),int(goal[3]))
        self.threshold = self._heuristic(start_coordinate, goal_coordinate) # f score is cost of current node x and heuristic of the node x
        while True:
            found_path = self._search(node=start_coordinate,g=0,threshold=self.threshold, goal=goal_coordinate)
            if found_path == "found":
                print(self.min_value)
                print("found")
                return True
            if found_path > self.max_f_value: 
                return False
            self.threshold = found_path

    def _search(self, node, g, threshold, goal):
        f = g + self._heuristic(node, goal)
        if f > self.threshold:
            return f
        if node == goal:
            return "found"
        for neighbour in self.graph[node]:
            if neighbour == "@":
                continue
            search_result = self._search(neighbour,g+1,threshold, goal) #recursive call for nodes neighbours, g+1 is the cost to travel to that node
            if search_result == "found":
                return "found"
            if search_result < self.min_value:
                self.min_value = search_result
        return self.min_value
    
    def _heuristic(self,start, goal):
        #Getting manhattan distance between nodes
        x_distance = start[0] - goal[0]
        y_distance = start[1] - goal[1]
        if x_distance < 0:
            x_distance = x_distance * (-1)
        if y_distance < 0:
            y_distance = y_distance * (-1)
        print(x_distance + y_distance)
        return x_distance + y_distance