import sys
input = sys.stdin.readline
 
def dfs(graph, v, visited):
    global cnt # 전역변수 
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(graph, i, visited)
 
PC = int(input())
network = int(input())
 
graph = [[] for _ in range(PC + 1)] # [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
visited = [False] * (PC + 1) # [False, True, True, True, False, True, True, False]
cnt = 0    # global variable
 
for i in range(network):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
 
# 1번 컴퓨터가 바이러스 걸려서 v = 1 
dfs(graph, 1, visited)
print(cnt)
