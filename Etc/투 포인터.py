n = 5
m = 5
data = [1 , 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

for start in range(n):
  while interval_sum < m and end < n:
    interval_sum += data[end]
    end += 1
  if interval_sum == m:
    count += 1
  interval_sum -= data[start]

print(count)

######
n,m = 3,4
a = [1,3,5]
b = [2,4,6,8]

result = [0] * (n + m)
i = 0
j = 0
k = 0

while i < n or j < m :
  if j >= m or (i < n and a[i] <= b[j]):
    result[k] = a[i]
    i +=1
  else:
    result[k] = b[j]
    j += 1
  k += 1

for i in result:
  print(i, end = ' ')
  
### 구간합
n = 5
data = [10,20,30,40,50]

sum_value = 0
prefix_sum = [0]
for i in data:
  sum_value += i
  prefix_sum.append(sum_value)
  
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left-1])

###순열
import itertools

data = [1,2]
for x in itertools.permutations(data,2):
  print(list(x))
  
###조합
import itertools

data = [1,2,3]

for x in itertools.combinations(data,2):
  print(list(x), end = ' ')
