# BFS
def solution(numbers, target):
    leaves = [0]            
    count = 0 

    for num in numbers : 
        temp = []
	
        # 자손 노드 생성 
        for leaf in leaves : 
            temp.append(leaf + num)    
            temp.append(leaf - num)    

        leaves = temp 

    # target과 같은지 확인 
    for leaf in leaves : 
        if leaf == target : 
            count += 1

    return count