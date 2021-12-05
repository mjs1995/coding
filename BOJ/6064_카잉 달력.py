import sys

input = sys.stdin.readline

Num = int(input())

for i in range(Num):
    M,N,x,y = map(int, input().split())
    if x == M:
        x = 0
    if y == N:
        y = 0
        
    result = -1
    
    for i in range(x, N*M+1, M):
        if i % N == y:
            result = i
            break
    print(result)
