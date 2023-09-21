import sys
n1, n2 = sys.stdin.readline().rstrip().split()
if int(n1[::-1]) > int(n2[::-1]):
    print(n1[::-1])
else:
    print(n2[::-1])