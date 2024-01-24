import math

def solution(progresses, speeds):
    answer = []
    day = []
    
    for i in range(len(progresses)):
        till = math.ceil((100 - progresses[i])/speeds[i])
        day.append(till)
    
    maxidx = 0
    for i in range(len(day)):
        if day[i] > day[maxidx]:
            answer.append(i - maxidx)
            maxidx = i
    answer.append(len(day)-maxidx)
    return answer