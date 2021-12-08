n, m = map(int, input().split())
s = []
queue = []
dx = [1, -1, 0, 0] #상하
dy = [0, 0, -1, 1] #좌우 
for i in range(n):
    s.append(list(input()))
queue = [[0, 0]]
s[0][0] = 1
while queue:
    a, b = queue[0][0], queue[0][1]
    del queue[0] 
    for i in range(4): #상화좌우 4
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and s[x][y] == "1": # 해당되는 조건이면 모두 조사 
            queue.append([x, y])
            s[x][y] = s[a][b] + 1
print(s[n - 1][m - 1])

""" s 
[1, '0', 9, 10, 11, 12]
[2, '0', 8, '0', 12, '0']
[3, '0', 7, '0', 13, 14]
[4,  5,  6, '0', 14, 15]
"""
