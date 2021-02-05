data = input()
count0 = 0 #전부 0
count1 = 0 #전부 1

if data[0] == '1':
    count0 += 1
else:
    count1 += 1
    
# 2번째 부터 모든 원소 확인
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1
            
print(min(count0, count1))
