import json

class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.discovered = False

class Graph:
    def __init__(self):
        self.nodes = []
        self.start = None
        self.target = None

    def getNode(self, value):
        for i in self.nodes:
            if i.value == value:
                return i

    def dfs_search(self, start_Node, target_Node):
        stack = []                  # Create stack LIFO (Last in first out)
        stack.append(start_Node)
        found = False
        path = ""
        while stack:
            current = stack.pop()
            if current.discovered != True:
                current.discovered = True
                path += current.value + " -> "
                if current == target_Node:
                    found = True
                    break
                # Iterate all the children backwards to fill stack correctly
                for i in range(len(current.edges)-1, -1, -1):
                    stack.append(current.edges[i])
        print("Path: " + path[0: -4])
        if found:
            print("Target found!")
        else:
            print("Target not found!")

graph = Graph()

with open('data.json') as json_file:
    data = json.load(json_file)
    for i in data:
        node = Node(i)
        for j in data[i]:
            node.edges.append(j)
        graph.nodes.append(node)

    # Replace any edge with the respective node object
    for node in graph.nodes:
        for edge in range(0, len(node.edges)):
            for i in graph.nodes:
                if node.edges[edge] == i.value:
                     node.edges[edge] = i

start_Node  = graph.getNode("A")
target_Node = graph.getNode("J")
graph.dfs_search(start_Node, target_Node)
