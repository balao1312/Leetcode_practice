class Solution:
    def sumOddLengthSubarrays(self, arr) -> int:
        total = 0
        for interval in range(1, len(arr) + 1, 2):
            for index in range(len(arr)):
                sub_array = arr[index:index + interval]
                if len(sub_array) != interval:
                    continue
                total += sum(sub_array)
        return total
