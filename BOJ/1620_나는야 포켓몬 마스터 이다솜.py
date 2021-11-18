import sys
read = sys.stdin.readline
 
l = []
d = {}
N, M = map(int, read().split())
 
for i in range(N):
    temp = read().replace('\n', '')
    l.append(temp)
    d[temp] = i+1
 
for _ in range(M):
    temp = read().replace('\n', '')
    if temp.isdigit():
        temp = int(temp)
        print(l[temp-1])
    else:
        print(d[temp])
