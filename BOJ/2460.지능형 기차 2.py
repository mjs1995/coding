temp = 0
re = []
for i in range(10):
    a,b = map(int,input().split())
    temp += (b-a)
    re.append(temp)
print(max(re))
