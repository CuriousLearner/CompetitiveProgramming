# https://leetcode.com/problems/house-robber-ii/


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        return max(self.robOne(nums[1:]), self.robOne(nums[: len(nums) - 1]))

    def robOne(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0] * (len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[len(nums) - 1]
