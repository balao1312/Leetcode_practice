class Solution:
    def longestCommonPrefix(self, strs) -> str:
        common_strings = ''
        if not strs:
            return common_strings

        if len(strs) == 1:
            return strs[0]

        for character in range(len(strs[0])):
            in_all_words = 0
            for words in range(1, len(strs)):
                try:
                    if strs[0][character] == strs[words][character]:
                        in_all_words = 1
                    else:
                        in_all_words = 0
                        break
                except IndexError:
                    in_all_words = 0
                    break

            if in_all_words == 1:
                common_strings += strs[0][character]
            else:
                break

        return common_strings


a = Solution()

print(a.longestCommonPrefix(['bb']))
