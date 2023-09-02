s = input()
d = {}
for i in s:
    if ord(i) >= ord('a'):
        if chr(ord(i)-32) not in d:
            d[chr(ord(i)-32)] = 1
        else:
            d[chr(ord(i)-32)]+=1
    else:
        if i not in d:
            d[i] = 1
        else:
            d[i]+=1
m = 0
mc = ''
flag = True
count = 0
for i in d.keys():
    if d[i] > m:
        m = d[i]
        mc = i
for i in d.keys():
    if d[i] == m:
        count += 1
        if count > 1:
            flag = False
            break
if flag == True:
    print(mc)
else:
    print('?')