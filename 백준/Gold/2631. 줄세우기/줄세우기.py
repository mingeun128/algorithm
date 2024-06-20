n = int(input())
inputs = [-1]
for _ in range(n):
    inputs.append(int(input()))
dp = [1] * (n+1)
for i in range(1, n+1):
    for j in range(1, i):
        if inputs[j] < inputs[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))