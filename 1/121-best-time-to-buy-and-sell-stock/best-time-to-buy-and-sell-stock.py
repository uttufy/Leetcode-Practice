class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) == 0:
            return 0
        buy = prices[0]
        sell = buy
        
        profit = 0

        for i in range(1, len(prices)):
            curr = prices[i]
            if curr < buy:
                buy = curr 
            profit = max(profit, curr-buy)

        return profit  
