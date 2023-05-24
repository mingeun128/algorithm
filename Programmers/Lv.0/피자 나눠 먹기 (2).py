def gcd(a,b):
    temp = 0
    mul = a*b
    while b > 0:
        temp = b
        b = a % b
        a = temp
    return mul // a
def solution(n):
    answer = gcd(n,6) // 6
    return answer