import tkinter as tk
import time, math, random

class Node:
    def __init__(self, x, y, col, row, obj):
        self.x = x
        self.y = y
        self.col = col
        self.row = row
        self.obj = obj
        self.neighbors = []
        self.gScore = math.inf         # gScore
        self.fScore = math.inf         # Both
        self.cameFrom = None
        self.obstacle = False

    # Rich comparison method called by x < y 
    def __lt__(self, other):
        # Returns priority based on alphabetical order
        return self.fScore < other.fScore

class Maze():

    def __init__(self, width, height, grid_w, grid_h):
        self.window = tk.Tk()
        self.window.title("A* Path finding algorithm")
        self.canvas = tk.Canvas(master = self.window, width = width, height = height, bg = "white")
        self.canvas.grid(row = 0, column = 0, sticky = "nsew")

        self.w = width / grid_w
        self.h = height / grid_h

        # Node grid 2D List
        self.grid = []
        for col in range(0, grid_w):
            self.grid.append([])
            current_row = self.grid[col]
            for row in range(0, grid_h):
                x = ((col * self.w) + (self.w * col + self.w))/2
                y = ((row * self.h) + (self.h * row + self.h))/2
                obj = self.canvas.create_oval(col * self.w + 2, row * self.h + 2, self.w * col + self.w - 2, self.h * row + self.h- 2, fill="white", outline="")
                new_node = Node(x, y, col, row, obj)
                if random.uniform(0, 1) < 0.3:
                    new_node.obstacle = True
                    self.canvas.itemconfig(new_node.obj, fill='black')
                current_row.append(new_node)

        # # TEST
        # for i in range(20, 35):
        #     self.grid[i][35].obstacle = True
        #     self.canvas.itemconfig(self.grid[i][35].obj, fill='black')
        # for i in range(15, 36):
        #     self.grid[35][i].obstacle = True
        #     self.canvas.itemconfig(self.grid[35][i].obj, fill='black')


        # Add node's neighbors
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[i])):
                if i < grid_w - 1:
                    if not self.grid[i+1][j].obstacle:
                        self.grid[i][j].neighbors.append(self.grid[i+1][j])
                if i > 0:
                    if not self.grid[i-1][j].obstacle:
                        self.grid[i][j].neighbors.append(self.grid[i-1][j])
                if j < grid_h - 1:
                    if not self.grid[i][j + 1].obstacle:
                        self.grid[i][j].neighbors.append(self.grid[i][j + 1])
                if j > 0:
                    if not self.grid[i][j - 1].obstacle:
                        self.grid[i][j].neighbors.append(self.grid[i][j - 1])

                # Diagonals
                if i > 0 and j > 0:
                    if not self.grid[i-1][j].obstacle or not self.grid[i][j - 1].obstacle:
                        self.grid[i][j].neighbors.append(self.grid[i - 1][j - 1])
                if i < grid_w - 1 and j > 0:
                    if not self.grid[i+1][j].obstacle or not self.grid[i][j - 1].obstacle:
                        self.grid[i][j].neighbors.append(self.grid[i + 1][j - 1])
                if i > 0 and j < grid_h - 1:
                    if not self.grid[i-1][j].obstacle or not self.grid[i][j + 1].obstacle:
                        self.grid[i][j].neighbors.append(self.grid[i - 1][j + 1])
                if i < grid_w - 1 and j < grid_h - 1:
                    if not self.grid[i+1][j].obstacle or not self.grid[i][j + 1].obstacle:
                        self.grid[i][j].neighbors.append(self.grid[i + 1][j + 1])

    def evaluate(self, node_1, node_2):
        distance = math.sqrt((node_2.x - node_1.x)**2 + (node_2.y - node_1.y)**2)   # Euclidean distance
        return distance