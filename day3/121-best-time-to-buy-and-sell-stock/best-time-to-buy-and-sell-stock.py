class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        buy = prices[0]
        res = 0

        for i in range(len(prices)):
            curr = prices[i]

            if curr > buy:
                res = max(res, curr-buy)
            elif curr < buy:
                buy = curr
        
        return res