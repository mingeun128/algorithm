import sys
def countCall(n):
    if n == 0:
        return 1,0
    elif n == 1:
        return 0,1
    else:
        fibo_call_count = [1] + ([0]*n)
        for i in range(n-1):
            fibo_call_count[i+1] += fibo_call_count[i]
            fibo_call_count[i+2] += fibo_call_count[i]
        return fibo_call_count[-1],fibo_call_count[-2]
n = int(sys.stdin.readline())
for i in range(n):
    k = int(sys.stdin.readline())
    zero_count,one_count = countCall(k)
    print('%d %d' % (zero_count,one_count))