import tkinter as tk
import random, time

class Node():
    def __init__(self, obj, number, pos = None):
        self.obj = obj
        self.number = number
        self.pos = pos

class Board():
    def __init__(self, num):
        self.grid = []
        self.queens = []

        # Window and canvas initialization parameters
        self.size  = num * 100
        self.s = self.size / num
        self.window = tk.Tk()
        self.window.title(str(num) + " Queen Problem")
        self.canvas = tk.Canvas(master = self.window, width = self.size, height = self.size, bg = "white")
        self.canvas.grid(row = 0, column = 0, sticky = "nsew")

        for col in range(num):
            x = ((col * self.s) + (self.s * col + self.s))/2        # FIXME Midpoint
            y = -self.s/2                                           # FIXME Midpoint

            # Initialize queens
            obj =  self.canvas.create_oval(x - self.s/2 + 5, y - self.s/2 + 5, x - self.s/2 - 5, y - self.s/2 - 5, fill="black")
            #canvas.itemconfigure(obj, state='hidden')
            self.queens.append(Node(obj, col, (col, -1)))
            
            tempList = []
            for row in range(num):
                if (col % 2 == 0 and row % 2 == 0) or (col % 2 != 0 and row % 2 != 0):
                    tile = self.canvas.create_rectangle(col * self.s, row * self.s, col * self.s + self.s, row * self.s + self.s, fill = '#f7edcb')
                else:
                    tile = self.canvas.create_rectangle(col * self.s, row * self.s, col * self.s + self.s, row * self.s + self.s, fill = '#66442e')
                self.canvas.tag_lower(tile)
                tempList.append([])
            self.grid.append(tempList)

        # self.move_queen(self.queens[0], (0, 3))
        # self.move_queen(self.queens[1], (1, 2))

    def move_queen(self, queen, pos):
        pass
        # print(queen.pos)
        # current_pos = queen.pos
        # while current_pos[0] != pos[0] or current_pos[1] != pos[1]:
        #     if current_pos[0] != pos[0]:
        #         print("Move right")
        #         self.canvas.move(queen.obj, self.s, 0)
        #     if current_pos[1] != pos[1]:
        #         print("Move down")
        #         self.canvas.move(queen.obj, 0, self.s)
        #     self.canvas.update()
        #     time.sleep(1)
