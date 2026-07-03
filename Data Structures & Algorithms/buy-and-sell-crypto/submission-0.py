class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        c, p = -1, 0
        
        for i in range(len(prices)):
            if prices[i] < c or c == -1:
                c = prices[i]
            p = max(p, prices[i] - c)
        
        return p