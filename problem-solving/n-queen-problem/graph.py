import tkinter as tk
import random

class Node():
    def __init__(self, obj, num, pos, domain):
        self.obj    = obj      # Canvas object ID
        self.num    = num      # Queen number (column)
        self.pos    = pos      # Queen current position (row number)
        self.domain = domain   # Domain of the Queen

class Board():
    def __init__(self, num):
        self.grid   = []
        self.queens = []

        # Window and canvas initialization parameters
        self.size  = num * 100
        self.s = self.size / num
        self.window = tk.Tk()
        self.window.title(str(num) + ' Queen Problem')
        self.canvas = tk.Canvas(master = self.window, width = self.size, height = self.size, bg = 'white')
        self.canvas.grid(row = 0, column = 0, sticky = 'nsew')
        self.queen_image = tk.PhotoImage(file = 'queen.png')

        # Initialize checkerboard
        for col in range(num):            
            tempList = []
            for row in range(num):
                if (col % 2 == 0 and row % 2 == 0) or (col % 2 != 0 and row % 2 != 0):
                    tile = self.canvas.create_rectangle(col * self.s, row * self.s, col * self.s + self.s, row * self.s + self.s, fill = '#f7edcb')
                else:
                    tile = self.canvas.create_rectangle(col * self.s, row * self.s, col * self.s + self.s, row * self.s + self.s, fill = '#66442e')
                self.canvas.tag_lower(tile)
                tempList.append(0)
            self.grid.append(tempList)

            # Initialize queens
            init_pos = ((col * self.s) + (self.s * col + self.s))/2
            obj = self.canvas.create_image(init_pos, -self.s/2, image = self.queen_image)
            self.queens.append(Node(obj, col + 1, -1, list(range(0, num))))

    # Helper function to return next unassigned queen
    def get_unassigned_queen(self):
        for queen in self.queens:
            if queen.pos == -1:
                return queen

    # Helper function to move a queen among rows
    def place_queen(self, queen, pos):
        _ , queen_y = self.canvas.coords(queen.obj)
        new_y  = ((pos * self.s) + (self.s * pos + self.s)) / 2
        move_y = new_y - queen_y

        # Create the moving animation
        while move_y != 0:
            if move_y > 0:
                self.canvas.move(queen.obj, 0, 25)
                move_y -= 25
            elif move_y < 0:
                self.canvas.move(queen.obj, 0, -25)
                move_y += 25
            self.canvas.after(10, self.canvas.update())

        # Change queen's location in the grid
        self.grid[queen.num-1][queen.pos] = 0
        queen.pos = pos
        if pos >= 0:
            self.grid[queen.num-1][queen.pos] = queen.num

    # Helper finction to reset/move a queen out of the canvas
    def reset_queen(self, queen):
        self.place_queen(queen, -1)

    # Helper function to check if queen is taking a valid move
    def is_valid_move(self, queen, pos):
        for i in range(len(self.grid)):
            if self.grid[i][pos] != 0 and i != queen.num-1:
                return False

        # Upper diagonal
        temp_col = queen.num - 2
        temp_row = pos - 1
        while temp_row >= 0 and temp_col >= 0:
            if self.grid[temp_col][temp_row] != 0:
                return False
            temp_col -= 1
            temp_row -= 1

        # Lower diagonal
        temp_col = queen.num - 2
        temp_row = pos + 1
        while temp_row < len(self.grid) and temp_col >= 0:
            if self.grid[temp_col][temp_row] != 0:
                return False
            temp_col -= 1
            temp_row += 1
        return True
        