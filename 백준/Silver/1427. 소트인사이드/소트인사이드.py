import sys
n = int(sys.stdin.readline())
nums = []
answer = ''
while n > 0:
    nums.append(n%10)
    n //= 10
nums.sort(reverse=True)

for i in nums:
    answer += str(i)
print(answer)