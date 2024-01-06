import sys
input = sys.stdin.readline

n = int(input().rstrip())
data = [list(map(int, input().rstrip().split())) for _ in range(n)]

data.sort(key=lambda x: (x[1], x[0]))

for i in data:
    for j in i:
        print(j, end=' ')
    print()