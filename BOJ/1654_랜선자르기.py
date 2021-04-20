k,n = map(int,input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))
l,u = 1, max(arr)
res = 0

while l <= u:
    mid = (l+u) // 2
    cut = sum([(i // mid) for i in arr])
    
    if cut >= n:
        res = mid
        l = mid + 1
    elif cut < n:
        u = mid - 1
print(res)
