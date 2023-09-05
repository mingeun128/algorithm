import sys
n = int(sys.stdin.readline())
ns = []
for i in range(n):
    ns.append(int(sys.stdin.readline()))
ns.sort()
summ = 0
while len(ns) > 1 and ns[1] <= 0:
    if ns[0] <= 0 and ns[1] <= 0:
        summ = summ + (ns.pop(0) * ns.pop(0))
while len(ns) > 1 and ns[-2] > 0:
    if ns[-2] == 1:
    	summ = summ + (ns.pop() + ns.pop())
    elif ns[-1] > 0 and ns[-2] > 0:
        summ = summ + (ns.pop() * ns.pop())
for i in ns:
    summ = summ + i
print(summ)