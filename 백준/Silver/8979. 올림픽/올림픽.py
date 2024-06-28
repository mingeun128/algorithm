import sys
n,k = map(int, sys.stdin.readline().split())
nara = []
rank = []
for _ in range(n):
    inputt = list(map(int, sys.stdin.readline().split()))
    nara.append((str(inputt[1]) + str(inputt[2]) + str(inputt[3]),inputt[0]))
nara.sort()
answer = 1
for i in range(1,n):
    answer+=1
    if nara[i][0] == nara[i-1][0]:
        answer-=1
    if nara[i][1] == k:
        break
print(answer)