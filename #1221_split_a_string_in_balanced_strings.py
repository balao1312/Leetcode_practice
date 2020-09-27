class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        splits = 0
        for each in s:
            balance += 1 if each == 'L' else -1
            if balance == 0:
                splits += 1

        return splits
