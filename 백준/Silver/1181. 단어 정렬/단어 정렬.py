import sys
input = sys.stdin.readline

n = int(input().rstrip())
data = set([input().rstrip() for _ in range(n)])
data = list(data)
data.sort(key=lambda x: (len(x), x))

for i in data:
    print(str(i))