import sys
sugar = int(sys.stdin.readline())
bag = 0
isPosible = False
while sugar >=0:
    if sugar % 5 == 0:
        bag+=(sugar//5)
        isPosible = True
        break
    else:
        sugar-=3
        bag+=1
if isPosible == True:
    print(bag)
else:
    print(-1)