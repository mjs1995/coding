for _ in range(int(input())):
    n = int(input())
    tmp1 = list(map(str, input().split()))
    tmp2 = list(map(str, input().split()))
    if sorted(tmp1) == sorted(tmp2):
        print("NOT CHEATER")
    else:
        print("CHEATER")
