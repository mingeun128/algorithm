import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
mapp = []
visited = [[False]*n for _ in range(n)]
areas = []
danji = 0
for _ in range(n):
    mapp.append(list(map(int, sys.stdin.readline().rstrip())))
def bfs(x,y,n):
    area = 1
    q = deque([(x,y)])
    visited[x][y] = True
    while len(q) > 0:
        cur = q.popleft()
        
        if cur[0] < n-1:
            if mapp[cur[0]+1][cur[1]] == 1 and visited[cur[0]+1][cur[1]] != True:
                q.append((cur[0]+1,cur[1]))
                visited[cur[0]+1][cur[1]] = True
                area += 1
        if cur[0] > 0:
            if mapp[cur[0]-1][cur[1]] == 1 and visited[cur[0]-1][cur[1]] != True:
                q.append((cur[0]-1,cur[1]))
                visited[cur[0]-1][cur[1]] = True
                area += 1
        if cur[1] < n-1:
            if mapp[cur[0]][cur[1]+1] == 1 and visited[cur[0]][cur[1]+1] != True:
                q.append((cur[0],cur[1]+1))
                visited[cur[0]][cur[1]+1] = True
                area += 1
        if cur[1] > 0:
            if mapp[cur[0]][cur[1]-1] == 1 and visited[cur[0]][cur[1]-1] != True:
                q.append((cur[0],cur[1]-1))
                visited[cur[0]][cur[1]-1] = True
                area += 1
    return area

for i in range(n):
    for j in range(n):
        if mapp[i][j] == 1 and visited[i][j] != True:
            areas.append(bfs(i,j,n))
            danji += 1
print(danji)
areas.sort()
for i in areas:
    print(i)