def solution(s):
    ans = ''
    if len(s) % 2 == 0:
        cnt = (len(s) // 2)
        return s[cnt-1:cnt+1]
    else:
        cnt = (len(s) // 2)
        return s[cnt]
