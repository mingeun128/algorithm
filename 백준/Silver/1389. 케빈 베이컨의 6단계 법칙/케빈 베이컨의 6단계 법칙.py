INF = 99999999
n,m = map(int, input().split())
rs = [[INF] * n for _ in range(n)] 
for i in range(m):
    a,b = map(int, input().split())
    rs[a-1][b-1] = 1
    rs[b-1][a-1] = 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            rs[i][j] = min(rs[i][j], rs[i][k] + rs[k][j])
kb = []
for i in range(n):
    k = 0
    for j in range(n):
        if rs[i][j] != INF:
            k+=rs[i][j]
    kb.append(k)
answer = 0
min_r = kb[0]
for i in range(n):
    if min_r > kb[i]:
        min_r = kb[i]
        answer = i
print(answer+1)