# [미로 탈출] 난이도 1.5/3, 풀이시간 30분, 시간 제한 1초, 메모리 제한 128MB

from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):
    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            # 상하좌우 이동 위치
            nx = x + dx[i]
            ny = y + dy[i]

            # 이탈하지 않고 괴물이 존재하지 않는 칸
            if (nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] != 0):
                # 처음 방문한다면 이전 노드 + 1로 현재 노드 값 초기화
                if (graph[nx][ny] == 1):
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

    return graph[n-1][m-1]


if __name__ == '__main__':
    global n, m
    n, m = map(int, input().split())

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().strip())))

    print(bfs(0, 0))
