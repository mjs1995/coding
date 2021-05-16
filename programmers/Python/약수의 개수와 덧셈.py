def find_divisor(num):
   count = 0
   for i in range(1, num+1):
      if num%i==0:
         count += 1
   # 짝수이면 1
   if count%2 == 0:
      return 1
   # 홀수이면 0
   else:
      return 0
    
def solution(left, right):
    ans = 0
    for i in range(left,right+1):
        if find_divisor(i) == 0:
            ans -= i
        else:
            ans += i
    return ans
