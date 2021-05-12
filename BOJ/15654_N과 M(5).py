from itertools import permutations

n,m = map(int,input().split())
n_li = sorted(list(map(int,input().split())))
              
for number in list(permutations(n_li,m)):
    for num in number:
        print(num,end=' ')
    print()
