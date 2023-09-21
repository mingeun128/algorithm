import sys

n = int(sys.stdin.readline())
scores = [0]
dp = [0] * (n+1)
for _ in range(n):
    scores.append(int(sys.stdin.readline()))
for i in range(1,n+1):
    if i < 3:
        dp[i] = dp[i-1] + scores[i]
    else:
        dp[i] = max(dp[i-2] , scores[i-1] + dp[i-3]) + scores[i]

print(dp[-1])