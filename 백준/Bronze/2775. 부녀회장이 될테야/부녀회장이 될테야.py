n = int(input())
lives = []
for i in range(n):
    a = int(input())
    b = int(input())
    lives.append((a,b))
max_floor = lives[0][0]
for i in range(1,n):
    if max_floor < lives[i][0]:
        max_floor = lives[i][0]
apart = [[]]
for i in range(14):
    apart[0].append(i+1)
for i in range(1,max_floor+1):
    apart.append([0]*14)
    apart[i][0] = 1
    for j in range(1,14):
        apart[i][j] = apart[i-1][j] + apart[i][j-1]
for i in range(n):
    print(apart[lives[i][0]][lives[i][1]-1])