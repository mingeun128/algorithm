from collections import deque
def solution(numbers, direction):
    q = deque(numbers)
    if direction == 'left':
        q.rotate(-1)
    elif direction == 'right':
        q.rotate(1)
    answer = list(q)
    return answer