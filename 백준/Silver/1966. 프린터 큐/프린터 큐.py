from collections import deque

def check_doc(m,k,plist):
    count = 0
    sorted_plist = plist.copy()
    sorted_plist.sort()
    for i in range(m):
    	plist[i] = (plist[i],i)
    pdeq = deque(plist)
    a = 0
    while True:
        if pdeq[0][0] < sorted_plist[-1]:
            pdeq.append(pdeq.popleft())
        elif pdeq[0][0] == sorted_plist[-1]:
            a = pdeq.popleft()
            sorted_plist.pop()
            count += 1
            if a[1] == k:
            	break
    return count

n = int(input())
for i in range(n):
    m,k = map(int, input().split())
    plist = list(map(int, input().split()))
    print(check_doc(m,k,plist))