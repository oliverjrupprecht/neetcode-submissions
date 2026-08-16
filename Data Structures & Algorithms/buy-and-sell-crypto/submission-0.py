class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we want to return the max(prices) - min(prices) where the max price is in the future
        # could do it in n2 time

        max_profit = 0
        for i in range(len(prices)):
            price = prices[i]
            profit = 0
            for j in range(i+1, len(prices)):
                profit = max(profit, prices[j] - prices[i])
            
            max_profit = max(profit, max_profit)

        return max_profit 
        