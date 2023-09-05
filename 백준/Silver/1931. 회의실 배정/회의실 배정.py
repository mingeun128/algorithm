import sys
n = int(sys.stdin.readline())
times = []
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    times.append((b,a))
times.sort()
answers = [times[0]]
for i in range(1,n):
    if times[i][1] >= answers[-1][0]:
        answers.append(times[i])
print(len(answers))