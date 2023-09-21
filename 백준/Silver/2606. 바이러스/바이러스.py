n = int(input())
m = int(input())
visited = [0] * (n+1)
rs = {}
stack = []

for _ in  range(m):
    a,b = map(int, input().split())
    if a not in rs:
        rs[a] = []
    if b not in rs:
        rs[b] = []
    rs[a].append(b)
    rs[b].append(a)

stack.append(1)
while len(stack) > 0:
    cur = stack.pop()
    visited[cur] = 1
    if cur not in rs:
        break
    for i in rs[cur]:
        if visited[i] == 0:
            stack.append(i)
print(sum(visited)-1)