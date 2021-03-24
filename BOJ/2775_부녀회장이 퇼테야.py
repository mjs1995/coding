t = int(input())

for _ in range(t):
    floor = int(input())
    n = int(input())
    f = [x for x in range(1, n+1)]
    for i in range(floor):
        for j in range(1,n):
            f[j] += f[j-1]
    print(f[-1])
