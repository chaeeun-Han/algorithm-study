from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []
    
    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue: # 슬라이스
            sec += 1
            if price > q:
                break 
        answer.append(sec)        
    return answer