n = int(input())
nums = []
for i in range(n):
    [x,y] = map(int,input().split())
    arr = [y,x]
    nums.append(arr)
nums = sorted(nums)
for i in range(n):
    print(nums[i][1],nums[i][0])
