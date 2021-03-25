num = int(input())
li = []

for _ in range(num):
    age,name = map(str,input().split())
    age = int(age)
    li.append((age,name))
    
li.sort(key = lambda i : i[0])

for m in li:
    print(m[0],m[1])
