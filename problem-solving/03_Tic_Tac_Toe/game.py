import tkinter as tk
import math, random

class Node():
    def __init__(self, obj, value):
        self.value = value
        self.obj = obj

class TicTacToe():
    def __init__(self):
        self.width  = 400
        self.height = 400

        self.w = self.width / 3
        self.h = self.height / 3

        self.window = tk.Tk()
        self.window.title("Tic Tac Toe Minimax and Alpha-Beta prunning")

        self.canvas = tk.Canvas(master = self.window, width = self.width, height = self.height, bg = "white")
        self.canvas.grid(row = 0, column = 0, sticky = "nsew")

        self.board = []
        self.players = [0, 1]  # 0 is circle, 1 is X

        # Create grid lines
        self.canvas.create_line(self.w, 0, self.w, self.height, width = 4, fill = 'black')
        self.canvas.create_line(self.w * 2, 0, self.w * 2, self.height, width = 4, fill = 'black')
        self.canvas.create_line(0, self.h, self.width, self.h, width = 4, fill = 'black')
        self.canvas.create_line(0, self.h * 2, self.width, self.h * 2, width = 4, fill = 'black')

        for _ in range(0, 3):
            temp_list = [None, None, None]
            self.board.append(temp_list)

        # Bind Events
        self.canvas.bind("<Button 1>", lambda event : self.insert(event, 0))
        self.canvas.bind("<Button 3>", lambda event : self.insert(event, 1))

    def insert(self, event, item):
        # FIXME Check if grid contains item already
        x = math.floor(event.x / self.w)
        y = math.floor(event.y / self.h)
        mid_x = (x * self.w + (x * self.w + self.w))/2
        mid_y = (y * self.h + (y * self.h + self.h))/2
        if item is 0:
            obj = self.canvas.create_text(mid_x, mid_y, font=("Purisa", 60), text = "O", fill="blue")
        else:
            obj = self.canvas.create_text(mid_x, mid_y, font=("Purisa", 60), text = "X", fill="red")
        self.board[y][x] = Node(obj, 0) #FIXME
        #print(" Row: " + str(y) + " Col: " + str(x))
        #print(self.grid[x][y])
        self.get_board_state()

    def get_board_state(self):
        state = []
        for col in range(0, len(self.board)):
            for row in range(0, len(self.board[col])):
                if self.board[col][row] is None:
                    state.append([col, row])
        return state

    def check_status(self):
        for col in self.board:
            if col[0] != None and col[1] != None and col[2] != None:
                if col[0].value == col[1].value == col[2].value:
                    return col[0].value

        for row in range(0, len(self.board)):
            if self.board[0][row] != None and self.board[1][row] != None and self.board[2][row] != None:
                if self.board[0][row].value == self.board[1][row].value == self.board[2][row].value:
                    return self.board[0][row].value

        if self.board[0][0] != None and self.board[1][1] != None and self.board[2][2] != None:
            if self.board[0][0].value == self.board[1][1].value == self.board[2][2].value:
                return self.board[0][0].value

        if self.board[2][0] != None and self.board[1][1] != None and self.board[0][2] != None:
            if self.board[2][0].value == self.board[1][1].value == self.board[0][2].value:
                return self.board[2][0].value

        return False

    def play(self, player):
        current_state = self.get_board_state()
        if not current_state:
            return False
        else:
            move = random.choice(current_state)
            mid_x = (move[0] * self.w + (move[0] * self.w + self.w))/2
            mid_y = (move[1] * self.h + (move[1] * self.h + self.h))/2
            if player is 0:
                value = 0
                obj = self.canvas.create_text(mid_x, mid_y, font=("Purisa", 60), text = "O", fill="blue")
                self.board[move[0]][move[1]] = Node(obj, value)
            else:
                value = 1
                obj = self.canvas.create_text(mid_x, mid_y, font=("Purisa", 60), text = "X", fill="red")
                self.board[move[0]][move[1]] = Node(obj, value)

            status = self.check_status()
            if status is not False:
                return status
            
            return True