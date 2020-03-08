import math


def solution(X, Y, D):
    """
    Return the minimal number of jumps from position X 
    to a position egual or greater than Y.
    :param X: start position of the frog
    :param Y: minimal end position
    :param D: fixed distance of the jump
    :return: number of jumps to get to a position greater than or equal to Y.
    """
    return int(math.ceil((Y - X) / float(D)))
