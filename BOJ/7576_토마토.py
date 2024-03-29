from collections import deque
 
m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
 
# 익은 토마토를 큐에 넣음
queue = deque() # deque([(3, 5, 0)])
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j, 0))
 
# 방향 지시자
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
 
while queue:
    x, y, days = queue.popleft()
    
    # 인접위치 토마토 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        ndays = days + 1
 
        # 박스 영역 안인지 확인
        if 0 <= nx < n and 0 <= ny < m:
            # 안익은 토마토일 경우 익힘 처리 후 큐에 삽입
            if box[nx][ny] == 0:
                box[nx][ny] = 1
                queue.append((nx, ny, ndays)) # deque([(2, 5, 1)]) -> deque([(2, 5, 1), (3, 4, 1)])


"""
[[0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 1], 
 [0, 0, 0, 0, 0, 1]]
deque([(2, 5, 1)])

[[0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 1], 
 [0, 0, 0, 0, 1, 1]]
deque([(2, 5, 1), (3, 4, 1)])

[[0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 1], 
 [0, 0, 0, 0, 0, 1], 
 [0, 0, 0, 0, 1, 1]]
deque([(3, 4, 1), (1, 5, 2)])

[[0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 1], 
 [0, 0, 0, 0, 1, 1], 
 [0, 0, 0, 0, 1, 1]]
deque([(3, 4, 1), (1, 5, 2), (2, 4, 2)])

[[0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1], 
 [0, 0, 0, 0, 1, 1], 
 [0, 0, 0, 1, 1, 1]]
deque([(1, 5, 2), (2, 4, 2), (3, 3, 2)])

[[0, 0, 0, 0, 0, 1], 
 [0, 0, 0, 0, 0, 1], 
 [0, 0, 0, 0, 1, 1], 
 [0, 0, 0, 1, 1, 1]]
deque([(2, 4, 2), (3, 3, 2), (0, 5, 3)])


[[0, 0, 0, 0, 0, 1], 
 [0, 0, 0, 0, 1, 1], 
 [0, 0, 0, 0, 1, 1], 
 [0, 0, 0, 1, 1, 1]]
deque([(2, 4, 2), (3, 3, 2), (0, 5, 3), (1, 4, 3)])

[[0, 0, 0, 0, 0, 1], 
 [0, 0, 0, 0, 1, 1], 
 [0, 0, 0, 1, 1, 1], 
 [0, 0, 0, 1, 1, 1]]
deque([(3, 3, 2), (0, 5, 3), (1, 4, 3), (2, 3, 3)])

[[0, 0, 0, 0, 0, 1], 
[0, 0, 0, 0, 1, 1], 
[0, 0, 0, 1, 1, 1], 
[0, 0, 1, 1, 1, 1]]
deque([(0, 5, 3), (1, 4, 3), (2, 3, 3), (3, 2, 3)])

[[0, 0, 0, 0, 1, 1], 
[0, 0, 0, 0, 1, 1], 
[0, 0, 0, 1, 1, 1], 
[0, 0, 1, 1, 1, 1]]
deque([(1, 4, 3), (2, 3, 3), (3, 2, 3), (0, 4, 4)])

[[0, 0, 0, 0, 1, 1], 
[0, 0, 0, 1, 1, 1], 
[0, 0, 0, 1, 1, 1], 
[0, 0, 1, 1, 1, 1]]
deque([(2, 3, 3), (3, 2, 3), (0, 4, 4), (1, 3, 4)])

[[0, 0, 0, 0, 1, 1], 
[0, 0, 0, 1, 1, 1], 
[0, 0, 1, 1, 1, 1], 
[0, 0, 1, 1, 1, 1]]
deque([(3, 2, 3), (0, 4, 4), (1, 3, 4), (2, 2, 4)])

[[0, 0, 0, 0, 1, 1], 
[0, 0, 0, 1, 1, 1], 
[0, 0, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1]]
deque([(0, 4, 4), (1, 3, 4), (2, 2, 4), (3, 1, 4)])

[[0, 0, 0, 1, 1, 1], 
[0, 0, 0, 1, 1, 1], 
[0, 0, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1]]
deque([(1, 3, 4), (2, 2, 4), (3, 1, 4), (0, 3, 5)])

[[0, 0, 0, 1, 1, 1], 
[0, 0, 1, 1, 1, 1], 
[0, 0, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1]]
deque([(2, 2, 4), (3, 1, 4), (0, 3, 5), (1, 2, 5)])

[[0, 0, 0, 1, 1, 1], 
[0, 0, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1]]
deque([(3, 1, 4), (0, 3, 5), (1, 2, 5), (2, 1, 5)])

[[0, 0, 0, 1, 1, 1], 
[0, 0, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1]]
deque([(0, 3, 5), (1, 2, 5), (2, 1, 5), (3, 0, 5)])

[[0, 0, 1, 1, 1, 1], 
[0, 0, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1]]
deque([(1, 2, 5), (2, 1, 5), (3, 0, 5), (0, 2, 6)])

[[0, 0, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1]]
deque([(2, 1, 5), (3, 0, 5), (0, 2, 6), (1, 1, 6)])

[[0, 0, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1]]
deque([(3, 0, 5), (0, 2, 6), (1, 1, 6), (2, 0, 6)])

[[0, 1, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1]]
deque([(1, 1, 6), (2, 0, 6), (0, 1, 7)])

[[0, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1]]
deque([(2, 0, 6), (0, 1, 7), (1, 0, 7)])

[[1, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1]]
deque([(1, 0, 7), (0, 0, 8)])

"""
# 익지 않은 토마토가 있을 경우 결과값 -1로 변경
for i in range(n):
    if box[i].count(0):
        days = -1
        break
 
print(days)
