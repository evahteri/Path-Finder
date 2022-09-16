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
        
    def find_route(self, start, end):
        start_x = int(start[3])
        start_y = int(start[1])
        end_x = int(end[3])
        end_y = int(end[1])
        self._initialize()
        print(start_x, start_y)
        self.distance_matrix[start_y][start_x] = 0
        heapq.heappush(self.heap, [0,(start_x,start_y)])
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
        previous = self.previous_node[(end_x, end_y)]
        while previous != (start_x, start_y):
            self.distance_matrix[previous[1]][previous[0]] = "x"
            previous = self.previous_node[previous]
        self.distance_matrix[start_y][start_x] = "start"
        self.distance_matrix[end_y][end_x] = "end"
        for row in self.distance_matrix:
            print(row)
        return self.distance_matrix
