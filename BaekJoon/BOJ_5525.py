import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
count = 0
Pn = 'IO' * n + 'I'
pn_len = len(Pn)
pi = [0] * pn_len
for i in range(2,pn_len):
    pi[i] = i-1
j=0
for i in range(m):
	while j>0 and s[i] != Pn[j]:
		j = pi[j-1]
	if s[i] == Pn[j]:
		if j == pn_len-1:
			count+=1
            j = pi[j]
		else:
			j+=1
print(count)
