class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            sss = int(str(x)[::-1])
        else:
            sss = int('-' + "".join(str(x)[1:][::-1]))

        return (sss) if - 2 ** 31 <= sss <= 2 ** 31 - 1 else 0


a = Solution()
print(a.reverse(1534236469))



