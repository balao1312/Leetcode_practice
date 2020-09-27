class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [2 * x + start for x in range(n)]
        output = nums[0]
        for i in range(1, len(nums)):
            output = nums[i] ^ output
        return output
