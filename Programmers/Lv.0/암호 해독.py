def solution(cipher, code):
    answer = ''
    slen = len(cipher)
    i = code - 1
    while i < slen:
        answer += cipher[i]
        i += code
    return answer