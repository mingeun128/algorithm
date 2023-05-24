def solution(num_list, n):
    answer = []
    l = len(num_list)
    for i in range(0,l,n):
        answer.append(num_list[i:i+n])
    return answer