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

