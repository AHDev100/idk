class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        ret = 0
        minPrice = prices[0]
        for i in range(1, len(prices)):
            profit = prices[i] - minPrice
            minPrice = min(prices[i], minPrice)
            ret = max(profit, ret)
        return ret
        