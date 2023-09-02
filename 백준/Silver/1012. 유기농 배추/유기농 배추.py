from collections import deque
import sys
dx = [1,0,-1,0]
dy = [0,1,0,-1]
def bfs(x,y,m,n):
    q = deque()
    q.append((x,y))
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if ny < m and nx > -1 and nx < n and ny > -1:
                if highlands[nx][ny] == 1:
                    q.append((nx,ny))
                    highlands[nx][ny] = 666
                    
c = int(sys.stdin.readline())
for i in range(c):
    count = 0
    m,n,k = map(int, sys.stdin.readline().split())
    highlands = [[0] * m for _ in range(n)]
    
    for j in range(k):
        a,b = map(int, sys.stdin.readline().split())
        highlands[b][a] = 1
    for j in range(n):
        for k in range(m):
            if highlands[j][k] == 1:
                bfs(j,k,m,n)
                count+=1
    print(count)