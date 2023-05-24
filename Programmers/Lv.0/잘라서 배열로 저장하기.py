def solution(my_str, n):
    answer = []
    i = 0
    while True:
        if len(my_str) < n:
            if len(my_str) > 0:
                answer.append(my_str)
            break
        else:
            answer.append(my_str[0:n])
            my_str = my_str[n:]
    return answer