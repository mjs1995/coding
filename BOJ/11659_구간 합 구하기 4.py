import sys
input = sys.stdin.readline

n, m = map(int,input().rsplit())
nums = list(map(int,input().rsplit()))
prefix = [0]
curr = 0

for n in nums:
    curr += n
    prefix.append(curr)

for _ in range(m):
    i, j = map(int,input().rsplit())
    print(prefix[j]-prefix[i-1])
