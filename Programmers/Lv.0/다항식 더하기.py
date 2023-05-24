def solution(polynomial):
    answer = ''
    hang = polynomial.split(' + ')
    xone = 0
    xzero = 0
    for x in hang:
        if 'x' in x:
            if len(x) > 1:
                xone += int(x[:-1])
            else:
                xone += 1
        else:
            xzero += int(x)
    if xone == 1:
        answer += 'x'
    elif xone > 1:
        answer += (str(xone) + 'x')
    if xzero > 0:
        answer = answer + ' + ' + str(xzero)
    if xone == 0:
        if xzero == 0:
            answer = '0'
        else:
            answer = str(xzero)
    return answer