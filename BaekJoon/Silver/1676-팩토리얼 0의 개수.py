import sys

n = int(sys.stdin.readline())
two_count = 0
five_count = 0
for i in range(n,0,-1):
    t = i
    while t % 2 == 0:
        two_count += 1
        t = t // 2
    f = i
    while f % 5 == 0:
        five_count += 1
        f = f // 5
print(min(two_count,five_count))
