import sys

n,m = map(int, sys.stdin.readline().split())
box = [0] * n
for _ in range(m):
    start, end, num = map(int, sys.stdin.readline().split())
    for i in range(start-1, end):
        box[i] = num
for i in box:
    print(i, end=' ')