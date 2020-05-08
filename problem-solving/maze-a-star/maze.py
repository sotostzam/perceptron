import tkinter as tk
import time, math, random

class Node:
    def __init__(self, x, y, col, row, obj):
        self.x = x                  # Node's canvas x value
        self.y = y                  # Node's canvas y value
        self.col = col              # Node's grid col value
        self.row = row              # Node's grid row value
        self.obj = obj              # Canvas object ID number
        self.neighbors = []         # List of neighbor nodes
        self.gScore = math.inf      # gScore is the cost of the cheapest path from start to this node
        self.fScore = math.inf      # fScore = gScore + heuristic of this node
        self.cameFrom = None        # Parent node comming from the cheapest path from start
        self.obstacle = False       # Node identification as obstacle

    # Rich comparison method called by x < y
    def __lt__(self, other):
        # Compare nodes based on their fScore value (used by priority queue)
        return self.fScore < other.fScore

class Maze:

    def __init__(self, width, height, grid_w, grid_h):
        self.pathLine = None

        self.window = tk.Tk()
        self.window.title("A* Path finding algorithm")
        self.canvas = tk.Canvas(master = self.window, width = width, height = height, bg = "white")
        self.canvas.grid(row = 0, column = 0, sticky = "nsew")

        self.w = width / grid_w
        self.h = height / grid_h

        # Initialize 2D grid holding all nodes
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

    def update_path_line(self, path, found = False):
        if len(path) > 2:
            self.canvas.delete(self.pathLine)
            self.pathLine = self.canvas.create_line(path, width = 6, fill = 'purple')
        self.canvas.update()
    
    def set_start(self, pos):
        if self.grid[pos[0]][pos[1]].obstacle:
            self.grid[pos[0]][pos[1]].obstacle = False
            self.canvas.itemconfig(self.grid[pos[0]][pos[1]].obj, fill='white')
        return self.grid[pos[0]][pos[1]]

    def set_goal(self, pos):
        if self.grid[pos[0]][pos[1]].obstacle:
            self.grid[pos[0]][pos[1]].obstacle = False
            self.canvas.itemconfig(self.grid[pos[0]][pos[1]].obj, fill='white')
        return self.grid[pos[0]][pos[1]]
    
    def set_status_closed(self, node):
        self.canvas.itemconfig(node.obj, fill='#ffcccb', outline='')

    def set_status_open(self, node):
        self.canvas.itemconfig(node.obj, fill='#90ee90', outline='')
