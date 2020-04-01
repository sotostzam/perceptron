import game, minimax
import random

if __name__ == "__main__":
    board = game.TicTacToe()
    current_player = random.choice(board.players)

    if current_player is 0:
        minimax.bestMove(board, 0)

    board.window.mainloop()