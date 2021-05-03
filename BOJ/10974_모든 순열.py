from itertools import permutations

n = int(input())
number = [i for i in range(1, n+1)]

for num in list(permutations(number)):
    for nu in num:
        print(nu , end = ' ')
    print()
