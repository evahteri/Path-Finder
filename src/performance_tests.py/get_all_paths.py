from algorithms.ida_star import IdaStar

class Get_All_Paths():
    """Class that includes all functions for Floyd Warshall algorithm
    """

    def __init__(self):
        """Constructor that creates all needed data structures and local values
        """
        self.ida_star = IdaStar()
        self.distances = {}
    
    def get_all_paths(self, map):
        size = 0
        for i in map:
            size += 1
        
        for x in range(size):
            for y in range(size):
                for x_2 in range(size):
                    for y_2 in range(size):
                        self.distances[(x,y)(x_2,y_2)] = self.ida_star.find_route(f"({x},{y})",f"({x_2},{y_2})")
        return self.distances
    

