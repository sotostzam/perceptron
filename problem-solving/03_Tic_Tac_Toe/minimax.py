import random, math
import game

# Scores
scores = {
    0:  1,      # Player 0 Won
    1: -1,      # Player 1 Won
    2:  0       # Draw
}

def bestMove(board, player):
    bestScore = -math.inf
    next_move = None
    moves = board.get_available_moves()
    for move in moves:
        board.board[move[0]][move[1]] = game.Node(None, 0)
        score = minimax(board, 0, False)
        board.board[move[0]][move[1]] = None
        if score > bestScore:
            bestScore = score
            next_move  = move
    board.play(0, next_move)
    board.canvas.update()
    status = board.check_status()
    if status is None:
        if player is board.players[0]:
            player = board.players[1]
        else:
            player = board.players[0]
    else:
        print("Winner is: Player " + str(status))

def randomPlay(board, player):
    moves = board.get_available_moves()
    if not moves:
        return False
    else:
        move = random.choice(moves)
        if move is False:
            print("Draw! Noone wins.")
        else:
            board.play(0, move)
            board.canvas.update()
            status = board.check_status()
            if status is None:
                if player is board.players[0]:
                    player = board.players[1]
                else:
                    player = board.players[0]
            else:
                print("Winner is: Player " + str(status))

def minimax(board, depth, maximizingPlayer):
    print(depth)
    status = board.check_status()
    if status is not None:
        return scores[status]
    if maximizingPlayer:
        value = -math.inf
        moves = board.get_available_moves()
        for move in moves:
            board.board[move[0]][move[1]] = game.Node(None, 0)
            value = max(value, minimax(board, depth + 1, False))
            board.board[move[0]][move[1]] = None
        return value
    else:
        value = math.inf
        moves = board.get_available_moves()
        for move in moves:
            board.board[move[0]][move[1]] = game.Node(None, 1)
            value = min(value, minimax(board, depth + 1, True))
            board.board[move[0]][move[1]] = None
        return value
    return 0