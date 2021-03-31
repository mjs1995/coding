n = int(input())
roads = list(map(int,input().split()))
costs = list(map(int,input().split()))

res = roads[0] * costs[0]
m = costs[0]
dist = 0
for i in range(1,n-1):
    if costs[i] < m:
        res += m*dist
        dist = roads[i]
        m = costs[i]
    else:
        dist += roads[i]
    if i == n-2:
        res += m* dist
print(res)
