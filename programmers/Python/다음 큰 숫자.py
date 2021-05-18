def solution(n):
    one_count = bin(n).count('1')
    for i in range(n+1, 100001):
        if bin(i).count('1') == one_count:
            return i
