# 왕실의 나이트
# 20min

import sys
input = sys.stdin.readline

# dx/dy를 사용한 방식
def solution(x, y):
    cnt = 0

    dx = [-1, 1, -1, 1, -2, -2, 2, 2]
    dy = [-2, -2, 2, 2, -1, 1, -1, 1]

    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]

        if (nx < 1 or nx > 8 or ny < 1 or ny > 8):
            continue
        cnt += 1

    return cnt

# 튜플 활용하기
def solution2(x, y):
    cnt = 0

    steps = [(-2, -1), (-1, -2), (1, -2), (2, -1),
             (2, 1), (1, 2), (-1, 2), (-2, 1)]

    for step in steps:
        nx = x + step[0]
        ny = y + step[1]

        # and 조건으로 제약 걸어보기
        if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
            cnt += 1

    return cnt

if __name__ == '__main__':
    start = input()
    row = int(start[1])
    column = int(ord(start[0])) - int(ord('a')) + 1
    print(solution(row, column))
