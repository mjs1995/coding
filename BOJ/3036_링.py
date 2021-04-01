n = int(input())
rad = list(map(int, input().split()))

for i in range(n-1):
    x = rad[0]
    y = rad[i+1]
    while (x % y != 0):
        r = x%y
        x = y
        y = r
    d = rad[0] // y
    num = rad[i+1] // y
    print(f'{d}/{num}')
