import json
from queue import PriorityQueue

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
                node = graph.add_node(vertice)
                # Loop through the edges
                for edge in data[vertice]:
                    # Loop through the keys (1 Iteration only)
                    for node_name in edge:
                        graph.add_edge(node, graph.add_node(node_name), edge[node_name])

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

# Define the Uniform Cost Search algorithm
def ucs_search(graph, origin, target):
    target_node = graph.get_node_obj(target)
    # UCS uses a priority queue. Here priority is the lowest cost
    frontier = PriorityQueue()        
    # Frontier is a tuple of (priority, (node, path_to_node))                    
    frontier.put((0, (graph.get_node_obj(origin), [])))
    while frontier.qsize() > 0:
        current_cost, state = frontier.get()
        current = state[0]
        current_path = state[1]
        if current.discovered != True:
            current.discovered = True
            if current == target_node:
                current_path.append(current.value)
                print("Path: " + str(' -> '.join(current_path)))
                print("Accumulated cost: " + str(current_cost))
                return True

            # Get neighbors of node and add them to frontier
            neighbors = graph.get_neighbors(current)
            for edge_node, cost in neighbors:
                if edge_node.discovered != True:
                    new_cost = current_cost + cost
                    new_path = current_path.copy()
                    new_path.append(current.value)
                    frontier.put((new_cost, (edge_node, new_path)))
    return print("Not found.")

if __name__ == "__main__":
    graph = Graph()
    graph.load_data('tour_romania.json')
    ucs_search(graph, "Arad", "Bucharest")
