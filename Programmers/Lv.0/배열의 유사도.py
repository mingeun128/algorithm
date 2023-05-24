def solution(s1, s2):
    answer = 0
    ss1 = set(s1)
    ss2 = set(s2)
    answer = len(ss1&ss2)
    return answer