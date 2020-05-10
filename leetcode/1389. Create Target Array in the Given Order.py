# https://leetcode.com/problems/create-target-array-in-the-given-order/


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = list()
        for num, i in zip(nums, index):
            target.insert(i, num)

        return target
