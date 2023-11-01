n = int(input())
tmp = n
cnt = 0

five = n // 5

for i in range(five, -1, -1):
    n = tmp
    n -= i * 5
    if (n % 3 == 0):
        cnt += n // 3 + i
        break

if (cnt != 0):
    print(cnt)
else:
    print(-1)