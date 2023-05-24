def solution(n):
    answer = []
    if n%2 == 1:
        n+=1
    for i in range(1,n,2):
        answer.append(i)
    return answer