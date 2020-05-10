# https://leetcode.com/problems/climbing-stairs/


class Solution:
    def climbStairs(self, n: int) -> int:
        if n in (0, 1):
            return 1
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
