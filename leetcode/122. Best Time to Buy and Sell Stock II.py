# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum([max(0, prices[i + 1] - prices[i]) for i in range(len(prices) - 1)])
