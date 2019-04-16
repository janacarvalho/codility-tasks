def solution(n):
    if n < 5:  # the smallest positive number with binary gap
        return 0

    nbr_list = list(bin(n))
    nbr_list.reverse()
    nbr_trim = str(int(''.join(nbr_list[:-2])))
    nbr_size = len(nbr_trim)

    if nbr_size < 3:
        return 0

    count_gaps = 0
    biggest_gap = 0
    gap_size = 0

    j = 0
    while j < nbr_size-1:
        if nbr_trim[j] == '0' and nbr_trim[j + 1] == '0':
            gap_size += 1
        if nbr_trim[j] == '0' and nbr_trim[j + 1] == '1':
            gap_size += 1
            count_gaps += 1
            biggest_gap = gap_size if gap_size > biggest_gap else biggest_gap
            gap_size = 0
        j += 1
    return biggest_gap


if __name__ == '__main__':
    print solution(-4)
    print solution(0)
    print solution(1)
    print solution(2)
    print solution(3)
    print solution(20)
    print solution(55)
    print solution(1041)
    print solution(32)
