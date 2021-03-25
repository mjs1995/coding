n = int(input())
res = []
res = list(map(int,str(n)))
res.sort(reverse=True)
for i in res:
    print(i, end="")
