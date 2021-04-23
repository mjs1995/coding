n,k = int(input()),int(input())
start, end = 1,k

while start <= end:
    mid = (start + end) // 2
    temp = 0
    for i in range(1, n+1):
        temp += min(mid//i, n)
        
    if temp < k:
        start = mid + 1
    else:
        end = mid -1
print(start)
