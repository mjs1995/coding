# 큐
from collections import deque
N = int(input())

tree= [[] for _ in range(N+1)] # [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parent = [0 for _ in range(N+1)]#visited [0, 6, 4, 6, 1, 3, 1, 4]
queue=[1]#start from root

while queue: # queue = []
    child = queue.pop(0) # 1,6,4,1,3,2,7,5,4,6,1,3,1,4
    for i in tree[child]:
        if parent[i]==0:
            parent[i]=child #update parent
            queue.append(i) # [6] [6,4] [4,1] [4,1,3] [1,3,2] [1,3,2,7] [2,7,5]
            print(parent) 

for i in range(2, N+1):
    print(parent[i])

"""
[0, 0, 0, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 1, 0, 1, 0]
[0, 6, 0, 0, 1, 0, 1, 0]
[0, 6, 0, 6, 1, 0, 1, 0]
[0, 6, 4, 6, 1, 0, 1, 0]
[0, 6, 4, 6, 1, 0, 1, 4]
[0, 6, 4, 6, 1, 3, 1, 4]
"""

# BFS
from collections import deque
import sys

input = sys.stdin.readline


def BFS(start, graph, visited, parent):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                parent[i] = now
                visited[i] = True
                queue.append(i)


N = int(input())
graph = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)
visited = [False] * (N + 1)

for i in range(N - 1):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

start = 1
BFS(start, graph, visited, parent)

[print(parent[x]) for x in range(2, N + 1)]
