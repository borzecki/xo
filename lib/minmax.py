import operator
from helpers import OPONENT_A, OPONENT_B
from copy import copy

def __min_max_rec(board, player, depth):
	oponent = OPONENT_A if player == OPONENT_B else OPONENT_B
	score = 0
	for next in board.available_placements:
		board[next] = player
		over, winner = board.game_over
		if over and winner == player:
			score += 1
		elif depth > 0:
			score -= __min_max_rec(board, oponent, depth-1)
		board[next] = None
	return score

def min_max(board, player, depth):
	oponent = OPONENT_A if player == OPONENT_B else OPONENT_B
	best = {}
	for next in board.available_placements:
		board[next] = player
		over, winner = board.game_over
		if over and winner == player:
			return next
		else:
			best[next] = -__min_max_rec(board, oponent, depth-1)
		board[next] = None
	return max(best.iteritems(), key=operator.itemgetter(1))[0]

