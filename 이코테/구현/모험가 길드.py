# [모험가 길드] 난이도 1/3, 풀이시간 30분, 시간 제한 1초, 메모리 제한 128MB
# 공포도가 X인 모험가는 반드시 X명 이상으로 그룹화 해야한다.
# 모든 모험가가 그룹에 소속될 필요는 없다.
# 그룹의 수의 최댓값은?

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
array.sort()

group_cnt = 0
people_in_group = 0

for scarry in array:
    people_in_group += 1  # 그룹에 현재 모험가 넣기
    if people_in_group >= scarry:
        group_cnt += 1  # 그룹 카운트 1증가
        people_in_group = 0  # 0으로 초기화

print(group_cnt)
