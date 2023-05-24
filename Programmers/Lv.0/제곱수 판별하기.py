def solution(n):
    answer = 2
    count = 1
    for i in range(2,n+1):
        if n%i == 0:
            count+=1
    if count%2 ==1:
        answer = 1
    return answer