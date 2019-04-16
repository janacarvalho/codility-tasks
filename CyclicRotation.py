def solution(A, K):
    list_size = len(A)

    if list_size < 2 or K == list_size:
        return A

    B = [0] * list_size
    for i in range(list_size):
        B[(i+K)%list_size] = A[i]
    return B

