def hanoi(n, start,end,bet):
    if n == 1:
        print(start,end=' ')
        print(end)
        return
    hanoi(n-1,start,bet,end)
    print(start, end = ' ')
    print(end)
    hanoi(n-1,bet,end,start)
N = int(input())
k = 2 ** N -1
print(k)
hanoi(N,1,3,2)
