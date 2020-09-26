class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        match = 0

        for each_character in J:
            match += S.count(each_character)

        return match
