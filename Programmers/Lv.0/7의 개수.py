def solution(array):
    answer = 0
    array_to_str = ''.join(list(map(str,array)))
    for s in array_to_str:
        if s == '7':
            answer+=1
    return answer