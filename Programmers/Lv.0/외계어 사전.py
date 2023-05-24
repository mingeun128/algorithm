def solution(spell, dic):
    answer = 2
    for s in dic:
        if set(spell) == set(s):
            answer = 1
            break
    return answer