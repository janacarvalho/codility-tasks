def solution(A, K):
    """
    Rotate an array A K times to the right
    :param A: array to be rotate
    :param K: the number to times
    :return: array rotate K times to the right
    """
    size = len(A)
    if K == size or size <= 1 or K % size == 0:
        return A
    index = size - K if K < size else size - K%size
    return (A[index:] + A[:index])
