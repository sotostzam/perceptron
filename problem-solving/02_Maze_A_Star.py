import tkinter as tk
import time, math, random
import heapq

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
                obj = self.canvas.create_rectangle(col * self.w, row * self.h, self.w * col + self.w, self.h * row + self.h, fill="grey")
                new_node = Node(x, y, col, row, obj)
                if random.uniform(0, 1) < 0.3:
                    new_node.obstacle = True
                    self.canvas.itemconfig(new_node.obj, fill='black')
                current_row.append(new_node)

        # Add node's neighbors
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[i])):
                if i < grid_w - 1:
                    self.grid[i][j].neighbors.append(self.grid[i+1][j])
                if i > 0:
                    self.grid[i][j].neighbors.append(self.grid[i-1][j])
                if j < grid_h - 1:
                    self.grid[i][j].neighbors.append(self.grid[i][j + 1])
                if j > 0:
                    self.grid[i][j].neighbors.append(self.grid[i][j - 1])

                # Diagonals
                if i > 0 and j > 0:
                    self.grid[i][j].neighbors.append(self.grid[i - 1][j - 1])
                if i < grid_w - 1 and j > 0:
                    self.grid[i][j].neighbors.append(self.grid[i + 1][j - 1])
                if i > 0 and j < grid_h - 1:
                    self.grid[i][j].neighbors.append(self.grid[i - 1][j + 1])
                if i < grid_w - 1 and j < grid_h - 1:
                    self.grid[i][j].neighbors.append(self.grid[i + 1][j + 1])

    def evaluate(self, node_1, node_2):
        distance = math.sqrt((node_2.x - node_1.x)**2 + (node_2.y - node_1.y)**2)   # Euclidean distance
        # distance = abs((node_1.x - node_2.x)) + abs((node_1.y - node_2.y))        # Manhattan distance
        return distance

def a_star(maze):
    start = maze.grid[0][0]
    goal = maze.grid[len(maze.grid)-1][len(maze.grid[0])-1]
    start.obstacle = False
    goal.obstacle = False

    start.gScore = 0
    start.fScore = maze.evaluate(start, goal)

    # The set of discovered nodes that may need to be (re-)expanded
    openSet = []
    heapq.heappush(openSet, start)

    # List of nodes already discovered and explored
    closedSet = []

    while openSet:
        current = heapq.heappop(openSet)

######################### CANVAS UPDATE ############################
        for node in openSet:
            maze.canvas.itemconfig(node.obj, fill='green')
        for node in closedSet:
            maze.canvas.itemconfig(node.obj, fill='red')
        path = []
        temp = current
        path.append(temp)
        while temp.cameFrom != None:
            path.append(temp.cameFrom)
            temp = temp.cameFrom
        for node in path:
            maze.canvas.itemconfig(node.obj, fill='blue')

        if current is goal:
            return True
        closedSet.append(current)
#####################################################################

        for neighbor in current.neighbors:
            if not neighbor in closedSet and not neighbor.obstacle:
                tentative_gScore = current.gScore + maze.evaluate(current, neighbor)
                # Check if neighbor is found with better gScore
                if neighbor in openSet:
                    if tentative_gScore < neighbor.gScore:
                        neighbor.gScore = tentative_gScore
                        neighbor.cameFrom = current
                else:
                    neighbor.gScore = tentative_gScore
                    neighbor.fScore = neighbor.gScore + maze.evaluate(neighbor, goal)
                    neighbor.cameFrom = current
                    heapq.heappush(openSet, neighbor)
            
            # if tentative_gScore < neighbor.gScore:
            #     neighbor.cameFrom = current
            #     neighbor.gScore = tentative_gScore
            #     neighbor.fScore = neighbor.gScore + maze.evaluate(neighbor, goal)
            #     print(neighbor.fScore)
            # if neighbor not in closedSet:
            #     heapq.heappush(openSet, (neighbor.fScore, neighbor))
            
            # tempG = neighbor.gScore
            # if neighbor in openSet:
            #     if tempG < neighbor.gScore:
            #         neighbor.gScore = tempG
            # else:
            #     neighbor.cameFrom = current
            #     neighbor.gScore = tempG
            #     neighbor.fScore = neighbor.gScore + maze.evaluate(neighbor, goal)
            #     heapq.heappush(openSet, neighbor)
                #maze.canvas.itemconfig(neighbor.obj, fill='green')

        maze.canvas.update()
    return False

if __name__ == "__main__":
    maze = Maze(500, 500, 50, 50)
    result = a_star(maze)
    maze.window.mainloop()
