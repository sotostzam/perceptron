import json

class Node:
    def __init__(self, value):
        self.value = value
        self.discovered = False

    # Rich comparison method called by x < y 
    def __lt__(self, other):
        # Returns priority based on alphabetical order
        return self.value < other.value

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    # Function to fill graph from dataset
    def load_data(self, path):
        with open(path) as json_file:
            data = json.load(json_file)
            # Loop through the vertices
            for vertice in data:
                node = self.add_node(vertice)
                # Loop through the edges
                for edge in data[vertice]:
                    # Loop through the keys (1 Iteration only)
                    for node_name in edge:
                        self.add_edge(node, self.add_node(node_name), edge[node_name])

    # Helper function to check regulate node's creation
    def add_node(self, value):
        for node in self.nodes:
            if node.value == value:
                return node
        new_node = Node(value)
        self.nodes.append(new_node)
        return new_node

    # Function to add an edge to the graph
    def add_edge(self, origin_node, target_node, cost = 0):
        self.edges.append((origin_node, target_node, cost))

    # Function returning a list of adjacent nodes
    def get_neighbors(self, node):
        neighbors = []
        for edge in self.edges:
            if (node == edge[0]):
                neighbors.append((edge[1], edge[2]))
        return neighbors

    # Helper function returning node object from name
    def get_node_obj(self, value):
        for node in self.nodes:
            if node.value == value:
                return node

    # Helper function to reset all nodes discovered status
    def reset_nodes(self):
        for node in self.nodes:
            if node.discovered:
                node.discovered = False