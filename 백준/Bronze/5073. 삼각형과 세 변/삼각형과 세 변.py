import sys
while True:
    nums = list(map(int, sys.stdin.readline().split()))
    if nums[0] == 0 and nums[1] == 0 and nums[2] == 0:
        break
    if nums[0] == nums[1] and nums[0] == nums[2]:
        print('Equilateral')
        continue
    max_num = nums[0]
    max_index = 0
    for i in range(1,3):
        if nums[i] > max_num:
            max_num = nums[i]
            max_index = i
    sum = 0
    for i in range(3):
        if i == max_index:
            continue
        sum+=nums[i]
    if sum <= max_num:
        print('Invalid')
    else:
        if len(set(nums)) == 2:
            print('Isosceles')
        elif len(set(nums)) == 3:
            print('Scalene')