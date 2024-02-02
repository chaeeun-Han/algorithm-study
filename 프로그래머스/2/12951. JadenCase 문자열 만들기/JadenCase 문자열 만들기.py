def solution(s):
    answer = ''
    s = s.lower()
    flag = True

    for i in s:
        if i == ' ':
            flag = True
        elif flag:
            i = i.upper()
            flag = False

        answer += i

    return answer