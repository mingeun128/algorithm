def solution(price):
    answer = price
    if price >= 500000:
        answer = answer * 80 // 100
    elif price >= 300000:
        answer = answer * 90 // 100
    elif price >= 100000:
        answer = answer * 95 // 100
    return answer