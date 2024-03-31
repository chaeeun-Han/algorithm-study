import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

# dp[i]는 nums[i]를 포함한 최대 연속 부분합을 저장합니다.
dp = [0] * n
dp[0] = nums[0]

for i in range(1, n):
    dp[i] = max(nums[i], dp[i-1] + nums[i])

print(max(dp))