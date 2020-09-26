class Solution:
    def restoreString(self, s: str, indices) -> str:
        output = [None for x in range(len(s))]
        for index, each in enumerate(indices):
            output[each] = s[index]
        result = ''.join(output)
        return result
