def solution(numbers):
    answer = ''
    nums = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    temp = ''
    for s in numbers:
        temp += s
        if temp in nums:
            answer += nums[temp]
            temp = ''
    return int(answer)