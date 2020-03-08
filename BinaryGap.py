def solution(N):
    """
    Calculate the max gap length within a binary number
    :param N: decimal number to get the corresponding gap
    :return: max gap length within the binary number
    """    
    if N < 5: return 0
    
    # transform decimal number into a string with the 
    # binary value corresponding without '0b'
    binary = bin(N)[2:]
    
    max_gap = 0
    gap_len = 0
    
    for i in range(len(binary)):
        n0 = binary[i]
        try:
            n1 = binary[i+1]
        except:
            n1 = '0'
        if n0 == '0' and n1 == '0':
            gap_len +=1
        elif n0 == '0' and n1 == '1':
            gap_len += 1
            max_gap = gap_len if gap_len > max_gap else max_gap
            gap_len = 0
    return max_gap
