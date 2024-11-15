# [음료수 얼려 먹기] 난이도 1.5/3, 풀이 시간 30분, 시간 제한 1초, 메모리 제한 128MB

import sys
input = sys.stdin.readline


def dfs(x, y):
    # 경로 이탈 시 반환
    if (x <= -1 or x >= n or y <= -1 or y >= m):
        return False

    # 방문하지 않은 노드일 때
    if graph[x][y] == 0:
        # 현재 노드 방문 처리
        graph[x][y] = 1

        # 상, 하, 좌, 우 연결된 노드 방문
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True

    return False


if __name__ == '__main__':
    global n, m
    n, m = map(int, input().split())
    cnt = 0

    # 2차원 배열로 그래프 입력 받기
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().strip())))

    # 현재 위치에서 노드 방문하기
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                cnt += 1

    print(cnt)
