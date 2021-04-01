from collections import Counter
t = int(input())
for i in range(t):
    n = int(input())
    s = []
    for j in range(n):
        a,b = input().split()
        s.append(b)
    num = 1
    res = Counter(s)
    
    for k in res:
        num *= res[k] +1
    print(num-1)
