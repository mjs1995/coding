def is_prime_number(x):
  for i in range(2,x):
    if x % i == 0:
      return False
    return True
print(is_prime_number(4))
print(is_prime_number(7))

import math
def is_prime_number(x):
  for i in range(2, int(math.sqrt(x)) + 1):
    if x % i == 0:
    return False
print(is_prime_number(4))
print(is_prime_number(7))


#에라토스테네스의 알고리즘
import math
n = 1000
array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n)) + 1):
  if array[i] == True:
    j = 2
    while i * j <= n:
      array[i * j] = False
      j += 1
for i in range(2, N+1):
  if array[i]:
    print(i, end= ' ')
    
