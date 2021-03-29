n,m = map(int,input().split())
v = [0 for _ in range(n)]
arr = []

def back(c):
    if c == m:
        print(*arr)
        return
    for i in range(n):
        if v[i] == 0:
            arr.append(i+1)
            
            back(c+1)
            v[i] = 1
            arr.pop
            
            for j in range(i+1,n):
                v[j] = 0
back(0)
