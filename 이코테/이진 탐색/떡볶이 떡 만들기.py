# [떡볶이 떡 만들기] 난이도 2/3, 풀이 시간 40분, 시간 제한 2초, 메모리 제한 128MB
# 떡의 갯수 n, 요청한 떡의 길이 m
# h만큼 자르고 남은 떡 길이의 합이 m이상
# 최적의 h를 찾아라

# h가 0일 때 부터, h가 가장 긴 떡일 때까지.
# 리스트에 자른 떡 길이의 합을 넣는다. index가 height, value가 sum
# sum이 m인 걸 이진 탐색으로 찾는다. 있으면 height(mid+1)를 출력/없으면 mid+2를 출력


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()


def left_sum(hight):
    sum = 0
    for num in array:
        if (num-hight > 0):
            sum += num-hight
        else:
            continue
    return sum


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if (array[mid] == target):
            return mid + 1
        elif (array[mid] > target):
            end = mid - 1
        else:
            start = mid + 1
    return mid + 2


height_list = []

for height in range(array[-1]+1):
    height_list.append(left_sum(height))

height_list.sort()

idx = binary_search(height_list, m, 0, len(height_list)+1)
print(array[-1]+1-idx)
