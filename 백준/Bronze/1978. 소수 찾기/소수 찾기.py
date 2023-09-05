n = int(input())
nums = list(map(int, input().split()))
nums.sort()
count = 0
check_prime = [False,False] + ([True] * (nums[-1] - 1))
for i in range(2,len(check_prime)):
    if check_prime[i] == True:
        for j in range(i*2,len(check_prime),i):
            check_prime[j] = False
for i in nums:
    if check_prime[i] == True:
        count+=1
print(count)