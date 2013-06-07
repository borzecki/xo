from lib.board import Board
from lib.helpers import *
from lib.minmax import min_max
from random import choice

if __name__ == "__main__":
    (options, args) = parse_options()

    board = Board(options.size, options.length)
    turn = OPONENT_A
    player_a = choice([OPONENT_A, OPONENT_B])
    player_b = OPONENT_B if player_a == OPONENT_A else OPONENT_A
    messages = {player_a: "%s won!"%player_a, player_b: "%s won!"%player_b, DRAW: "It's a draw."}

    while not board.game_over[0]:
        if turn == player_a:
            next_move = take_coords(turn)
        else:
            next_move = take_coords(turn)
        board[next_move] = turn
        turn = OPONENT_B if turn == OPONENT_A else OPONENT_A
        print board
    print messages[board.game_over[1]]


