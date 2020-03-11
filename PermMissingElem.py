def solution(A):
    """
    Return the value of the missing element in an array A.
    :param A: an array of N different integers missing one element
    :return: the missing element in the array A of different elements
    """
    if not A: return 1
    
    A.sort()
    if A[0] == 2: return 1
    if A[-1] - A[0] == len(A) - 1:
        return A[-1] + 1

    if len(A) == 2:
        return A[0] + 1
        
    half = int(len(A)/2)
    first_half = A[:half]
    last_half = A[half:]
    if len(first_half) < first_half[-1] - first_half[0] + 1:
        return solution(first_half)
    if len(last_half) < last_half[-1] - last_half[0] + 1:
        return solution(last_half)  
    if first_half[-1] + 1 == last_half[0]:
        return last_half[-1] + 1
    else:
        return first_half[-1] + 1
    