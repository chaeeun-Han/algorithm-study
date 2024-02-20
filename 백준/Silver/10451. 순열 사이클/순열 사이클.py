import sys
sys.setrecursionlimit(2000) #최대 재귀를 늘려줘야 런타임 에러를 피할 수 있다
t = int(input())
answer = []

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    global cycle

    visited = [False] * n
    idx = arr[0]

    def dfs(idx, cycle):
        visited[idx-1] = True
        target = arr[idx-1]
        if visited[target-1]:
            cycle += 1
            try:
                target = visited.index(False) + 1
            except:
                return answer.append(cycle)
            dfs(target, cycle)
        else:
            dfs(target, cycle)

    dfs(idx, 0)

for a in answer:
    print(a)