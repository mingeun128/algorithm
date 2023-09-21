nums = []
for i in range(9):
    nums.append(int(input()))

max_index = 0
for i in range(1,len(nums)):
    if nums[max_index] < nums[i]:
        max_index = i
print(nums[max_index])
print(max_index+1)