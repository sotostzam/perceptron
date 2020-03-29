import tkinter as tk
import time, math
import heapq

class Node:
    def __init__(self, x, y, col, row, obj):
        self.x = x
        self.y = y
        self.col = col
        self.row = row
        self.obj = obj
        self.neighbors = []
        self.gScore = 0         # gScore
        self.fScore = 0         # Both
        self.cameFrom = None

    # Rich comparison method called by x < y 
    def __lt__(self, other):
        # Returns priority based on alphabetical order
        return self.gScore < other.gScore

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
                obj = self.canvas.create_oval(col * self.w, row * self.h, self.w * col + self.w, self.h * row + self.h, fill="grey")
                new_node = Node(x, y, col, row, obj)
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

    def evaluate(self, node_1, node_2):
        # Euclidean distance
        return math.sqrt((node_2.x - node_1.x)**2 + (node_2.y - node_1.y)**2)

def a_star(maze):
    start = maze.grid[0][0]
    goal = maze.grid[len(maze.grid)-1][len(maze.grid[0])-1]

    start.gScore = 0
    start.fScore = maze.evaluate(start, goal)

    # The set of discovered nodes that may need to be (re-)expanded
    openSet = []
    # openSet is a tuple of (priority, (node, total_cost))
    heapq.heappush(openSet, (start.gScore + start.fScore, start))

    # List of nodes already discovered and explored
    closedSet = []

    while openSet:
        _ , current = heapq.heappop(openSet)
        if current is goal:
            path = []
            temp = current
            path.append(temp)
            # while temp.cameFrom != None:
            #     print(temp.cameFrom)
            #     path.append(temp.cameFrom)
            #     temp = temp.cameFrom
            for node in path:
                maze.canvas.itemconfig(node.obj, fill='blue')
            return True
        closedSet.append(current)

        for neighbor in current.neighbors:
            # tentative_gScore = current.gScore + maze.evaluate(current, neighbor)
            #             # FIXME
            # if tentative_gScore < neighbor.gScore:
            #     neighbor.cameFrom = current
            #     neighbor.gScore = tentative_gScore
            #     neighbor.fScore = neighbor.gScore + maze.evaluate(neighbor, goal)
            #     print(neighbor.fScore)
            # if neighbor not in closedSet:
            #     heapq.heappush(openSet, (neighbor.fScore, neighbor))
            
            tempG = neighbor.gScore
            if neighbor in openSet:
                if tempG < neighbor.gScore:
                    neighbor.gScore = tempG
            else:
                neighbor.cameFrom = current
                neighbor.gScore = tempG
                neighbor.fScore = neighbor.gScore + maze.evaluate(neighbor, goal)
                heapq.heappush(openSet, (neighbor.fScore, neighbor))
                #maze.canvas.itemconfig(neighbor.obj, fill='green')

        for node in openSet:
            maze.canvas.itemconfig(node[1].obj, fill='green')
        for node in closedSet:
            maze.canvas.itemconfig(node.obj, fill='red')

        maze.canvas.update()
        time.sleep(.05)
    return False

if __name__ == "__main__":
    maze = Maze(500, 500, 20, 20)
    a_star(maze)
    maze.window.mainloop()
