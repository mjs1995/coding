from collections import defaultdict
T = int(input())
for _ in range(T):
    a,b = input().split()
    ad = defaultdict(int)
    bd = defaultdict(int)
    
    for char in a:
        ad[char] += 1
        
    for char in b:
        bd[char] += 1
    
    if ad == bd:
        print('{} & {} are anagrams.'.format(a,b))
    else:
        print('{} & {} are NOT anagrams.'.format(a,b))
