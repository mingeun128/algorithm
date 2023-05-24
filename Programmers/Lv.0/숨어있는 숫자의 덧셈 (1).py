def solution(my_string):
    answer = 0
    for c in my_string:
        if ord(c) <= 57 and ord(c) >= 48:
            answer += int(c)
    return answer