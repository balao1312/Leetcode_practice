class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result_list = []
        total_for_now = 0
        for each in nums:
            total_for_now += each
            result_list.append(total_for_now)

        return result_list
