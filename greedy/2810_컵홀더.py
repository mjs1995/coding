n = int(input())
a = input()
count = a.count('LL')
if (count <= 1):
    print(len(a))
else:
    print(len(a) - count + 1)
