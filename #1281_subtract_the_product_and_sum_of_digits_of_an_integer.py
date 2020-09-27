class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        str_n = str(n)

        total = 1
        to_subtract = 0
        for each in str_n:
            total *= int(each)
            to_subtract += int(each)
        return total - to_subtract
