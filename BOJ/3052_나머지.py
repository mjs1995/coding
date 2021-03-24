arr = []
for i in range(10):
    number = int(input())
    arr.append(number % 42)
res = set(arr)
print(len(res))
