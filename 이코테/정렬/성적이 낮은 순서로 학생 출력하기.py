# [성적이 낮은 순서로 학생 출력하기] 난이도 1/3, 풀이 시간 20분, 시간 제한 1초, 메모리 제한 128MB

import sys
input = sys.stdin.readline

n = int(input())
students = []

for _ in range(n):
    key, value = input().split()
    students.append((key, value))


# def setting(data):
#     return data[1]

# students.sort(key=setting)

# lambda를 사용하면
students.sort(key=lambda student: student[1])

for student in students:
    print(student[0], end=" ")
