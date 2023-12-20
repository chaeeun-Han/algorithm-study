def solution(n, lost, reserve):
    answer = n - len(lost)
    lost.sort()
    reserve.sort()
    lost_copy = lost.copy()

    # 여벌을 가져왔는데 잃어버린 경우
    for i in lost_copy:
        if i in reserve:
            answer += 1
            reserve.remove(i)
            lost.remove(i)

    # 본인의 여벌x 도난당했을 경우
    for i in lost:
        # 본인보다 작은 것을 빌릴 경우
        if (i - 1) in reserve:
            answer += 1
            reserve.remove(i - 1)
        # 작은게 없어서 큰 걸 빌릴 경우
        elif (i + 1) in reserve:
            answer += 1
            reserve.remove(i + 1)

    return answer