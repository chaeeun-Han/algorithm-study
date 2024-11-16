def solution(n):
    answer = 0
    
    def hap(start, total):
        if total > n:
            return False
        elif total == n:
            return True
        else:
            return hap(start+1, total+start)
    
    for i in range(1, n+1):
        if hap(i, 0):
            answer += 1
            
    return answer