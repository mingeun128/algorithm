a,b = map(int, input().split())
aa = a
bb = b
while b > 0:
    t = a%b
    a = b
    b = t
aa = aa//a
bb = bb//a
print(a)
print(a*aa*bb)