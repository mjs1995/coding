def gcd(n,m):
    while m>0:
        tmp = m
        m = n%m
        n = tmp
    return n

def solution(n, m):
    val = gcd(max(n,m), min(n,m))
    return [val,(n*m)/val]
