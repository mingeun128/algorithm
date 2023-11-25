import sys
S = sys.stdin.readline().rstrip()
P = S[::-1]
if S == P:
    print(1)
else:
    print(0)