a,b = map(int, input().split())
tmp = []
for _ in range(a):
    tmp.append(input())
print((sorted(tmp))[b-1])    
