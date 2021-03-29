class Solution:
    def myAtoi(self, s: str) -> int:
        is_number = False
        start = 0
        end = 0
        if len(s) == 0:
            return 0
        if not(ord(s[0]) >= 48 and ord(s[0]) <= 57) and (s[0] != ' ' and s[0] != '-' and s[0] != '+'):
            return 0
        else:
            i=0
            while i < len(s):
                if s[i] == ' ' and is_number == False:
                    i+=1
                    continue
                elif ord(s[i]) >= 48 and ord(s[i]) <= 57 and is_number == False:
                    if i == 0:
                        start = 0
                    elif i > 0 and (s[i-1] == '-' or s[i-1] == '+') :
                        start = i-1
                    elif i > 0 and (s[i-1] == ' '):
                        start = i
                    else:
                        return 0
                    is_number = True
                elif not(ord(s[i]) >= 48 and ord(s[i]) <= 57) and is_number == True:
                    end = i
                    break
                if i+1 <= len(s) and is_number == True:
                    end = i+1
                i+=1
            print(start,end)
        if start >= end-1:
            return 0
        if start > 0 and s[start-1] != ' ':
            return 0
        if int(s[start:end]) < -2147483648:
            return -2147483648
        elif int(s[start:end]) > 2147483647:
            return 2147483647
        else:
            return(int(s[start:end]))