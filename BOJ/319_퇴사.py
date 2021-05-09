n = int(input())
work_pay = []
max_pay = [0]*n

for _ in range(n):
    work_pay.append(list(map(int,input().split())))
    
for i in range(n-1,-1,-1): #뒤에서 부터 다이나믹 프로그래밍
    day = work_pay[i][0]
    pay = work_pay[i][1]
    
    if day > n-i:
        if i != n-1:
            max_pay[i] = max_pay[i+1]
        continue
    if i == n-1:
        max_pay[i] = pay
    elif i + day == n:
        max_pay[i] = max(pay,max_pay[i+1])
    else:
        max_pay[i] = max(pay + max_pay[i +day], max_pay[i+1])
        
print(max_pay[0])
