# [위에서 아래로] 난이도 1/3, 풀이 시간 15분, 시간 제한 1초, 메모리 제한 128MB

import sys
input = sys.stdin.readline

n = int(input())
nums = []
nums = [int(input()) for _ in range(n)]

nums.sort(reverse=True)

for num in nums:
    print(num, end=" ")
