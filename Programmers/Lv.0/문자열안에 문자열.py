def solution(str1, str2):
    answer = 2
    slen1 = len(str1)
    slen2 = len(str2)
    for i in range(slen1-slen2+1):
        if str1[i:i+slen2] == str2:
            answer = 1
            break
        
    return answer