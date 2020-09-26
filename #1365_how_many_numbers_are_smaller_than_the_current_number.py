class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sorted = nums[:]
        sorted.sort()
        result = [sorted.index(x) for x in nums]
        return result
