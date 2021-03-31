def gcd(a,b):
    return gcd(b%a,a) if b%a else a

def lcm(a,b):
    d = gcd(a,b)
    return d*(a//d) * (b//d)

t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    print(lcm(a,b))
