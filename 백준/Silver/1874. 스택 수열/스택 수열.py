n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
count = 1
stack = []
opers = []
is_stack_num = True
i=0
while i < n:
    if nums[i] >= count:
        stack.append(count)
        opers.append('+')
        count+=1
    elif nums[i] == stack[-1]:
        stack.pop()
        opers.append('-')
        i+=1
    else:
    	is_stack_num = False
    	break
if is_stack_num == True:
	for i in opers:
	    print(i)
else:
	print('NO')