num = list(map(int, input()))

while num[0] != 0:
    if num == num[::-1]:
        print('yes')
    else:
        print('no')
    num = list(map(int, input()))
