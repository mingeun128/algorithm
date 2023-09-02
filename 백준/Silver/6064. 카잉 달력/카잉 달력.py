import sys
T = int(sys.stdin.readline().rstrip())

def gcd(a,b):
    while b > 0:
        t = b
        b = a % b
        a = t
    return a
for _ in range(T):
    answer = -1
    m,n,x,y = map(int, sys.stdin.readline().rstrip().split())
    cal = []
    gcdd = gcd(m,n)
    gcmm = m*n//gcdd
    a = x
    while True:
        if a > gcmm:
            answer = -1
            break
        if ((a-1) % n)+1 == y:
            answer = a
            break
        else:
            a += m
    print(answer)