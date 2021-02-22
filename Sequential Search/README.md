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

