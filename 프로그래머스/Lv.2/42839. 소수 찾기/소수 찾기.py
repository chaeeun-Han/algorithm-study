import itertools
def solution(numbers):
    number = [i for i in numbers]
    num = []

    # 숫자 조합
    for i in range(len(number)):
        for j in itertools.permutations(number, i+1):
            num.append(int(''.join(j)))
    num_list = list(set(num))
    
    if 1 in num_list:num_list.remove(1)
    if 0 in num_list:num_list.remove(0)
    
    answer = len(num_list)

    for i in num_list:
        for j in range(2, i):  # 2부터 i-1까지의 모든 숫자
            if i % j == 0:
                answer -= 1
                break

    return answer