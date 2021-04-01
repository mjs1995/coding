n = int(input())
for _ in range(n):
    st = list(input())
    cnt = 0
    
    while (len(st) != 0):
        if (cnt < 0):
            break
        res = st.pop()
        
        if (res == '(') :
            cnt -= 1
        elif (res == ')') :
            cnt += 1
    if (cnt == 0):
        print('YES')
    else:
        print('NO')
