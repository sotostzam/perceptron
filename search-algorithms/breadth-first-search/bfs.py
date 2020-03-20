import json

class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.discovered = False
        self.parent = None

class Graph:
    def __init__(self):
        self.nodes = []
        self.start = None
        self.target = None

    def getNode(self, value):
        for i in self.nodes:
            if i.value == value:
                return i

    def bfs_search(self, start_Node, target_Node):
        queue = []
        queue.append(start_Node)
        start_Node.discovered = True
        while queue:
            current = queue.pop(0)
            if current == target_Node:
                break
            for edge in current.edges:
                if edge.discovered != True:
                    edge.discovered = True
                    edge.parent = current
                    queue.append(edge)

        # Print the path that BFS followed
        path = []
        path.append(current.value)
        while current.parent:
            path.append(current.parent.value)
            current = current.parent
        path.reverse()
        bfs_path = ""
        for node in path:
            bfs_path += node + " -> "
        print("Path: " + bfs_path[0: -4])

graph = Graph()

with open('search-algorithms/breadth-first-search/data.json') as json_file:
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
graph.bfs_search(start_Node, target_Node)
