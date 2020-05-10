# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, num in enumerate(nums):
            hm[num] = i
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hm.keys() and hm[complement] != i:
                return [i, hm[target - num]]
