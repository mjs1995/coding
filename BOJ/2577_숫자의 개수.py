a = int(input())
b = int(input())
c = int(input())
num = a*b*c
li = list(str(num))
for i in range(10):
    ct = li.count(str(i))
    print(ct)
