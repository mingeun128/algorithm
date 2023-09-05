from collections import deque
n,m = map(int, input().split())
maze = []
jobs = deque()
visited = [[False]*m for _ in range(n)]
for _ in range(n):
    line = input()
    maze.append(list(line))
jobs.append((0,0,1))
visited[0][0] = True
while len(jobs) > 0:
    cur = jobs.popleft()
    if cur[0] == n-1 and cur[1] == m-1:
        print(cur[2])
        break
    if cur[0] - 1 > -1:
        if visited[cur[0]-1][cur[1]] == False and maze[cur[0]-1][cur[1]] == '1':
            visited[cur[0]-1][cur[1]] = True
            jobs.append((cur[0]-1,cur[1],cur[2]+1))
    if cur[0] + 1 < n:
        if visited[cur[0]+1][cur[1]] == False and maze[cur[0]+1][cur[1]] == '1':
            visited[cur[0]+1][cur[1]] = True
            jobs.append((cur[0]+1,cur[1],cur[2]+1))
    if cur[1] - 1 > -1:
        if visited[cur[0]][cur[1]-1] == False and maze[cur[0]][cur[1]-1] == '1':
            visited[cur[0]][cur[1]] = True
            jobs.append((cur[0],cur[1]-1,cur[2]+1))
    if cur[1] + 1 < m:
        if visited[cur[0]][cur[1]+1] == False and maze[cur[0]][cur[1]+1] == '1':
            visited[cur[0]][cur[1]] = True
            jobs.append((cur[0],cur[1]+1,cur[2]+1))