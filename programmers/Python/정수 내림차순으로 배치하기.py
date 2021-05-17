def solution(n):
    new = [int(i) for i in str(n)]
    new.sort(reverse=True)
    return int(''.join(map(str,new)))
