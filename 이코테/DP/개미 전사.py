# [개미 전사] 난이도 2/3, 풀이 시간 30분, 시간 제한 1초, 메모리 제한 128MB

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
dp = [0] * 101  # 식량 창고의 갯수만큼 초기화

dp[0] = array[0]
dp[1] = max(dp[0], array[1])

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2]+array[i])

print(dp[n-1])
