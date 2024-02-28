import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [1] * n  # 각 원소 자체로 길이 1의 감소하는 부분 수열을 형성하므로 초기값을 1로 설정

for i in range(n):
    for j in range(i):
        if data[i] < data[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))