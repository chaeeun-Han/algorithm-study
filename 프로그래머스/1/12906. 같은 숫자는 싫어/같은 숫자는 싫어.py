def solution(arr):
    answer = []
    idx = 0
    answer.append(arr[0])
    
    for i in range(len(arr)):
        if arr[idx] != arr[i]:
            answer.append(arr[i])
            idx = i
    return answer