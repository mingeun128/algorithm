def solution(emergency):
    elen = len(emergency)
    answer = [0]*elen
    emergency_index = [(emergency[i],i) for i in range(elen)]
    emergency_index.sort(reverse=True)
    print(emergency_index)
    for i in range(elen):
        answer[emergency_index[i][1]] = i+1
    return answer