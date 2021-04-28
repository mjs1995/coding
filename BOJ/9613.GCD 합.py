from itertools import combinations

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

for _ in range(int(input())):
    arr = list(map(int,input().split()))
    res = 0
    for a in list(combinations(arr[1:],2)):
        #print('#',a)
        if a[0] > a[1]:
            res += gcd(a[0],a[1])
        else:
            res += gcd(a[1],a[0])
    print(res)
