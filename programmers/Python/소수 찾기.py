def solution(n):
    num = set(range(2,n+1))
    for i in range(2,n+1):
        if i in num:
            num -= set(range(2*i, n+1,i))
        
    return len(num)
  
def solution(n):
    count = 0
    for n in range(2, n+1):
        for i in range(2,n):
            if n % i == 0:
                break
            else:
                count += 1
    return count  
