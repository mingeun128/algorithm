def solution(my_string):
    answer = ''
    strlist = []
    for i in my_string:
        if i not in strlist:
            strlist.append(i)
    answer = ''.join(strlist)
    return answer