def solution(s):
    answer = []
    n = len(s.replace('0', ''))
    zero_cnt, cnt = len(s) - n, 1
    
    while (n != 1):
        s = binary(n, [])
        n = len(s.replace('0', ''))
        zero_cnt += len(s) - n
        cnt += 1
    
    return [cnt, zero_cnt]

def binary(n, result):
    if (n != 0):
        result.insert(0, str(n%2))
        return binary(n//2, result) 
    else:
        return ''.join(result)    
    