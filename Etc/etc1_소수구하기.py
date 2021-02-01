import math

m,n = map(int,input().split())
array = [True for i in range(1000001)]
array[1] = 0

# 에라토스테네스
for i in range(2, int(math.sqrt(n)) + 1):
  if array[i] == True:
    j = 2
    while i * j <= n:
      array[i*j] = False
      j += 1

for i in range(m, n+1):
  if array[i]:
    print(i)
