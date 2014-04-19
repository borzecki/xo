from lib.board import Board
from lib.helpers import *
from lib.minmax import min_max
from random import choice

if __name__ == "__main__":
    (options, args) = parse_options()

    board = Board(options.size, options.length)
    turn = OPPONENT_A
    you = choice([OPPONENT_A, OPPONENT_B])
    pc = OPPONENT_B if you == OPPONENT_A else OPPONENT_A
    messages = {you: "You've won!", pc: "You've lost!", DRAW: "It's a draw."}

    while not board.game_over[0]:
        if turn == pc:
            next_move = min_max(board, pc, 3)
        else:
            next_move = take_coordinates(turn)
        board[next_move] = turn
        turn = OPPONENT_B if turn == OPPONENT_A else OPPONENT_A
        print board
    print messages[board.game_over[1]]


