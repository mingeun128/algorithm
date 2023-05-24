def solution(i, j, k):
    answer = 0
    num_string = ''
    for i in range(i,j+1):
        num_string += str(i)
    for s in num_string:
        if str(k) == s:
            answer += 1
    return answer