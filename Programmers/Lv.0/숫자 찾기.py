def solution(num, k):
    answer = -1
    i = 0
    while num > 0:
        if num % 10 == k:
            answer = i
        num //= 10
        i+=1
    if answer == -1:
        return answer
    else:
        return i - answer