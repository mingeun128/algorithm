def solution(my_string):
    ops = my_string.split()
    answer = int(ops[0])
    for o in range(1,len(ops)-1,2):
        if ops[o] == '+':
            answer += int(ops[o+1])
        elif ops[o] == '-':
            answer -= int(ops[o+1])
    return answer