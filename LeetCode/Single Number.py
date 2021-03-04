class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_count = {}
        for i in range(len(nums)):
            if nums[i] in nums_count:
                nums_count[nums[i]] += 1
            else:
                nums_count[nums[i]] = 1
        answer = -1
        for i in nums_count.keys():
            if nums_count[i] == 1:
                answer = i
                break
        return answer