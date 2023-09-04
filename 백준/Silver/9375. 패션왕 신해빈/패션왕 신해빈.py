import sys
t = int(sys.stdin.readline())
for _ in range(t):
    fasion = {}
    answer = 1
    n = int(sys.stdin.readline())
    for _ in range(n):
        cl = sys.stdin.readline().rstrip().split()
        if cl[1] not in fasion:
            fasion[cl[1]] = []
        fasion[cl[1]].append(cl[0])
    for key in fasion:
        answer *= (len(fasion[key])+1)
    print(answer-1)