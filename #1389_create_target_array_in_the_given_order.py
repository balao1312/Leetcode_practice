class Solution:
    def createTargetArray(self, nums, index):
        output = []
        for i, each in enumerate(index):
            output.insert(each, nums[i])
        return output
