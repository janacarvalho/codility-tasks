

def solution(A):
    for elem in A:
        if A.count(elem) % 2 != 0:
            return elem
    return -1


if __name__ == '__main__':
    A = [9, 3, 9, 3, 9, 7, 9]
    print solution(A)
