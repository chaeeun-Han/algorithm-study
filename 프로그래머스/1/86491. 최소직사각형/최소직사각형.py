def solution(sizes):
    big = []
    small = []
    
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            big.append(sizes[i][0])
            small.append(sizes[i][1])
        else:
            big.append(sizes[i][1])
            small.append(sizes[i][0])
            
    return max(big) * max(small)