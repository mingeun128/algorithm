def solution(before, after):
    answer = 1
    before_spell = [0]*26
    after_spell = [0]*26
    for b in before:
        before_spell[ord(b)-97]+=1
    for a in after:
        after_spell[ord(a)-97]+=1
    for i in range(26):
        if after_spell[i] != before_spell[i]:
            answer = 0
            break
    return answer