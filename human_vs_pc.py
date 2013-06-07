from lib.board import Board
from lib.helpers import *
from lib.minmax import min_max
from random import choice

if __name__ == "__main__":
    (options, args) = parse_options()

    board = Board(options.size, options.length)
    turn = OPONENT_A
    you = choice([OPONENT_A, OPONENT_B])
    pc = OPONENT_B if you == OPONENT_A else OPONENT_A
    messages = {you: "You've won!", pc: "You've lost!", DRAW: "It's a draw."}

    while not board.game_over[0]:
        if turn == pc:
            next_move = min_max(board, pc, 3)
        else:
            next_move = take_coords(turn)
        board[next_move] = turn
        turn = OPONENT_B if turn == OPONENT_A else OPONENT_A
        print board
    print messages[board.game_over[1]]


