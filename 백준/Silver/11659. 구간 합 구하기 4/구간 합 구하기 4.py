import sys
n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums_sum = [0]
summ = 0
for i in range(n):
    summ += nums[i]
    nums_sum.append(summ)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    answer = nums_sum[b] - nums_sum[a-1]
    print(answer)