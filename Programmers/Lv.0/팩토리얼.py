def solution(n):
    answer = 0
    facto = 1
    while facto <= n:
        answer+=1
        facto*=answer
        
    return answer-1