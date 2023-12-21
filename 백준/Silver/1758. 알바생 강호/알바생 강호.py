import sys
input = sys.stdin.readline

n = int(input().rstrip())
tip = [int(input().rstrip()) for _ in range(n)]
total = 0

tip.sort(reverse=True)

for i in range(1, len(tip) + 1):
    tmp = tip[i-1] - (i - 1)
    if tmp < 0:
        continue
    total += tmp

print(total)