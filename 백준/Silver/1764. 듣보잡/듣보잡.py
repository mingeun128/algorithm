n,m = map(int, input().split())
nohear = []
nosee = []
for _ in range(n):
    nohear.append(input())
for _ in range(m):
    nosee.append(input())
nohear_nosee = sorted(list(set(nohear)&set(nosee)))
print(len(nohear_nosee))
for n in nohear_nosee:
    print(n)