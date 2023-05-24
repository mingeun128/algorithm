def solution(num, total):
    answer = list(range((total//num - (num-1)//2), (total//num + (num//2 + 1))))
    return answer