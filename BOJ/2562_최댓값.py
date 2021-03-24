res = []
for _ in range(9):
    res.append(int(input()))
print(max(res))
print(res.index(max(res))+1)
