from collections import deque

n,m,v = map(int, input().split())
graph = {}
for i in range(m):
    key,val = map(int, input().split())
    if key not in graph:
        graph[key] = []
    graph[key].append(val)
    if val not in graph:
        graph[val] = []
    graph[val].append(key)
for k in graph.keys():
	graph[k].sort()
##DFS
stack = [v]
visited_dfs = []
while stack:
	n = stack.pop()
	if n not in visited_dfs:
		visited_dfs.append(n)
		if n not in graph:
			continue
		for i in range(len(graph[n])-1,-1,-1):
			stack.append(graph[n][i])
##BFS
queue = deque([v])
visited_bfs = []
while len(list(queue)):
	n = queue.pop()
	if n not in visited_bfs:
		visited_bfs.append(n)
		if n not in graph:
			continue
		for i in range(len(graph[n])):
			queue.appendleft(graph[n][i])

for i in visited_dfs:
	print(i,end=' ')
print('')
for i in visited_bfs:
	print(i,end=' ')
