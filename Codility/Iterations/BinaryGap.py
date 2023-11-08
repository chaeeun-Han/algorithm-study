def solution(N):
    binary_list = list()
    result_list = list()
    num = N
    cnt = 0

    while (num != 1):
        binary = num % 2
        binary_list.append(binary)
        num //= 2

    binary_list.append(1)
    binary_list.reverse()

    for i in binary_list:
        if i == 0:
            cnt += 1
        elif i == 1:
            if cnt != 0:
                result_list.append(cnt)
                cnt = 0
            else:
                cnt = 0

    if result_list:
        result_list.sort(reverse=True)
        result = result_list[0]
    else:
        result = 0

    return result
