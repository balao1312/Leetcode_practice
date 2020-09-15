class Solution:
    def romanToInt(self, s: str) -> int:
        convert_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)):
            try:
                if convert_dict[s[i]] >= convert_dict[s[i + 1]]:
                    result += convert_dict[s[i]]
                else:
                    result -= convert_dict[s[i]]
            except IndexError:
                result += convert_dict[s[i]]
        return result
