import sys

n = int(sys.stdin.readline())
dp = [0, 1, 2] + [0]*(n-2)
for i in range(3,n+1):
    dp[i] = (dp[i-1] + dp[i-2])%10007
print(dp[n])