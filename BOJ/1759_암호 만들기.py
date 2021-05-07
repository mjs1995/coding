from itertools import combinations

l,c = map(int,input().split())
a = sorted(input().split())
b = set('aeiou')

com = list(combinations(a,l))

for i in com:
    c = set(i) - b
    if 2 <= len(c) and l-len(c) >= 1:
        print("".join(i))
