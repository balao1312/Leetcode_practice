class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = head.val
        while head.next:
            num = num * 2 + head.next.val
            head = head.next
        return num


    def getDecimalValue(self, head) -> int:
        sum = 0
        for ex in range(len(head) - 1, -1, -1):
            print(len(head) - ex - 1)
            print(2 ** ex)
            sum += head[len(head) - 1 - ex] * (2 ** ex)
        return sum
