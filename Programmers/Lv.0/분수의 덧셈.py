def gcd(a,b):
    while a > 0:
        temp = a
        a = b%a
        b = temp
    return b
def solution(numer1, denom1, numer2, denom2):
    answer = []
    answer.append(numer1*denom2 + numer2*denom1)
    answer.append(denom1*denom2)
    gcd_ = 0
    gcd_ = gcd(answer[0], answer[1])
    answer[0] = answer[0] // gcd_
    answer[1] = answer[1] // gcd_
    return answer