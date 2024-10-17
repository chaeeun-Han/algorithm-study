def solution(s):
    stack = []
    
    try:
        for value in s:
            if value == '(':
                stack.append(1)
            else:
                stack.pop()
    # pop을 더이상 할 수 없는 경우 False
    except IndexError:
        return False

    # stack에 값이 존재하는 경우 False
    if (stack):
        return False

    return True