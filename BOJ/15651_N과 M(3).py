n,m = map(int,input().split())
arr = []

def back(c):
    if c == m:
        print(*arr)
        return
    for i in range(n):
        arr.append(i+1)
        back(c+1)
        arr.pop()
back(0)
