# https://leetcode.com/problems/cousins-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        levels = {}

        def traverse(node, parent, level):
            if not node:
                return
            levels[level] = levels.get(level, {})
            levels[level].update({node.val: parent})
            traverse(node.left, node.val, level + 1)
            traverse(node.right, node.val, level + 1)

        traverse(root, None, 0)
        # print(levels)

        for l in levels:
            if x in levels[l] and y in levels[l]:
                if levels[l][x] != levels[l][y]:
                    return True
        return False
