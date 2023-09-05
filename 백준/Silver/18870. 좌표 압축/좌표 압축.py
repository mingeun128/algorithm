import sys
n = int(sys.stdin.readline().rstrip())
answer = [-1] * n
coordis = list(map(int, sys.stdin.readline().split()))
index = list(range(n))
new_coordis = [(c,i) for c,i in zip(coordis,index)]
sorted_coordis = sorted(new_coordis)

count = 0
for i in range(n):
    if i > 0 and sorted_coordis[i][0] != sorted_coordis[i-1][0]:
        count+=1
    answer[sorted_coordis[i][1]] = count

for a in answer:
    print(a, end = ' ')