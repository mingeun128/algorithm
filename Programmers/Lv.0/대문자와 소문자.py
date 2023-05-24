def solution(my_string):
    answer = ''
    for s in my_string:
        if ord(s) >= 97:
            answer += chr(ord(s) - 32)
        else:
            answer += chr(ord(s) + 32)
    return answer