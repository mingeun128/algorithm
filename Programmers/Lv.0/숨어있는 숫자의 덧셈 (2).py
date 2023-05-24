def solution(my_string):
    answer = 0
    num_buffer = []
    strnum = ''
    for i in range(len(my_string)):
        if ord(my_string[i]) >= 48  and ord(my_string[i]) < 58:
            strnum += my_string[i]
            if i == len(my_string)-1:
                num_buffer.append(int(strnum))
                strnum = ''
        else:
            if len(strnum) > 0:
                num_buffer.append(int(strnum))
                strnum = ''
    answer = sum(num_buffer)
    return answer