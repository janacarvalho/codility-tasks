def solution(X,A):
    """
    A small frog wants to get to the other side of a river. The frog is initially
    located on one bank of the river (position 0) and wants to get to the opposite
    bank (position X+1). Leaves fall from a tree onto the surface of the river.
    
    :param X: Number of falling leaves used to cross the river.
    :param A: array consisting of N integers representing the falling leaves.
    :return: the earliest time when the frog can jump to the other side.
    """
    if len(A) < X: return -1
    result = [-1]*(X+1)
    for i in range(len(A)):
        result[A[i]] = i if result[A[i]] == -1 else min(i, result[A[i]])
        if -1 not in result[1:]:
            break
    return -1 if -1 in result[1:] else max(result[1:])
