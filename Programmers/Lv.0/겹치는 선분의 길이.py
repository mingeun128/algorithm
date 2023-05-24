def solution(lines):
    answer = 0
    x_min = min(list(zip(*lines))[0])
    y_max = max(list(zip(*lines))[1])
    i = x_min + 0.5
    count = 0
    while i < y_max:
        for a,b in lines:
            if a < i and i < b:
                count+=1
        if count > 1:
            answer += 1
        count = 0
        i += 1.0
    return answer