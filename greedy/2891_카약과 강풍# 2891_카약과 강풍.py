a,b,c =map(int,input().split())

demage = list(map(int,input().split()))
more = list(map(int,input().split()))
count = b
for i in range(b):
    for j in range(c):
        if (demage[i] == more[j]) or abs(demage[i] - more[j]) == 1:
            count -= 1
            del more[j]
            c -=1
            break
print(count)
