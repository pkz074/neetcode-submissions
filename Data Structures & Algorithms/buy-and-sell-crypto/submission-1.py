class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = prices[0] # largest until now is the first
        profit = 0 

        for price in prices:

            buy = min(buy, price)
            profit = max(profit, price - buy)

        return profit

        