class Solution:
    def decompressRLElist(self, nums):
        output = []
        index = 0
        while index < len(nums):
            for _ in range(nums[index]):
                output.append(nums[index+1])
            index += 2
        return output
