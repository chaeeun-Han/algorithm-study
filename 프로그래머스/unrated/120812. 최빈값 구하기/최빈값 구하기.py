def solution(array):
    data = dict()
    
    for i in array:
        if i in data:
            continue
        else:
            data[i] = array.count(i)
            
    tmp = [k for k,v in data.items() if max(data.values()) == v]    
    return -1 if len(tmp) > 1 else tmp[0]
