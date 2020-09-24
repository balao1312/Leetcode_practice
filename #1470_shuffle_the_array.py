class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        list_1 = nums[:n]
        list_2 = nums[n:]

        new_list = []
        for index in range(n):
            new_list.append(list_1[index])
            new_list.append(list_2[index])

        return new_list
