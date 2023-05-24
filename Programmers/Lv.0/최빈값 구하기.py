def solution(array):
    answer = 0
    array_set = set(array)
    dir_count = {}
    for i in array_set:
        c = array.count(i)
        if c not in dir_count:
            dir_count[c] = []
        dir_count[c].append(i)
    m = max(dir_count.keys())
    if len(dir_count[m]) == 1:
        answer = dir_count[m][0]
    else:
        answer = -1
    return answer