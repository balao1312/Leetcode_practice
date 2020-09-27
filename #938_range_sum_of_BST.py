# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Solution 1
    # def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    #     if root is None:
    #         return 0
    #
    #     if L <= root.val <= R:
    #         return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
    #     else:
    #         return self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)

    # Solution2
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.ans = 0

        def helper(node, L, R):
            if node:
                # Using the BST property
                # If val of the root you're currently at is less than the lower limit of the range, just search the right subtree
                if node.val < L:
                    helper(node.right, L, R)
                elif node.val > R:
                    helper(node.left, L, R)
                # If val of current root is within limits, add it to the ans and move on to the children
                else:
                    self.ans += node.val
                    helper(node.left, L, R)
                    helper(node.right, L, R)

        helper(root, L, R)

        return self.ans

