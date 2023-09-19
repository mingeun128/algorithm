t = int(input())
for _ in range(t):
    dp = [0,1,1,1,2,2]
    n = int(input())
    for i in range(6,n+1):
        dp.append(dp[i-5] + dp[i-1])
    print(dp[n])