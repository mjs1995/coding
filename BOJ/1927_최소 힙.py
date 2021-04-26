import heapq
from sys import stdin

n = int(stdin.readline())
heap = []
for _ in range(n):
    num = int(stdin.readline())
    
    if num != 0:
        heapq.heappush(heap,num)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
