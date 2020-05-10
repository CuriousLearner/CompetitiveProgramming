# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    summation = 0

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        if not root:
            return 0

        if L <= root.val <= R:
            self.summation += root.val
            self.rangeSumBST(root.left, L, R)
            self.rangeSumBST(root.right, L, R)

        if root.val < L:
            self.rangeSumBST(root.right, L, R)
        if root.val > R:
            self.rangeSumBST(root.left, L, R)

        return self.summation
