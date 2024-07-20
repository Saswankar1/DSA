class Solution(object):
    def twoSum(self, nums, target):
        indices = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in indices:
                return [indices[complement], i]
            indices[num] = i
        return []
