import sys
nums = list(map(int, sys.stdin.readline().rstrip().split()))
is_asc = False
is_des = False
if nums[0] == 1:
    is_asc = True
elif nums[0] == 8:
    is_des = True
i = 1
while ((is_asc == True) or (is_des == True)) and i < 8:
    if (is_asc == True) and (nums[i]-nums[i-1]<0):
        is_asc = False
        break
    if (is_des == True) and (nums[i]-nums[i-1]>0):
        is_des = False
        break
    i+=1
if is_asc == True:
    print("ascending")
elif is_des == True:
    print("descending")
else:
    print("mixed")
