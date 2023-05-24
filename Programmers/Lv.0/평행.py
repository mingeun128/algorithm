def solution(dots):
    answer = 0
    x1 = dots[0][0]
    y1 = dots[0][1]
    x2 = dots[1][0]
    y2 = dots[1][1]
    x3 = dots[2][0]
    y3 = dots[2][1]
    x4 = dots[3][0]
    y4 = dots[3][1]
    if (y1 - y2) / (x1 - x2) == (y3 - y4) / (x3 - x4):
        answer = 1
    elif (y1 - y3) / (x1 - x3) == (y2 - y4) / (x2 - x4):
        answer = 1
    elif (y1 - y4) / (x1 - x4) == (y2 - y3) / (x2 - x3):
        answer = 1
    return answer