# https://leetcode.com/problems/coin-change/


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + max(coins) + 1] * (amount + 1)
        dp[0] = 0
        for amt in range(1, len(dp)):
            for coin in coins:
                if amt - coin >= 0:
                    dp[amt] = min(dp[amt - coin] + 1, dp[amt])
        return dp[amount] if dp[amount] != amount + max(coins) + 1 else -1
