import json, math

class Node:
    def __init__(self, value, x = None, y = None, obj = None):
        self.value = value
        self.discovered = False
        self.x = x
        self.y = y
        self.obj = obj

    # Rich comparison method called by x < y 
    def __lt__(self, other):
        # Returns priority based on alphabetical order
        return self.value < other.value

class Graph:
    def __init__(self):
        self.nodes        = []
        self.edges        = []

    # Function to fill graph from dataset
    def load_data(self, path, canvas):
        with open(path) as json_file:
            data = json.load(json_file)
            # Loop through the vertices
            for vertice in data:
                x_coord = data[vertice]['x']
                y_coord = data[vertice]['y']
                node = self.add_node(vertice, x_coord, y_coord, canvas)
                # Loop through the edges
                for edge in data[vertice]['Edges']:
                    # Loop through the keys (1 Iteration only)
                    for node_name in edge:
                        self.add_edge(node, self.add_node(node_name, data[node_name]['x'], data[node_name]['y'], canvas), edge[node_name], canvas)

    # Helper function to check regulate node's creation
    def add_node(self, value, x, y, canvas):
        for node in self.nodes:
            if node.value == value:
                return node
        obj = canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="grey")
        new_node = Node(value, x, y, obj)
        self.nodes.append(new_node)
        return new_node
    
    # Helper function to check regulate edge's creation
    def add_edge(self, node1, node2, cost, canvas):
        for edge in self.edges:
            if edge[0] == node2 and edge[1] == node1:
                return False
        obj = canvas.create_line(node1.x, node1.y, node2.x, node2.y, width = 3, fill='black')
        canvas.tag_lower(obj)
        self.edges.append((node1, node2, cost, obj))
        return True

    # Function returning a list of adjacent nodes
    def get_neighbors(self, node):
        neighbors = []
        for edge in self.edges:
            if node == edge[0]:
                neighbors.append((edge[1], edge[2]))
            if node == edge[1]:
                neighbors.append((edge[0], edge[2]))
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

    # Heuristic function returning the distance from origin to target node
    def evaluate(self, node_1, node_2):
        distance = math.sqrt((node_2.x - node_1.x)**2 + (node_2.y - node_1.y)**2)   # Euclidean distance
        # distance = abs((node_1.x - node_2.x)) + abs((node_1.y - node_2.y))        # Manhattan distance
        return distance

    # Helper function to provide additional info for tour_romania file
    def show_info(self, canvas):
        # Names of cities
        canvas.create_text(30, 160, font=("Purisa", 10, 'bold'), text = "Arad")
        canvas.create_text(560, 420, font=("Purisa", 10, 'bold'), text = "Bucharest")
        canvas.create_text(300, 485, font=("Purisa", 10, 'bold'), text = "Craiova")
        canvas.create_text(135, 445, font=("Purisa", 10, 'bold'), text = "Drobeta")
        canvas.create_text(765, 475, font=("Purisa", 10, 'bold'), text = "Eforie")
        canvas.create_text(400, 195, font=("Purisa", 10, 'bold'), text = "Fagaras")
        canvas.create_text(525, 485, font=("Purisa", 10, 'bold'), text = "Giurgiu")
        canvas.create_text(760, 370, font=("Purisa", 10, 'bold'), text = "Hirsova")
        canvas.create_text(665, 135, font=("Purisa", 10, 'bold'), text = "Iasi")
        canvas.create_text(210, 325, font=("Purisa", 10, 'bold'), text = "Lugoj")
        canvas.create_text(225, 385, font=("Purisa", 10, 'bold'), text = "Mehadia")
        canvas.create_text(530, 70, font=("Purisa", 10, 'bold'), text = "Neamt")
        canvas.create_text(165, 40, font=("Purisa", 10, 'bold'), text = "Oradea")
        canvas.create_text(420, 325, font=("Purisa", 10, 'bold'), text = "Pitesti")
        canvas.create_text(335, 265, font=("Purisa", 10, 'bold'), text = "Rimnicu_Vilcea")
        canvas.create_text(260, 190, font=("Purisa", 10, 'bold'), text = "Sibiu")
        canvas.create_text(115, 270, font=("Purisa", 10, 'bold'), text = "Timisoara")
        canvas.create_text(640, 390, font=("Purisa", 10, 'bold'), text = "Urziceni")
        canvas.create_text(720, 225, font=("Purisa", 10, 'bold'), text = "Vaslui")
        canvas.create_text(125, 115, font=("Purisa", 10, 'bold'), text = "Zerind")
        # Value of edges
        canvas.create_text(60, 125, font=("Purisa", 10), text = "75")
        canvas.create_text(95, 65, font=("Purisa", 10), text = "71")
        canvas.create_text(150, 170, font=("Purisa", 10), text = "140")
        canvas.create_text(45, 220, font=("Purisa", 10), text = "118")
        canvas.create_text(200, 120, font=("Purisa", 10), text = "151")
        canvas.create_text(312, 200, font=("Purisa", 10), text = "99")
        canvas.create_text(475, 305, font=("Purisa", 10), text = "211")
        canvas.create_text(120, 320, font=("Purisa", 10), text = "111")
        canvas.create_text(165, 355, font=("Purisa", 10), text = "70")
        canvas.create_text(165, 415, font=("Purisa", 10), text = "75")
        canvas.create_text(235, 440, font=("Purisa", 10), text = "120")
        canvas.create_text(360, 420, font=("Purisa", 10), text = "138")
        canvas.create_text(305, 370, font=("Purisa", 10), text = "146")
        canvas.create_text(240, 250, font=("Purisa", 10), text = "80")
        canvas.create_text(340, 330, font=("Purisa", 10), text = "97")
        canvas.create_text(460, 390, font=("Purisa", 10), text = "101")
        canvas.create_text(520, 450, font=("Purisa", 10), text = "90")
        canvas.create_text(560, 375, font=("Purisa", 10), text = "85")
        canvas.create_text(665, 355, font=("Purisa", 10), text = "98")
        canvas.create_text(760, 410, font=("Purisa", 10), text = "86")
        canvas.create_text(665, 300, font=("Purisa", 10), text = "142")
        canvas.create_text(675, 175, font=("Purisa", 10), text = "92")
        canvas.create_text(585, 100, font=("Purisa", 10), text = "87")
