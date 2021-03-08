class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in nums:
            if i == 0:
                count+=1
        if count == 0:
            return
        i=0
        end = len(nums) - count
        while i < end:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i+=1
        