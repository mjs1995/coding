# Counter
```python
from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
find = list(map(int,input().split()))
count = Counter(arr)
print(' '.join(str(count[x]) if x in count else '0' for x in find))
_________________________________
count 
#Counter({6: 1, 3: 2, 2: 1, 10: 3, -10: 2, 7: 1})
_________________________________
for x in find:
    if x in count:
        print(x)
# 10
# 2
# 3
# -10
_________________________________
for x in find:
    if x in count:
        print(count[x])
# 3
# 1
# 2
# 2      
```

# Heap
```python
import heapq

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
  heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
  print(heapq.heappop(heap)[1])  # index 1
```
8
7
5
4
3
1

```python
import heapq

def kth_smallest(nums, k):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)

  kth_min = None
  for _ in range(k):
    kth_min = heapq.heappop(heap)
  return kth_min

print(kth_smallest([4, 1, 7, 3, 8, 5], 3))
```
4
