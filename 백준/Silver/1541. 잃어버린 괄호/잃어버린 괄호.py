exp = input()
minus_nums = []
plus_nums = []
answer = 0
if exp[0] == '-':
    flag = False
else:
    flag = True
num = ''
for e in exp:
    if e == '+':
        if len(num) > 0:
            if flag == True:
                plus_nums.append(int(num))
            else:
                minus_nums.append(int(num))
                #flag = True
        num = ''
    elif e == '-':
        if len(num) > 0:
            if flag == True:
                plus_nums.append(int(num))
                flag = False
            else:
                minus_nums.append(int(num))
        num = ''
    else:
        num+=e
if flag == True:
    plus_nums.append(int(num))
else:
    minus_nums.append(int(num))
answer += sum(plus_nums)
answer -= sum(minus_nums)
#print(plus_nums)
#print(minus_nums)
print(answer)