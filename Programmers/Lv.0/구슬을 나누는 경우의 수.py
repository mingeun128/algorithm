def facto(n):
    f = 1
    for i in range(1,n+1):
        f*=i
    return f
def combi(a, b):
    return facto(a)/facto(a-b)/facto(b)
def solution(balls, share):
    answer = combi(balls,share)
    return answer