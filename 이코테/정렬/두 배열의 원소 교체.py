# [두 배열의 원소 교체] 난이도 1/3, 풀이 시간 20분, 시간 제한 2초, 메모리 제한 128MB
# n: 배열의 원소 갯수, k: 최대 바꿔치기 횟수
# 바꿔치기: A에 있는 원소를 B에 있는 원소와 바꾸는 것
# 배열 A의 모든 원소의 합이 최대가 되도록하라.


import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()  # 오름차순 정렬
b.sort(reverse=True)  # 내림차순 정렬

for idx in range(k):
    # a의 값이 b보다 작으면 교체
    if a[idx] < b[idx]:
        a[idx], b[idx] = b[idx], a[idx]
    else:
        break

print(sum(a))
