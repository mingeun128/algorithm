import sys
c = list(map(int, sys.stdin.readline().split()))
a = [1, 1, 2, 2, 2, 8]
for i in range(len(a)):
    print(a[i] - c[i], end=' ')