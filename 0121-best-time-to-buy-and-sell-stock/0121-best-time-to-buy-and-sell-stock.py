from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_Profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                current_profit = prices[r] - prices[l]
                max_Profit = max(max_Profit, current_profit)
                r = r+1
            else:
                l = r
                r = r+1
        return max_Profit
    


        
        