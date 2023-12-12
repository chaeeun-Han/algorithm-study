def solution(n):
    p = 1
    while (6 * p % n != 0):
        p += 1
    
    return p