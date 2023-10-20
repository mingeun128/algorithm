import sys

hh,mm = map(int, sys.stdin.readline().split())
time = int(sys.stdin.readline().rstrip())

mm += time
if mm >= 60:
    hh += (mm//60)
    mm %= 60
if hh >= 24:
    hh %= 24
print(str(hh) + " " + str(mm))
