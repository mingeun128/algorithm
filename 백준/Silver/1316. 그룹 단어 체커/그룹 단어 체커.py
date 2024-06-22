def is_group_word(word):
    used = [0]*26
    i=1
    used[ord(word[0])-ord('a')] = 1
    n = len(word)
    if n == 1:
        return True
    while i < n:
        ascii = ord(word[i])-ord('a')
        if word[i] != word[i-1]:
            if used[ascii] != 0:
                return False
            else:
                used[ascii] = 1
        i+=1
    return True
n = int(input())
count = 0
for _ in range(n):
    if is_group_word(input()):
        count+=1
print(count)