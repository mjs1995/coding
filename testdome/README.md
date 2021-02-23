# list 중복 제거 - set()
```python
def unique_names(names1, names2):
    a = list(set(names1 + names2))
    return a 

if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia
```
