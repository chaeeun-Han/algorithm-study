def solution(nums):
    array = [str(i)*3 for i in nums]
    array.sort()
    answer = []
    cnt = 0

    for i in array:
        if i == '000':
            cnt += 1
        if cnt == len(array):
            return '0'

    for i in array:
        i = i[0:len(i)//3]
        answer.append(i)

    return "".join(answer[::-1])