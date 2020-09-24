class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        def sets(n):
            if n == 1:
                return 0
            elif n == 2:
                return 1
            else:
                return n-1 + sets(n - 1)
        
        unique_nums = set(nums)
        total_sets = 0
        for each in unique_nums:
            total_sets += sets(nums.count(each))
        
        return total_sets
