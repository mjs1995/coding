from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
find = list(map(int,input().split()))
count = Counter(arr)
print(' '.join(str(count[x]) if x in count else '0' for x in find))
