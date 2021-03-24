start_num = int(input())
last_num = int(input())

li = []
for num in range(start_num,last_num+1):
    res = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                res += 1
                break
        if res == 0:
            li.append(num)
if len(li) > 0:
    print(sum(li))
    print(min(li))
else:
    print(-1)
