n,c = map(int,input().split())
house = [int(input()) for _ in range(n)]

house = sorted(house)
start,end = 1, house[-1] - house[0]
res = 0
while (start <= end):
    mid = (start + end) // 2
    wifi = 1
    before_install = house[0]
    for i in range(1,n):
        if house[i] >= before_install +mid:
            wifi += 1
            before_install = house[i]
    if wifi < c:
        end = mid - 1
    else:
        start = mid + 1
        res = mid
        
print(res)
