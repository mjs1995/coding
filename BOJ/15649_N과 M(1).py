n,m = map(int,input().split())

s = []
def sol():
    if len(s) == m:
        print(' '.join(map(str,s)))
        return
    for i in range(1,n+1):
        if i in s:
            continue
        s.append(i)
        sol()
        s.pop()
sol()
