h, m = map(int, input().split())
if m - 45 < 0:
    m = 60 - (45-m)
    h = h-1
else:
    m = m-45
if h < 0:
    h = 24+h
    
print(str(h)+ ' ' + str(m))