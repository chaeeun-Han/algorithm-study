# [부품 찾기] 난이도 1.5/3, 풀이 시간 30분, 시간 제한 1초, 메모리 제한 128MB

import sys
input = sys.stdin.readline


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if (array[mid] == target):
            return "yes"
        elif (array[mid] > target):
            end = mid - 1
        else:
            start = mid + 1
    return "no"


n = int(input())
array = list(map(int, input().split()))
m = int(input())
targetList = list(map(int, input().split()))

array.sort()

for target in targetList:
    result = binary_search(array, target, 0, len(array)-1)
    print(result, end=" ")
