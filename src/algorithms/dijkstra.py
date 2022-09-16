import heapq

class Dijkstra():
    def __init__(self):
        self.distance_matrix = [[999]*10 for _ in range(10)]
        self.unvisited_nodes = []
        self.visited_nodes = []
        self.heap = []
        self.map = None
        self.neighbours = {}
        self.previous_node = {}
    
    
    def _initialize(self):

        map = open("../Path_Finder/src/static/maps/map_1.txt" , "r")
        self.map = map.read().splitlines()
        for row in self.map:
            print(row)
        y_coordinate = 0
        for y in self.map:
            x_coordinate = 0
            for x in y:
                if x != "@":
                    self.distance_matrix[y_coordinate][x_coordinate] = 999
                    self.neighbours[x_coordinate,y_coordinate] = []
                    self.unvisited_nodes.append((x_coordinate, y_coordinate))
                    if x_coordinate != 0:
                        self.neighbours[x_coordinate,y_coordinate].append((x_coordinate-1,y_coordinate))
                    if x_coordinate != 9:
                        self.neighbours[x_coordinate,y_coordinate].append((x_coordinate+1,y_coordinate))
                        #Handle right neighbour
                    if y_coordinate != 0:
                        self.neighbours[x_coordinate,y_coordinate].append((x_coordinate,y_coordinate-1))
                        #Handle north neighbour
                    if y_coordinate != 9:
                        self.neighbours[x_coordinate,y_coordinate].append((x_coordinate,y_coordinate+1))
                        #Handle south neughbour
                if x == "@":
                    self.distance_matrix[y_coordinate][x_coordinate] = "@"
                x_coordinate += 1
            y_coordinate += 1
        
    def find_route(self):
        self._initialize()
        self.distance_matrix[0][0] = 0
        heapq.heappush(self.heap, [0,(0,0)])
        while len(self.heap) != 0:
            node_tuple = heapq.heappop(self.heap)
            node = (node_tuple[1][0],node_tuple[1][1])
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
                    heapq.heappush(self.heap, (new,neighbour))
        end = (9,9)
        previous = self.previous_node[end]
        while previous != (0,0):
            self.distance_matrix[previous[1]][previous[0]] = "x"
            previous = self.previous_node[previous]
        for row in self.distance_matrix:
            print(row)
        return self.distance_matrix
