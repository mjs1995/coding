def solution(n):
    answer = ""
    res = 0 
    
    while n >= 3:
        answer += str(n%3)
        n = n//3
    answer += str(n)
    for i in range(len(answer)):
        res += int(answer[-(i+1)])*int(3**i)
    return res
    
