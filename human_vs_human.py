from lib.board import Board
from lib.helpers import *
from random import choice

if __name__ == "__main__":
    (options, args) = parse_options()

    board = Board(options.size, options.length)
    turn = OPPONENT_A
    player_a = choice([OPPONENT_A, OPPONENT_B])
    player_b = OPPONENT_B if player_a == OPPONENT_A else OPPONENT_A
    messages = {player_a: "%s won!" % player_a, player_b: "%s won!" % player_b, DRAW: "It's a draw."}

    while not board.game_over[0]:
        if turn == player_a:
            next_move = take_coordinates(turn)
        else:
            next_move = take_coordinates(turn)
        board[next_move] = turn
        turn = OPPONENT_B if turn == OPPONENT_A else OPPONENT_A
        print board
    print messages[board.game_over[1]]


