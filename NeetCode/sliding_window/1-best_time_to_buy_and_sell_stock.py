# Solution with dynamic programming approach to find the maximum profit from a list of stock prices.
# Time complexity: O(n) where n is the length of the input string.
# Space complexity: O(1)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_profit = 0

        for sell in prices:
            profit = sell - min_buy
            min_buy = min(min_buy, sell)
            max_profit = max(max_profit, profit)

        return max_profit
