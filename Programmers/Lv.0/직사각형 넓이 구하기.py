def solution(dots):
    answer = 0
    xs = list(zip(*dots))[0]
    ys = list(zip(*dots))[1]
    answer = (max(xs) - min(xs)) * (max(ys) - min(ys))
    return answer