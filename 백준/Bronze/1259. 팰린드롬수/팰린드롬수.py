def palindrome_check(s):
    if len(s) == 1:
        return True
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l+=1
        r-=1
    return True
n = input()
while n != '0':
    check = palindrome_check(n)
    if check == True:
        print("yes")
    else:
        print("no")
    n = input()