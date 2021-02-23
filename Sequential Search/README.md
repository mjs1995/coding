# 순차 탐색 
-bisect_right()는 x와 동일한 값이 시퀀스 a에 존재할 때 x와 동일한 값 바로 뒤 위치를 리턴한다.
- 반면에 bisect_left()는 x와 동일한 값 위치를 리턴한다.

```python
sequence = [1, 3, 4, 5]
print(bisect.bisect_right(sequence, 3))
print(bisect.bisect_left(sequence, 3))
----------------------------------------
2
1
```
- 이진 탐색
```python
def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid - 1)
    else:
        return binary_search(array, mid + 1, end)
```

