import operator
from helpers import OPPONENT_A, OPPONENT_B


def __min_max_rec(board, player, depth):
    opponent = OPPONENT_A if player == OPPONENT_B else OPPONENT_B
    score = 0
    for placement in board.available_placements:
        board[placement] = player
        over, winner = board.game_over
        if over and winner == player:
            score += 1
        elif depth > 0:
            score -= __min_max_rec(board, opponent, depth-1)
        board[placement] = None
    return score


def min_max(board, player, depth):
    opponent = OPPONENT_A if player == OPPONENT_B else OPPONENT_B
    best = {}
    for placement in board.available_placements:
        board[placement] = player
        over, winner = board.game_over
        if over and winner == player:
            return placement
        else:
            best[placement] = -__min_max_rec(board, opponent, depth-1)
        board[placement] = None
    return max(best.iteritems(), key=operator.itemgetter(1))[0]

