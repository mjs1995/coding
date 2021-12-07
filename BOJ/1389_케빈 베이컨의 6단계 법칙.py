import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
graph = defaultdict(list)  # defaultdict(list, {})
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append((v, 1))
    graph[v].append((u, 1))
# 다익스트라 알고리즘 구현
answer = []
for k in range(1, n+1):
    queue = [(0, k)]
    dist = defaultdict(int)
    while queue:
        time, node = heapq.heappop(queue)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                heapq.heappush(queue, (time+w, v))
    answer.append((sum(dist.values()), k))
answer.sort()
print(answer[0][1])

"""
1 3
defaultdict(<class 'list'>, {1: [(3, 1)], 3: [(1, 1)]})
1 4
defaultdict(<class 'list'>, {1: [(3, 1), (4, 1)], 3: [(1, 1)], 4: [(1, 1)]})
4 5
defaultdict(<class 'list'>, {1: [(3, 1), (4, 1)], 3: [(1, 1)], 4: [(1, 1), (5, 1)], 5: [(4, 1)]})
4 3
defaultdict(<class 'list'>, {1: [(3, 1), (4, 1)], 3: [(1, 1), (4, 1)], 4: [(1, 1), (5, 1), (3, 1)], 5: [(4, 1)]})
3 2
defaultdict(<class 'list'>, {1: [(3, 1), (4, 1)], 3: [(1, 1), (4, 1), (2, 1)], 4: [(1, 1), (5, 1), (3, 1)], 5: [(4, 1)], 2: [(3, 1)]})
"""

"""answer
[(6, 1)]
[(6, 1), (8, 2)]
[(6, 1), (8, 2), (5, 3)]
[(6, 1), (8, 2), (5, 3), (5, 4)]
[(6, 1), (8, 2), (5, 3), (5, 4), (8, 5)]
"""
