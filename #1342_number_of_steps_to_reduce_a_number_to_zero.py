class Solution:
    def numberOfSteps(self, num: int) -> int:
        times = 0

        while num > 0:
            if num % 2 == 0:
                num = num / 2
                times += 1
            else:
                num -= 1
                times += 1
        return times
