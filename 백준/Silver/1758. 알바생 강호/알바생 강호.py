n = int(input())
tip = list()
total = 0

for i in range(n):
    tip.append(int(input()))

tip.sort(reverse=True)

for i in range(1, len(tip) + 1):
    tmp = tip[i-1] - (i - 1)
    if tmp > 0:
        total += tmp

print(total)