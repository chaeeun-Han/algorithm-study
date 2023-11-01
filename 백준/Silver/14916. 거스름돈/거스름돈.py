n = tmp = int(input())
cnt = 0
five = n // 5

for i in range(five, -1, -1):
    n = tmp
    n -= i * 5
    if (n % 2 == 0):
        cnt += n // 2 + i
        break

if (cnt != 0):
    print(cnt)
else:
    print(-1)