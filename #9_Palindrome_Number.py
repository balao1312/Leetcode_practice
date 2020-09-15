# 9_Palindrome_Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        rx = str(x)[::-1]
        if rx == str(x):
            return True
        else:
            return False


print(Solution().isPalindrome(1234321))
