import heapq

def solution(scoville, K):
    answer = 0
    h = []
    
    for i in scoville:
        heapq.heappush(h,i)
    
    while h[0] < K:
        try:
            heapq.heappush(h, heapq.heappop(h) + (heapq.heappop(h)*2))
        except indexError:
            return -1
        answer += 1
    return answer
