import sys

OPPONENT_A = 'o'
OPPONENT_B = 'x'
DRAW = 'draw'


def take_coordinates(player):
    print "Players '%s' turn. Give coordinates (COL ROW):" % player
    return tuple(map(int, sys.stdin.readline().strip().split()))


def parse_options():
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option("-s", "--size", type="int", dest="size", default=3,
                      help="board size (default is 3)")
    parser.add_option("-l", "--length", type="int", dest="length", default=3,
                      help="winning length (default is 3)")
    return parser.parse_args()