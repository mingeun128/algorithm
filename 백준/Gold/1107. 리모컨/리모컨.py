import sys
t = int(sys.stdin.readline())
n = int(sys.stdin.readline())
ns = sys.stdin.readline().split()
answer = abs(t - 100)
flag = True
for i in range(1000001):
	tt = list(str(i))
	for j in tt:
		if j in ns:
			flag = False
			break
	if flag == True:
		answer = min(answer, len(str(i)) + abs(i-t))
	flag = True
print(answer)