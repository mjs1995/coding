n = int(input())
nums = []
for i in range(n):
    [x,y] = map(int,input().split())
    nums.append([x,y])
nums = sorted(nums)

for i in range(n):
    print(nums[i][0], nums[i][1])
