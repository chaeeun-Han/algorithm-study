from collections import deque # Queue를 사용하기 위한 collection library 사용

n, m = map(int,input().split()) # n 과 m에 대한 입력을 받음

graph = [] # 2차원 list 
for i in range(n): # n개의 rows에 대해서 map에 대한 정보를 얻음
    graph.append(list(map(int,input())))

dx = [-1,1,0,0] 
dy = [0,0,-1,1]

# 상하좌우 움직이도록 하는 lists

def bfs(x,y): # BFS 선언, 입력으로 x와 y의 정보를 받음
    queue = deque() # queue 초기화
    queue.append((x,y)) # 초기 위치 

    while queue:
        x, y = queue.popleft() # queue에서 꺼내기

        for i in range(4): # 4 방향에 대해서 이동 check

            nx = x+ dx[i] # 이동
            ny = y+ dy[i] # 이동

            if nx < 0 or ny < 0 or nx >=n or ny >= m: # 밖으로 넘어가는 경우,
                continue # continue
            if graph[nx][ny] == 0: # 이동 할 수 없는경우
                continue # continue

            if graph[nx][ny] == 1: # nx, ny에 처음으로 이동했을 때에,
                graph[nx][ny] = graph[x][y] + 1 # graph[x][y]는 최소의 거리를 저장, 1을 더한 값을 graph[nx][ny에 저장
                queue.append((nx,ny)) # 이동 된 nx, ny를 queue에 집어 넣기

    return graph[n-1][m-1] # 최종 n, m 위치에서의 graph 값 즉, 최소 거리를 반환함

print(bfs(0,0))