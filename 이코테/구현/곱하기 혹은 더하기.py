# [곱하기 혹은 더하기] 난이도 1/3, 풀이시간 30분, 시간 제한 1초, 메모리 제한 128MB
# 0~9로 이루어진 문자열 s
# 문자열 사이에 x 또는 + 연산자를 넣어 최댓값 만들기
# 단, 연산은 무조건 왼쪽부터 오른쪽으로 연산한다.

import sys
input = sys.stdin.readline

s = list(map(int, input().rstrip()))
total = s[0]

for num in s[1:]:
    # 숫자가 1보다 크면 곱하기
    if (total > 1 and num > 1):
        total *= num
    # 1이하이면 더하기
    else:
        total += num

print(total)
