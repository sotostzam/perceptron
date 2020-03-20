import json

class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.explored = False

class Graph:
    def __init__(self):
        self.nodes = []

    def bfs_search(self, start_Node, target_Node):
        pass

graph = Graph()

with open('search-algorithms/breadth-first-search/data.json') as json_file:
    data = json.load(json_file)
    for i in data:
        node = Node(i)
        for j in data[i]:
            node.edges.append(j)
        graph.nodes.append(node)
