n = int(input())
dp = [-1, 1, 0, 1] + [-1] * (n-3)
result = -1
if n == 1:
    result = 1
elif n == 2:
    result = 0
elif n == 3:
    result = 1
else:
    for i in range(4, n+1):
        if dp[i-1] == 1 or dp[i-3]:
            dp[i] = 0
        else:
            dp[i] = 1
    result = dp[-1]
if result == 0:
    print('CY')
else:
    print('SK')