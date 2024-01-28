from collections import deque
def solution(s):
    queue = deque()
    
    for i in s:
        if i == '(':
            queue.append(i)
        elif i == ")":
            if queue:
                queue.popleft()
            else:
                return False
    
    if queue:
        return False
    return True