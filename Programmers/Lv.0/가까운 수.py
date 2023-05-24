def solution(array, n):
    array.sort()
    answer = array[0]
    min_sub = abs(array[0] - n)
    for i in range(1, len(array)):
        subst = abs(array[i] - n)
        if subst < min_sub:
            min_sub = subst
            answer = array[i]
    return answer