from itertools import permutations
a,b = input().split()
for i in permutations(sorted(a),int(b)):
    print(''.join(i))
