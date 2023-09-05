import sys
L = list(input())
n = int(sys.stdin.readline())
R = []
for i in range(n):
    data = sys.stdin.readline().split()
    if data[0] == 'L' and len(L) > 0:
        R.append(L.pop())
    elif data[0] == 'D' and len(R) > 0:
        L.append(R.pop())
    elif data[0] == 'B' and len(L) > 0:
        L.pop()
    elif data[0] == 'P':
        L.append(data[1])
R.reverse()
print(''.join(L+R))