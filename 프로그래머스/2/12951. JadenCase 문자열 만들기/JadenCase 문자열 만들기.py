def solution(s):
#     answer = ''
#     buf = [word.lower() for word in s.split()]
    
#     for word in buf:
#         answer += ' ' + word.capitalize()
        
#     return answer[1:]
    isFirst = True
    answer = ''
    s = s.lower()
    
    for word in s:
        if (isFirst and word != ' '):
            answer += word.upper()
            isFirst = False
        elif (word == ' '):
            answer += word
            isFirst = True
        else:
            answer += word
            
    return answer
            
