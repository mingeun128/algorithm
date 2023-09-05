n = int(input())
for i in range(1,1000000):
    j = i
    jj = j
    ans = j
    while j > 0:
        jj += (j%10)
        j //= 10
    if n == jj:
        break
if n == jj:
    print(ans)
else:
    print(0)