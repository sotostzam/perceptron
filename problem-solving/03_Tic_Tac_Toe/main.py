import game
import time, random

def minimax():
    pass

if __name__ == "__main__":
    board = game.TicTacToe()

    current_player = random.choice(board.players)
    keepPlaying = True

    while keepPlaying:
        status = board.play(current_player)
        board.canvas.update()

        if status is True:
            if current_player is board.players[0]:
                current_player = board.players[1]
            else:
                current_player = board.players[0]
            time.sleep(0.1)
        elif status is not False:
            print("Winner is: Player " + str(status))
            keepPlaying = False
        else:
            print("Draw! Noone wins.")
            keepPlaying = False

    board.window.mainloop()