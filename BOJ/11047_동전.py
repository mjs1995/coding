n,k = map(int,input().split())
coin = []

for i in range(n):
    coin.append(int(input()))
res = 0
coin.sort(reverse=True)

for i in coin:
    if k == 0: 
        break
    res += (k // i)
    k %= i
print(res)
