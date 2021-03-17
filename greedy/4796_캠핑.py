i = 1
while True:
    L,P,V = map(int, input().split())
    if L+P+V == 0:
        break
    res = (V//P) * L
    res += min((V%P), L)
    print('Case %d: %d' % (i,res))
    i += 1
