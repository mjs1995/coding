a = list(map(int, input().split()))
b = list(map(int, input().split()))
pr = list(product(a,b))
li = []
for i in pr:
    li.append(str(i))
print(' '.join(li))

a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*product(a,b))
