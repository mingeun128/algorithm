import sys
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    for j in range(i + n):
        if j < n - i -1:
            print(" ", end='')
        else:
            print("*", end='')
    print()
for i in range(n - 1):
    for j in range(2 * (n-1) - i):
        if j < i + 1:
            print(" ", end='')
        else:
            print("*", end='')
    print()
