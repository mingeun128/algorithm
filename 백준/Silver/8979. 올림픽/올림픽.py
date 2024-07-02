import sys
n, k = map(int, sys.stdin.readline().split())
nara = []
for _ in range(n):
    inputt = list(map(int, sys.stdin.readline().split()))
    nara.append(((inputt[1],inputt[2],inputt[3]),(inputt[0])))
ranking = sorted(nara, key=lambda x: (-x[0][0],-x[0][1],-x[0][2]))
answer = 1
if nara[0][1] != k:
    for i in range(1,n):
        if ranking[i][0][0] != ranking[i-1][0][0] or ranking[i][0][1] != ranking[i-1][0][1] or ranking[i][0][2] != ranking[i-1][0][2]:
            answer = i+1
        if ranking[i][1] == k:
            break
rank = [1]
for i in range(1,n):
    if ranking[i][0][0] == ranking[i-1][0][0] and ranking[i][0][1] == ranking[i-1][0][1] and ranking[i][0][2] == ranking[i-1][0][2]:
        rank.append(rank[i-1])
    else:
        rank.append(i+1)
    if ranking[i][1] == k:
        answer = i+1
        break
print(answer)