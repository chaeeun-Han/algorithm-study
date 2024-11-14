# 시각: 00:00:00 ~ n:59:59, 3이 포함되어있는 시각의 갯수 세기
# 완전탐색: 데이터의 개수가 100만개 이하일 때 적절

import sys
input = sys.stdin.readline


def solution(hour):
    cnt = 0

    for h in range(hour+1):
        for m in range(60):
            for s in range(60):
                result = str(h) + str(m) + str(s)
                if "3" in result:
                    cnt += 1

    return cnt


if __name__ == '__main__':
    hour = int(input())

    print(solution(hour))
