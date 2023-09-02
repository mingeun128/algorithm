import sys
n,r,c = map(int, sys.stdin.readline().split())
sp = 0
sx = 0
sy = 0
while n > 1:
    w = 2 ** (n-1)
    if r < (sy + w) and c < (sx + w): #UL
        pass
    elif r < (sy + w) and c >= (sx + w): #UR
        sp += (w**2)
        sx += w
    elif r >= (sy + w) and c < (sx + w): #DL
        sp += ((w**2)*2)
        sy += w
    elif r >= (sy + w) and c >= (sx + w): #DR
        sp += ((w**2)*3)
        sx += w
        sy += w
    n-=1
if r == sy and c == sx: #UL
    print(sp)
elif r == sy and c > sx: #UR
    print(sp+1)
elif r > sy and c == sx: #DL
    print(sp+2)
elif r > sy and c > sx: #DR
    print(sp+3)