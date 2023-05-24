def get_answer(s):
    hang = s.split(' ')
    if hang[1] == '-':
        if int(hang[0]) - int(hang[2]) == int(hang[4]):
            result = True
        else:
            result = False
    elif hang[1] == '+':
        if int(hang[0]) + int(hang[2]) == int(hang[4]):
            result = True
        else:
            result = False
    return result
def solution(quiz):
    answer = []
    for q in quiz:
        if get_answer(q) == True:
            answer.append('O')
        else:
            answer.append('X')
    return answer