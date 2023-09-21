import sys
nums = []
for i in range(10):
    nums.append(int(sys.stdin.readline().rstrip()))
mod_result = []
for i in range(10):
    mod_result.append(nums[i]%42)
mod_result = list(set(mod_result))
print(len(mod_result))