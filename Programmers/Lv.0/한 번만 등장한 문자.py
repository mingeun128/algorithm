def solution(s):
    answer = ''
    count_list = [0]*26
    for c in s:
        count_list[ord(c)-97] += 1
    for i in range(26):
        if count_list[i] == 1:
            answer+=chr(i+97)
    return answer