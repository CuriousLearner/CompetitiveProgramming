# https://leetcode.com/problems/majority-element/


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        freq = {}
        for i, num in enumerate(nums):
            freq[num] = freq.get(num, 0) + 1
        for num in nums:
            if freq[num] > (n // 2):
                return num
