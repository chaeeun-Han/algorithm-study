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

# 조금 더 나은 풀이
# 내림차순으로 정렬 후, total에서 3의 배수에 속하는 것들을 빼주면 된다.
import sys
input = sys.stdin.readline

n = int(input())
price = [int(input().rstrip()) for _ in range(n)]
price.sort(reverse=True)

total = 0
for i in range(2,len(price),3):
  total += price[i]

print(sum(price) - total)
