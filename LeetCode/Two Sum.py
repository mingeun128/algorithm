class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        find_index = {}
        for i in range(len(nums)):
            if nums[i] not in find_index:
                find_index[nums[i]] = []
            find_index[nums[i]].append(i)
        for i in range(len(nums)):
            if (target - nums[i]) in find_index:
                if find_index[target - nums[i]][-1] != i:
                    answer.append(i)
                    answer.append(find_index[target - nums[i]].pop())
                    return answer