def solution(babbling):
    answer = 0
    for i in range(len(babbling)):
        for j in ['aya', 'ye', 'woo', 'ma']:
            babbling[i] = babbling[i].replace(j, '*')
    for i in babbling:
        bab = list(set(list(i)))
        if len(bab) == 1 and bab[0] == '*':
            answer += 1
    return answer