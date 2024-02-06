# heapq.nlargest(n, iterable, key=None)
# heapq.nsmallest(n, iterable, key=None)
import heapq
def solution(operations):
    heap = []
    
    for command in operations:
        if "I" in command:
            heapq.heappush(heap, int(command[2:]))
        elif heap:
            if command == "D 1":
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)
            elif command == "D -1":
                heapq.heappop(heap)
            
    if heap:
        return [max(heap), min(heap)]
    else:
        return [0,0]
