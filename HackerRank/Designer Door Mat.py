n,m = map(int, input().split())
a = '.|.'
b = 'WELCOME'

i = 1
while i <= n-2:
    print((a*i).center(m,'-'))
    i += 2
    
print(b.center(m,'-'))

i = n-2
while i >= 1:
    print((a*i).center(m,'-'))
    i -= 2
