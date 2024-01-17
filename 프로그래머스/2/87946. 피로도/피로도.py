from itertools import permutations

def solution(k, dungeons):
    answer = []
    power = k
    for per in permutations(dungeons, len(dungeons)):
        per = list(per)
        cnt, k = 0, power
        
        for i in range(len(per)):
            if per[i][0] <= k and (k - per[i][1]) >= 0:
                k -= per[i][1]
                cnt += 1    

        answer.append(cnt)
    return max(answer)