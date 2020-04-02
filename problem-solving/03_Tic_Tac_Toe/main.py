import game, minimax
import random

def main():
    board = game.TicTacToe()
    board.current_player = random.choice((0, 1))

    if board.current_player is 0:
        board.current_player = board.players[0]
        print("A.I plays first.\nThinking...")
        minimax.bestMove(board)
    else:
        board.current_player = board.players[1]
        print("Human plays first. Please select your move.")

    board.window.mainloop()

if __name__ == "__main__":
    main()