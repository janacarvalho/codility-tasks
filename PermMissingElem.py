def solution(A):
    """
    Return the value of the missing element in an array A.
    :param A: an array of N different integers missing one element
    :return: the missing element in the array A of different elements
    """
    # empty or one-element string
    if not A or len(A) == 1:
        return 1
    A.sort()
    if len(A) == 2:
        return A[0] + 1
    half = int(len(A)/2)
    first_half = A[:half]
    last_half = A[half:]
    if len(first_half) < first_half[-1] - first_half[0] + 1:
        return solution(first_half)
    if len(last_half) < last_half[-1] - last_half[0] + 1:
        return solution(last_half)
    return first_half[-1] + 1
