n = int(input())
p = [n]
total_time = 0

p = list(map(int, input().split()))

p.sort()

for i in range(n):
    time = sum(p[:i+1])
    total_time += time

print(total_time)