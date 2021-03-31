n = int(input())
n_list = list(map(int,input().split()))
dp = [0 for _ in range(n)]
res = -1001

for i in range(n):
    dp[i] = max(dp[i-1] + n_list[i], n_list[i])
    print(dp[i])
    res = max(res,dp[i])
    print('--',res)
print(res)
