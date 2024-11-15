def solution(numbers, target):
    cnt = 0
    
    def dfs(idx, nsum):
        nonlocal cnt
        
        # numbers idx 끝까지 갔고, nsum이 target과 같으면 True
        if (idx == len(numbers)):
            if (nsum == target):
                cnt += 1
            return

        dfs(idx+1, nsum + numbers[idx])
        dfs(idx+1, nsum - numbers[idx])
    
    dfs(0, 0)
        
    return cnt