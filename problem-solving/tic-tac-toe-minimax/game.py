import tkinter as tk
import math, random
import minimax

class Node:
    def __init__(self, obj, name):
        self.name = name
        self.obj = obj

class TicTacToe:
    def __init__(self):
        self.board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]
        self.players = ['A.I', 'Player']
        
        # Scores
        self.score = {
            self.players[0]:  10,       # A.I Won
            self.players[1]: -10,       # Player Won
            "Draw"         :  0         # Draw
        }
        self.current_player = None
        self.game_on_progress = True

        # Window and canvas initialization parameters
        self.width  = 400
        self.height = 400
        self.w = self.width / 3
        self.h = self.height / 3
        self.window = tk.Tk()
        self.window.title("Minimax with Alpha-Beta Pruning")
        self.canvas = tk.Canvas(master = self.window, width = self.width, height = self.height, bg = "white")
        self.canvas.grid(row = 0, column = 0, sticky = "nsew")

        # Create grid lines
        self.canvas.create_line(self.w, 0, self.w, self.height, width = 4, fill = 'black')
        self.canvas.create_line(self.w * 2, 0, self.w * 2, self.height, width = 4, fill = 'black')
        self.canvas.create_line(0, self.h, self.width, self.h, width = 4, fill = 'black')
        self.canvas.create_line(0, self.h * 2, self.width, self.h * 2, width = 4, fill = 'black')

        # Bind Events
        self.canvas.bind("<Button 1>", lambda event : self.insert(event, 0))

    # Player makes a move by selecting a tile
    def insert(self, event, item):
        x = math.floor(event.x / self.w)
        y = math.floor(event.y / self.h)
        if self.board[x][y] is None and self.game_on_progress and self.current_player is self.players[1]:
            self.play(self.players[1], [x, y])
            if self.game_on_progress:
                minimax.bestMove(self)

    # Get tiles with available movement
    def get_available_moves(self):
        state = []
        for col in range(0, len(self.board)):
            for row in range(0, len(self.board[col])):
                if self.board[col][row] is None:
                    state.append([col, row])
        return state

    # Create and display line crossing the three tiles
    def calculate_line(self, point_1, point_2):
        x1 = (point_1[0] * self.w + (point_1[0] * self.w + self.w))/2
        y1 = (point_1[1] * self.h + (point_1[1] * self.h + self.h))/2
        x2 = (point_2[0] * self.w + (point_2[0] * self.w + self.w))/2
        y2 = (point_2[1] * self.h + (point_2[1] * self.h + self.h))/2
        self.canvas.create_line(x1, y1, x2, y2, width = 5, fill = 'black')

    # Helper function check if 3 items are equal
    def is_equal(self, item_1, item_2, item_3):
        return item_1.name is item_2.name and item_2.name is item_3.name and item_1.name is item_3.name

    # Check if there is a winner either vertically, horizontally or diagonally
    def check_status(self, changeState):
        winner = None
        points = []
        for col in range(0, len(self.board)):
            if self.board[col][0] and self.board[col][1] and self.board[col][2] and self.is_equal(self.board[col][0], self.board[col][1], self.board[col][2]):
                winner = self.board[col][0].name
                points = ([col, 0], [col, 2])
        for row in range(0, len(self.board[0])):
            if self.board[0][row] and self.board[1][row] and self.board[2][row] and self.is_equal(self.board[0][row], self.board[1][row], self.board[2][row]):
                winner = self.board[0][row].name
                points = ([0, row], [2, row])
        if self.board[0][0] and self.board[1][1] and self.board[2][2] and self.is_equal(self.board[0][0], self.board[1][1], self.board[2][2]):
            winner = self.board[0][0].name
            points = ([0, 0], [2, 2])
        if self.board[2][0] and self.board[1][1] and self.board[0][2] and self.is_equal(self.board[2][0], self.board[1][1], self.board[0][2]):
            winner = self.board[2][0].name
            points = ([2, 0], [0, 2])

        # Change game state to "not in progess"
        if changeState:
            if winner is not None:
                self.game_on_progress = False
                self.calculate_line(points[0], points[1])
                print("Winner is: " + self.current_player)
            if len(self.get_available_moves()) is 0:
                self.game_on_progress = False
                print("Draw! No winner.")
        else:
            if winner is None and len(self.get_available_moves()) is 0:
                return "Draw"
            else:
                return winner

    # Function to make a move with the player as parameter
    def play(self, player, move):
        print(str(self.current_player) + " selected tile: " + "[" + str(move[0]) + ", " + str(move[1]) + "] ")
        mid_x = (move[0] * self.w + (move[0] * self.w + self.w))/2
        mid_y = (move[1] * self.h + (move[1] * self.h + self.h))/2
        if player is self.players[0]:
            name = self.players[0]
            obj = self.canvas.create_oval(mid_x-30, mid_y-30, mid_x+30, mid_y+30, fill="white", outline="blue", width = 6)
            self.board[move[0]][move[1]] = Node(obj, name)
        else:
            name = self.players[1]
            obj = self.canvas.create_text(mid_x, mid_y, font=("Purisa", 60), text = "X", fill="red")
            self.board[move[0]][move[1]] = Node(obj, name)        
        self.canvas.update()
        self.check_status(True)     # Check if winner is found after a move
        if self.current_player is self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]
