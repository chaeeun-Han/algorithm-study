from itertools import permutations

N = int(input())

numbers = list(permutations(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 3))

for _ in range(N):
    question_number, strike, ball = map(int, input().split())
    question_number = list(str(question_number))
    removed = 0

    for i in range(len(numbers)):
        strike_cnt = 0
        ball_cnt = 0
        i -= removed
        for j in range(3):
            if question_number[j] == numbers[i][j]:
                strike_cnt += 1
            elif question_number[j] in numbers[i]:
                ball_cnt += 1

        if strike_cnt != strike or ball_cnt != ball:
            numbers.remove(numbers[i])
            removed += 1

print(len(numbers))