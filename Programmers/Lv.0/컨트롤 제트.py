def solution(s):
    answer = 0
    nums = s.split()
    for i in range(len(nums)):
        if nums[i] != 'Z':
            answer += int(nums[i])
        else:
            answer -= int(nums[i-1])
    return answer