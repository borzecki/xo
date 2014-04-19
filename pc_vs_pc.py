from lib.board import Board
from lib.helpers import *
from lib.minmax import min_max
from random import choice

if __name__ == "__main__":
    (options, args) = parse_options()

    pc_a = choice([OPPONENT_A, OPPONENT_B])
    pc_b = OPPONENT_B if pc_a == OPPONENT_A else OPPONENT_A
    score = {pc_a: 0, pc_b: 0, DRAW: 0}

    for _ in xrange(10):
        board = Board(options.size, options.length)
        turn = choice([OPPONENT_A, OPPONENT_B])
        while not board.game_over[0]:
            if turn == pc_a:
                next_move = min_max(board, pc_a, 2)
            else:
                next_move = min_max(board, pc_b, 4)
            board[next_move] = turn
            turn = OPPONENT_B if turn == OPPONENT_A else OPPONENT_A
        score[board.game_over[1]] += 1
    print pc_a, pc_b
    print score

