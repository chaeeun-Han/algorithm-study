def solution(brown, yellow):
    answer = []
    for i in range(yellow, 0, -1):
        width = i + 2
        length = (brown+yellow)/width 
        expectBr = width * 2 + (length - 2) * 2
        if expectBr == brown and width >= length:
            answer.append(width)
            answer.append(length)
            break
    return answer