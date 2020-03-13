def solution(A):
    """
    Calculate the difference between the two parts and return the minimal difference.
    :param A: array of N integers
    :return: the absolute difference between the sum of the first and last part.
    """
    s = sum(A)
    m = float('inf')
    left_sum = 0
    for n in A[:-1]:
        left_sum += n
        m = min(abs(2*left_sum - s), m)
    return m
