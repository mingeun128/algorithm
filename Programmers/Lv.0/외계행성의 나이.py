def solution(age):
    answer = ''
    while age > 0:
        answer = chr(age%10 + 97) + answer
        age //= 10
    return answer