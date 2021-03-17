N = int(input())
fans = []
for i in range(N):
    fans.append(list(map(int, input().split())))
print(fans)
go = sorted(fans, key = lambda x: x[0])    
back = sorted(fans, key = lambda x : x[1])

result = go[-1][0] - back[0][1]

if result <= 0:
    print(0)
else:
    print(result)
