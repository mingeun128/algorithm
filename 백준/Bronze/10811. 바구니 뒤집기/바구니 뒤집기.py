import sys
n,m = map(int, sys.stdin.readline().split())
bucket = list(range(1, n+1))
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    temp = bucket[a-1:b]
    temp.reverse()
    bucket = bucket[:a-1] + temp + bucket[b:]
print(" ".join(map(str, bucket)))