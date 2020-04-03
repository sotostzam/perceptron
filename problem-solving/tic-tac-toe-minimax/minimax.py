import random, math
import game

# Initial call for the Minimax algorithm
def bestMove(board):
    bestScore = -math.inf
    next_move = None
    moves = board.get_available_moves()
    for move in moves:
        board.board[move[0]][move[1]] = game.Node(None, board.players[0])
        score = minimax(board, 0, False, -math.inf, math.inf)
        board.board[move[0]][move[1]] = None
        if score > bestScore:
            bestScore = score
            next_move  = move
    board.play(board.players[0], next_move)

# Minimax recursive algorithm
def minimax(board, depth, maximizingPlayer, alpha = None, beta = None):
    status = board.check_status(False)
    if status is not None:
        return board.score[status]
    if maximizingPlayer:
        value = -math.inf
        moves = board.get_available_moves()
        for move in moves:
            board.board[move[0]][move[1]] = game.Node(None, board.players[0])
            value = max(value, minimax(board, depth + 1, False, alpha, beta))
            board.board[move[0]][move[1]] = None
            alpha = max(alpha, value)
            if beta <= alpha:
                break               # Beta cut-off
        return value - depth        # Substract depth for shorter path moves
    else:
        value = math.inf
        moves = board.get_available_moves()
        for move in moves:
            board.board[move[0]][move[1]] = game.Node(None, board.players[1])
            value = min(value, minimax(board, depth + 1, True, alpha, beta))
            board.board[move[0]][move[1]] = None
            beta = min(beta, value)
            if beta <= alpha:
                break               # Alpha cut-off
        return value + depth        # Substract depth for shorter path moves
