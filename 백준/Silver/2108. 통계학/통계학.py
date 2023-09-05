n = int(input())
nums = []
nums_count = {}
sum = 0

for i in range(n):
	nums.append(int(input()))
	sum += nums[i]
nums.sort()

for i in range(n):
	if nums[i] not in nums_count:
		nums_count[nums[i]] = 0
	nums_count[nums[i]]+=1

max = 0
modes = []
for i in nums_count.keys():
	if nums_count[i] > max:
		max = nums_count[i]
for i in nums_count.keys():
	if nums_count[i] == max:
		modes.append(i)
if len(modes) > 1:
	mode = modes[1]
else:
	mode = modes[0]
if sum >= 0:
	avg = (sum / n) + 0.5
else:
	avg = (sum / n) - 0.5
mid = nums[n//2]
rang = nums[-1] - nums[0]

print(int(avg))
print(mid)
print(mode)
print(rang)