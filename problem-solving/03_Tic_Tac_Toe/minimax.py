import random, math
import game

# Scores
scores = {
    0:  10,      # Player 0 Won
    1: -10,      # Player 1 Won
    2:  0        # Draw
}

# Initial call for the Minimax algorithm
def bestMove(board):
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

    # Check if winner is found after AI makes a move
    status, points = board.check_status()
    if status is not None:
        if status is not 2:
            board.calculate_line(points[0], points[1])
            print("Winner is: " + board.current_player)
            board.game_on_progress = False
        else:
            print("Draw! No winner.")

    board.current_player = "Player"

# Minimax recursive algorithm
def minimax(board, depth, maximizingPlayer):
    status, _ = board.check_status()
    if status is not None:
        return scores[status]
    if maximizingPlayer:
        value = -math.inf
        moves = board.get_available_moves()
        for move in moves:
            board.board[move[0]][move[1]] = game.Node(None, 0)
            value = max(value, minimax(board, depth + 1, False))
            board.board[move[0]][move[1]] = None
        return value - depth
    else:
        value = math.inf
        moves = board.get_available_moves()
        for move in moves:
            board.board[move[0]][move[1]] = game.Node(None, 1)
            value = min(value, minimax(board, depth + 1, True))
            board.board[move[0]][move[1]] = None
        return value + depth
