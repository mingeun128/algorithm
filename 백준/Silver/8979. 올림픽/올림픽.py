import sys
n, k = map(int, sys.stdin.readline().split())
nara = []
for _ in range(n):
    inputt = list(map(int, sys.stdin.readline().split()))
    nara.append((str(inputt[1]) + str(inputt[2]) + str(inputt[3]),inputt[0]))
nara.sort()
nara.reverse()
answer = 1
if nara[0][1] != k:
    for i in range(1,n):
        if nara[i][0] != nara[i-1][0]:
            answer = i+1
        if nara[i][1] == k:
            break
print(answer)