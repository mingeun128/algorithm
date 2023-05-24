def gcd(a, b):
    temp = 0
    while a > 0:
        temp = a
        a = b%a
        b = temp
    return b
def solution(a, b):
    answer = 0
    b = b / gcd(a,b)
    while True:
        if b % 2 == 0:
            b //= 2
            continue
        if b % 5 == 0:
            b //= 5
            continue
        else:
            break
    if b > 1:
        answer = 2
    else:
        answer = 1
    return answer