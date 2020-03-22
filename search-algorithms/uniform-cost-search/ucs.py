import json
from queue import PriorityQueue

class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.discovered = False
        self.parent = []

    def get_cost(self, target):
        for edge in self.edges:
            if edge['node'] == target:
                return edge['cost']

class Graph:
    def __init__(self):
        self.nodes = []
        self.start = None
        self.target = None

    def getNode(self, value):
        for i in self.nodes:
            if i.value == value:
                return i

    def ucs_search(self, start_Node, target_Node):
        frontier = PriorityQueue()
        frontier.put((0, start_Node))
        while frontier:
            current_cost, current =  frontier.get()
            if current.discovered != True:
                current.discovered = True
                if current == target_Node:
                    return print("Path found with cost: " + str(current_cost))
                for edge in current.edges:
                    if edge['node'].discovered != True:
                        edge['node'].parent.append(current)
                        new_cost = current_cost + current.get_cost(edge['node'])
                        #print(current.value + " -> " + edge['node'].value + " with total cost: " + str(new_cost))
                        frontier.put((new_cost, edge['node']))


graph = Graph()

with open('data.json') as json_file:
    data = json.load(json_file)
    for i in data:
        node = Node(i)
        for j in data[i]:
            for k in j:
                item = {"node": k, "cost": j[k]}
                node.edges.append(item)
        graph.nodes.append(node)

    # Replace any edge with the respective node object
    for node in graph.nodes:
        for edge in range(0, len(node.edges)):
            for i in graph.nodes:
                if node.edges[edge]['node'] == i.value:
                     node.edges[edge]['node'] = i

start_Node  = graph.getNode("A")
target_Node = graph.getNode("G")

graph.ucs_search(start_Node, target_Node)
