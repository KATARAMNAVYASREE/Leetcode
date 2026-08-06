class Solution(object):
    def twoSum(self, nums, target):
        n = {}
        for i, num in enumerate(nums):
            if target - num in n:
                return [n[target - num], i]
            n[num] = i
