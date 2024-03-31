# 28min 23sec
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

current_sum = nums[0]
max_sum = nums[0]

for i in range(1, n):
    current_sum = max(nums[i], current_sum + nums[i])
    max_sum = max(max_sum, current_sum)

print(max_sum)