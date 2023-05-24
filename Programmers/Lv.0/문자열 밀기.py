def solution(A, B):
    answer = 0
    length = len(A)
    for i in range(length):
        if A == B:
            break
        B = B[1:] + B[0]
        answer+=1
    if answer == length:
        answer = -1
    return answer