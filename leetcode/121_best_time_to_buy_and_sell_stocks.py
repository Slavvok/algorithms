"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l = range(len(prices))
        output = [[0 for _ in l] for _ in l]
        profit = 0

        for i in l:
            for j in l:
                if i == j:
                    continue
                val = prices[j] - prices[i]
                output[i][j] = val
                if val >= 0:
                    profit = max(profit, val)
        return profit
