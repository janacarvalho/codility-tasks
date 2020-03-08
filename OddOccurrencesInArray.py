from collections import Counter


def solution(A):
    """
    Return the number of the unpaired element.
    :param A: array of integers containing an odd number
    :return: the value of the unpaired element
    """
    for item, times in Counter(A).items():
        if times%2:
            return item
    return
