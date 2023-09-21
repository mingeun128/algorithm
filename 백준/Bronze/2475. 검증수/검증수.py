nums = list(map(int, input().split()))
summ = 0
for i in nums:
    summ += (i*i)
print(summ%10)