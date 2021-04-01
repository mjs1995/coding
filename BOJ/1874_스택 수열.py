n = int(input())
s = []
p = []
cnt = 1
temp = True
for i in range(n):
    num = int(input())
    while cnt <= num:
        s.append(cnt)
        p.append('+')
        cnt += 1
    if s[-1] == num:
        s.pop()
        p.append('-')
    else:
        temp = False
if temp == False:
    print('NO')
else:
    for i in p:
        print(i)
