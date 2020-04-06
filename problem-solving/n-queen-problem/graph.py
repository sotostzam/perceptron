import tkinter as tk
import random, time

class Node():
    def __init__(self, obj, num, pos):
        self.obj = obj      # Canvas object ID
        self.num = num      # Queen number (column)
        self.pos = pos      # Queen current position (row number)

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
                tempList.append([])
            self.grid.append(tempList)

            # Initialize queens
            init_pos = ((col * self.s) + (self.s * col + self.s))/2
            obj = self.canvas.create_image(init_pos, -self.s/2, image = self.queen_image)
            self.queens.append(Node(obj, col, -1))

        self.move_queen(self.queens[0], 2)
        self.move_queen(self.queens[1], 3)
        self.reset_queen(self.queens[0])

    # Helper function to move a queen among rows
    def move_queen(self, queen, pos):
        _ , queen_y = self.canvas.coords(queen.obj)
        new_y  = ((pos * self.s) + (self.s * pos + self.s)) / 2
        move_y = new_y - queen_y

        # Create the moving animation
        while move_y != 0:
            if move_y > 0:
                self.canvas.move(queen.obj, 0, 10)
                move_y -= 10
            elif move_y < 0:
                self.canvas.move(queen.obj, 0, -10)
                move_y += 10
            time.sleep(0.05)
            self.canvas.update()
        queen.pos = pos

    # Helper finction to reset/move a queen out of the canvas
    def reset_queen(self, queen):
        self.move_queen(queen, -1)
