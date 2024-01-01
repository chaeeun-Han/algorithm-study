n = int(input())
cityLen = list(map(int, input().split()))
gasPrice = list(map(int, input().split()))
sum, less = 0, gasPrice[0]

for i in range(n-1):
    if gasPrice[i] < less:
        less = gasPrice[i]
    sum += cityLen[i] * less

print(sum)