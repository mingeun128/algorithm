import sys

n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline().rstrip())
answer = 0
for i in nums:
    if i == target:
        answer+=1
print(answer)