import heapq
heap = []
n = int(input())

for _ in range(n):
    for elem in list(map(int, input().split())):
        heapq.heappush(heap, elem)
        if len(heap) > n:
            heapq.heappop(heap)

print(heap[0])