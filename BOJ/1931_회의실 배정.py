n = int(input())
r = []
for i in range(n):
    f,s = map(int,input().split())
    r.append([f,s])
r = sorted(r,key=lambda x:x[0])
r = sorted(r,key=lambda x:x[1])
last = 0
cnt = 0
for i,j in r:
    if i >= last:
        cnt+= 1
        last = j
print(cnt)
