# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            j = abs(nums[i]) - 1
            nums[j] = abs(nums[j]) * -1
        return [i + 1 for i, x in enumerate(nums) if x > 0]
