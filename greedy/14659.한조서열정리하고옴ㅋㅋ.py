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
