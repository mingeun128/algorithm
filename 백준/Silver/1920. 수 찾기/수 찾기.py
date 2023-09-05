def find_num(nums, k):
    if k < nums[0]:
        return False
    elif k > nums[-1]:
        return False
    l = 0
    r = len(nums)-1
    while l<=r:
        mid = (l+r)//2
        if k > nums[mid]:
            l = mid+1
        if k < nums[mid]:
            r = mid-1
        if k == nums[mid]:
            return True
    return False

n = int(input())
A = list(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))
A.sort()
for i in M:
    find = find_num(A,i)
    if find == True:
        print("1")
    else:
        print("0")