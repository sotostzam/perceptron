import tkinter as tk
import random, math

class Node:
    def __init__(self, x, y, obj):
        self.x = x                  # Node's canvas x value
        self.y = y                  # Node's canvas y value
        self.obj = obj              # Canvas object ID number
        self.neighbors = []         # List of neighbor nodes
        self.cameFrom = None        # Parent node comming from the cheapest path from start

    # Rich comparison method called by x < y
    def __lt__(self, other):
        # Compare nodes based on their fScore value (used by priority queue)
        return self.x < other.x

class Graph():
    def __init__(self, num):
        self.width  = 400
        self.height = 400
        self.nodes = []

        self.window = tk.Tk()
        self.window.title("Traveling Salesman Problem using genetic algorithm")

        self.canvas_left = tk.Canvas(master = self.window, width = self.width, height = self.height, bg = "white")
        self.canvas_left.grid(row = 1, column = 0, sticky = "nsew")

        self.canvas_right = tk.Canvas(master = self.window, width = self.width, height = self.height, bg = "white")
        self.canvas_right.grid(row = 1, column = 1, sticky = "nsew")

        # Path canvas objects
        self.best_path_obj = None
        self.current_path_obj = None

        for _ in range(0, num):
            x = random.randrange(0, self.width)
            y = random.randrange(0, self.height)
            obj = self.canvas_left.create_rectangle(x - 10, y - 10, x + 10, y + 10, fill="blue", outline="red", width=5)
            self.canvas_right.create_rectangle(x - 10, y - 10, x + 10, y + 10, fill="blue", outline="green", width=5)
            new_node = Node(x, y, obj)
            self.nodes.append(new_node)

    def update_current_path(self, path):
        self.canvas_left.delete(self.current_path_obj)
        self.current_path_obj = self.canvas_left.create_line(path, width = 2, fill = 'red')
        self.canvas_left.tag_lower(self.current_path_obj)

    def update_best_path(self, path):
        self.canvas_right.delete(self.best_path_obj)
        self.best_path_obj = self.canvas_right.create_line(path, width = 2, fill = 'green')
        self.canvas_right.tag_lower(self.best_path_obj)

class Population:
    def __init__(self, nodes):
        self.nodes = nodes
        self.distance = 0
        self.fitness = 0

# Create population object and find fitness
def get_population(nodes, num):
    population_list = []
    for _ in range(num):
        current_pop = Population(nodes)
        random.shuffle(current_pop.nodes)
        population_list.append(current_pop)
    return population_list

# Euclidean Distance between two points
def euclidean_distance(node_1, node_2):
    distance = math.sqrt((node_2.x - node_1.x)**2 + (node_2.y - node_1.y)**2)
    return distance

# Total distance for a path of nodes
def get_total_distance(node_list):
    total_distance = 0
    for i in range(0, len(node_list)-2):
        total_distance += euclidean_distance(node_list[i], node_list[i+1])
    return total_distance
