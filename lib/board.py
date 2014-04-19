import itertools
from helpers import OPPONENT_A, OPPONENT_B, DRAW
from copy import copy


def board_coordinates(size):
    return itertools.product(range(size), range(size))


class Board(object):
    def __init__(self, size, length):
        assert size >= length, 'size greater than winning length'
        assert length > 1, 'winning length shorter than 2'
        self.size = size
        self.length = length
        self.placements = dict([(x, None) for x in board_coordinates(size)])

    @property
    def available_placements(self):
        return [p for p in board_coordinates(self.size) if not self.placements[p]]

    def __copy__(self):
        board_copy = Board(self.size, self.length)
        board_copy.placements = copy(self.placements)
        return board_copy

    def valid_win_placements(self):
        # Vertical and horizontal
        for i in xrange(self.size):
            for j in xrange(self.size - self.length + 1):
                yield [(i, x + j) for x in xrange(self.length)]
                yield [(x + j, i) for x in xrange(self.length)]
        # Diagonal
        for i in xrange(self.size - self.length + 1):
            for j in xrange(self.size - self.length + 1):
                yield [(x + i, x + j) for x in xrange(self.length)]
                yield [(self.size - 1 - (x + i), x + j) for x in xrange(self.length)]

    @property
    def game_over(self):
        for placement in self.valid_win_placements():
            pieces = map(lambda pos: self.placements[pos], placement)
            if None in pieces:
                continue
            elif ''.join(pieces) == OPPONENT_A * self.length:
                return True, OPPONENT_A
            elif ''.join(pieces) == OPPONENT_B * self.length:
                return True, OPPONENT_B
        if not None in self.placements.values():
            return True, DRAW
        return False, None

    def __getitem__(self, coordinates):
        return self.placements[coordinates]

    def __setitem__(self, coordinates, value):
        assert value in [OPPONENT_A, OPPONENT_B, None], 'wrong value'
        assert coordinates in self.placements, 'coordinate exceeding placements'
        self.placements[coordinates] = value

    def __repr__(self):
        frame_size = self.size + 2
        frame = [['#'] * frame_size for _ in xrange(frame_size)]
        for n in xrange(self.size):
            frame[0][n + 1] = frame[n + 1][0] = str(n)

        for i, j in board_coordinates(self.size):
            if self[(i, j)]:
                frame[i + 1][j + 1] = self[(i, j)]
            else:
                frame[i + 1][j + 1] = " "
        return "\n".join([''.join(x) for x in frame])

