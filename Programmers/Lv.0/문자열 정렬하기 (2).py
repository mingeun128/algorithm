def solution(my_string):
    answer = ''
    temp = []
    for c in my_string:
        ascii = ord(c)
        if ascii < 97:
            ascii += 32
        temp.append(ascii)
    temp.sort()
    for i in temp:
        answer += chr(i)
    return answer