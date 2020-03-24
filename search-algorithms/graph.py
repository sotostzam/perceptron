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
        self.nodes        = []
        self.edges        = []
        self.dist_to_goal = []

    # Function to fill graph from dataset
    def load_data(self, path):
        with open(path) as json_file:
            data = json.load(json_file)
            # Loop through the vertices
            for vertice in data:
                node = self.add_node(vertice)
                # Loop through the edges
                for edge in data[vertice]['Edges']:
                    # Loop through the keys (1 Iteration only)
                    for node_name in edge:
                        self.edges.append((node, self.add_node(node_name), edge[node_name]))
                self.dist_to_goal.append((node, data[vertice]['Distance']))

    # Helper function to check regulate node's creation
    def add_node(self, value):
        for node in self.nodes:
            if node.value == value:
                return node
        new_node = Node(value)
        self.nodes.append(new_node)
        return new_node

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

    # Heuristic function returning the distance from origin to target node
    def get_distance(self, value):
        for distance in self.dist_to_goal:
            if distance[0] == value:
                return distance[1]

    # Helper function to reset all nodes discovered status
    def reset_nodes(self):
        for node in self.nodes:
            if node.discovered:
                node.discovered = False
