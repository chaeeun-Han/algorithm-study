def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)

    for index in range(0, len(A)):
        answer += (A[index]*B[index])
        
    return answer