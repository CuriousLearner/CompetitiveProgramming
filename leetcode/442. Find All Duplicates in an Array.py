# https://leetcode.com/problems/find-all-duplicates-in-an-array/


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                result.append(abs(nums[i]))
            nums[index] = abs(nums[index]) * -1
        return result
