

def solution(A):
    a_size = len(A)
    all_sums = []
    for P in range(1, a_size):
        part1 = A[0:P]
        part2 = A[P:]
        res = abs(sum(part1) - sum(part2))
        all_sums.append(res)
    return min(all_sums)


A = [3, 1, 2, 4, 3]
solution(A)
