def solution(keyinput, board):
    answer = [0,0]
    half_width = (board[0]-1)//2
    half_height = (board[1]-1)//2
    for keyword in keyinput:
        if keyword == 'left':
            if answer[0] > -half_width:
                answer[0] -= 1
        if keyword == 'right':
            if answer[0] < half_width:
                answer[0] += 1
        if keyword == 'up':
            if answer[1] < half_height:
                answer[1] += 1
        if keyword == 'down':
            if answer[1] > -half_height:
                answer[1] -= 1
    return answer