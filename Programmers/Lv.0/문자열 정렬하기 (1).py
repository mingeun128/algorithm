def solution(my_string):
    answer = []
    for s in my_string:
        if ord(s) >= 48 and ord(s) <= 57:
            answer.append(int(s))
    answer.sort()
    return answer