def solution(people, limit):
    answer, start, end = 0, 0, len(people) -1
    people.sort()
    
    while(start<=end):   
        if(people[start]+people[end] <=limit):  
            start +=1
            end -=1
        else:           
            end-=1
        answer +=1
    return answer