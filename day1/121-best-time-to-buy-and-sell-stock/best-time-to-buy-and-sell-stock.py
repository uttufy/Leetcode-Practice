class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        buy = prices[0]
        profit = 0

        for curr in prices:
            if curr < buy:
                buy = curr
            else: 
                profit = max(profit, curr-buy)
            
        return profit

