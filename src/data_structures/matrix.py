class Matrix():
    
    def __init__(self):
        self.nodes = []
    
    def add_node(self,coordinate):
        coordinate = []
        self.nodes.append(coordinate)
    
    def add_edge(self, start_node, end_node):
        if end_node not in self.nodes[start_node]:
            self.nodes[start_node].append(end_node)
        if start_node not in self.nodes[end_node]:
            self.nodes[end_node].append(start_node)