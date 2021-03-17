N = int (input())
li = list(map(int, input().split()))
res = []
for i in range(N-1):
    cnt = 0
    for j in range(i+1, N):
        if li[i] > li[j]:
            cnt += 1
        else:
            break
    res.append(cnt)
print(max(res))

##
num=int(input())
hills=[int(x) for x in input().split()]

res=0
highest=0
cnt=0

for hill in hills :
  if hill > highest :
    highest = hill
    cnt = 0
  else : 
    cnt +=1
  res = max(res, cnt)

print(res)
