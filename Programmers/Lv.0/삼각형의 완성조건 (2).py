def solution(sides):
    answer = 0
    l = max(sides)
    s = min(sides)
    answer = l+s - (l-s) -1
    return answer