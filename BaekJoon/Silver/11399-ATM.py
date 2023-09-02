import sys
n = int(sys.stdin.readline())
times = list(map(int, sys.stdin.readline().split()))
times.sort()
for i in range(1,n):
    times[i] += times[i-1]
answer = times[0]
for i in range(1,n):
    answer += times[i]
print(answer)