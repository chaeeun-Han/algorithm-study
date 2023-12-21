import sys
input = sys.stdin.readline

n = int(input().rstrip())
price = [int(input().rstrip()) for _ in range(n)]
cnt = 1

price.sort(reverse=True)
left = price[-(len(price) % 3):] if (len(price) % 3) != 0 else [0]
total = sum(left)

for i in range(len(price) - (len(price) % 3)):
    if cnt == 3:
        cnt = 1
        continue
    total += price[i]
    cnt += 1

print(total)