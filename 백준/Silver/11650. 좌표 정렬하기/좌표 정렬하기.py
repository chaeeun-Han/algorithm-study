import sys
input = sys.stdin.readline

n = int(input().rstrip())
data = [list(map(int, input().rstrip().split())) for _ in range(n)]
data.sort()

for i in data:
    for j in i:
        print(j, end=' ')
    print()