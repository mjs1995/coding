from itertools import combinations
a,b = input().split()
for i in range(1,int(b) +1):
    for j in combinations(sorted(a),i):
        print(''.join(j))
