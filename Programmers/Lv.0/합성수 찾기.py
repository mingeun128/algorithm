def composite_number(n):
    count = 0
    is_composite = False
    for i in range(1,n+1):
        if n % i == 0:
            count +=1
        if count > 2:
            is_composite = True
            break
    return is_composite
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if composite_number(i):
            answer+=1
    return answer