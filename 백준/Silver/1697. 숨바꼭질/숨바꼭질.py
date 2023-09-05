from collections import deque

n,m = map(int, input().split())
visited = [False] * 100001
answer = 0
q = deque()
q.append((n,0))
while len(q) > 0:
    cur = q.popleft()
    visited[cur[0]] = True
    if m < n:
        answer = n - m
        break
    if cur[0] == m:
        answer = cur[1]
        break
    if cur[0] - 1 == m or cur[0] * 2 == m or cur[0] + 1 == m:
        answer = cur[1] + 1
        break
    if cur[0] - 1 >= 0 and visited[cur[0] - 1] == False:
        q.append((cur[0] - 1, cur[1] + 1))
    if cur[0] + 1 <= 100000 and visited[cur[0] + 1] == False:
        q.append((cur[0] + 1, cur[1] + 1))
    if cur[0] * 2 <= 100000 and visited[cur[0] *2] == False:
        q.append((cur[0] * 2, cur[1] + 1))
print(answer)