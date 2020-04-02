import tkinter as tk
import math, random, time
import minimax

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

    # Player makes a move by selecting a tile
    def insert(self, event, item):
        x = math.floor(event.x / self.w)
        y = math.floor(event.y / self.h)
        if self.board[x][y] is None:
            mid_x = (x * self.w + (x * self.w + self.w))/2
            mid_y = (y * self.h + (y * self.h + self.h))/2
            obj = self.canvas.create_text(mid_x, mid_y, font=("Purisa", 60), text = "X", fill="red")
            self.board[x][y] = Node(obj, 1)
            self.canvas.update()

            # Check if winner is found after Player makes a move
            status, points = self.check_status()
            if status is not None:
                if status is not 2:
                    self.calculate_line(points[0], points[1])
                    print("Winner is: Player " + str(status))
                else:
                    print("Draw! No winner.")
            else:
                minimax.bestMove(self)

    # Get tiles with available movement
    def get_available_moves(self):
        state = []
        for col in range(0, len(self.board)):
            for row in range(0, len(self.board[col])):
                if self.board[col][row] is None:
                    state.append([col, row])
        return state

    # Helper function check if 3 items are equal
    def is_equal(self, item_1, item_2, item_3):
        return item_1.value is item_2.value and item_2.value is item_3.value and item_1.value is item_3.value

    # Create and display line crossing the three tiles
    def calculate_line(self, point_1, point_2):
        x1 = (point_1[0] * self.w + (point_1[0] * self.w + self.w))/2
        y1 = (point_1[1] * self.h + (point_1[1] * self.h + self.h))/2
        x2 = (point_2[0] * self.w + (point_2[0] * self.w + self.w))/2
        y2 = (point_2[1] * self.h + (point_2[1] * self.h + self.h))/2
        self.canvas.create_line(x1, y1, x2, y2, width = 4, fill = 'black')

    # Check if there is a winner either vertically, horizontally or diagonally
    def check_status(self):
        winner = None
        points = []
        for col in range(0, len(self.board)):
            if self.board[col][0] and self.board[col][1] and self.board[col][2] and self.is_equal(self.board[col][0], self.board[col][1], self.board[col][2]):
                winner = self.board[col][0].value
                points = ([col, 0], [col, 2])
        for row in range(0, len(self.board[0])):
            if self.board[0][row] and self.board[1][row] and self.board[2][row] and self.is_equal(self.board[0][row], self.board[1][row], self.board[2][row]):
                winner = self.board[0][row].value
                points = ([0, row], [2, row])
        if self.board[0][0] and self.board[1][1] and self.board[2][2] and self.is_equal(self.board[0][0], self.board[1][1], self.board[2][2]):
            winner = self.board[0][0].value
            points = ([0, 0], [2, 2])
        if self.board[2][0] and self.board[1][1] and self.board[0][2] and self.is_equal(self.board[2][0], self.board[1][1], self.board[0][2]):
            winner = self.board[2][0].value
            points = ([2, 0], [0, 2])

        if winner is None and len(self.get_available_moves()) is 0:
            return 2, points
        else:
            return winner, points

    # Function to make a move with the player as parameter
    def play(self, player, move):
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
