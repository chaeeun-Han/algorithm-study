import sys
input = sys.stdin.readline


def solution(n, plans):
    x, y = 1, 1

    # 이동 방향 설정
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    route = ['L', 'R', 'U', 'D']

    for r in plans:
        # 이동 좌표 구하기
        i = route.index(r)
        nx = x + dx[i]
        ny = y + dy[i]

        # 공간을 벗어나는 경우
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue

        # 이동 수행
        x, y = nx, ny

    return x, y


if __name__ == '__main__':
    n = int(input())
    plans = input().split()
    x, y = solution(n, plans)
    print(f"{x} {y}")
