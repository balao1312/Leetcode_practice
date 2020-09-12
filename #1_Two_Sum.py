class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        calculated_diff = {}
        for i, num in enumerate(nums):
            new_diff = target - num
            if new_diff not in calculated_diff:
                calculated_diff[num] = i
            else:
                return [calculated_diff[new_diff], i]


a = Solution()
print(a.twoSum([3, 2, 4, 8, 6, 7, 13, 58], 62))

