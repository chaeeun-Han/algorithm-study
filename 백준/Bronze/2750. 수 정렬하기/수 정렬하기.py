import sys
sys.setrecursionlimit(10**6)
n = int(input())
data = [int(input()) for _ in range(n)]

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [i for i in tail if i <= pivot]
    right_side = [i for i in tail if i > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

answer = quick_sort(data)
for i in answer:
    print(i)