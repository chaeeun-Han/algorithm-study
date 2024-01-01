n, k = map(int, input().split())
data = [int(input()) for _ in range(n)]
cnt = 0

data.sort(reverse=True)

for i in data:
    if i > k:
        continue
    else:
        cnt += k // i
        k %= i

print(cnt)