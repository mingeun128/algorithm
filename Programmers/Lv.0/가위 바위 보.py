def solution(rsp):
    answer = ''
    for s in rsp:
        if s == '0':
            answer += '5'
        elif s == '2':
            answer += '0'
        elif s == '5':
            answer += '2'
    return answer