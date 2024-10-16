def solution(s):
    int_list = [int(str) for str in s.split(" ")]

    answer = str(min(int_list)) + " " + str(max(int_list))
    return answer
