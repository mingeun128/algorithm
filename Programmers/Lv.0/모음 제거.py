def solution(my_string):
    answer = ''
    for c in my_string:
        if c not in ['a','e','i','o','u']:
            answer+=c
    return answer