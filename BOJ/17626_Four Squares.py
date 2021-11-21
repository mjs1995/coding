n = int(input())

dp = [0] * 50001
dp[1] = 1

for x in range(1, n + 1):
    ans = 0
    i = x
    while i:
        a = int(i ** 0.5) ** 2
        i -= a
        ans += 1
    dp[x] = ans

    for j in range(1, int(x ** 0.5) + 1):
        dp[x] = min(dp[x], dp[j * j] + dp[x - j * j])

print(dp[n])

# 다이나믹 그램 
import math

n = int(input())
dp = [0] * (n + 1)
dp[0], dp[1] = 0, 1 # [0, 1, 0, 0, 0, 0, ~~~]

# 2^2, 3^2, 4^2 등 제곱수는 1로 만들고 나머지는 그대로 
for i in range(2, n + 1):
    if i == int(math.sqrt(i)) ** 2:
        dp[i] = 1
    else:
        dp[i] = i

for i in range(2, n + 1):
    for j in range(1, int(math.sqrt(i)) + 1):
        dp[i] = min(dp[i], dp[j * j] + dp[i - j * j])

print(dp[n])
